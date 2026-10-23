#!/usr/bin/env python3
"""Deterministic VSIX for the minimal DDTA VS Code extension (stdlib only)."""
import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'vscode' / 'ddta-authoring-pilot'
EPOCH = (2020, 1, 1, 0, 0, 0)

def build(output: Path):
    package_raw = (SOURCE / 'package.json').read_bytes()
    script_raw = (SOURCE / 'extension.js').read_bytes()
    package = json.loads(package_raw)
    for key in ('name', 'publisher', 'version', 'engines'):
        assert key in package, f'Missing manifest field: {key}'
    version = str(package['version'])
    assert package['name'] == 'ddta-authoring-pilot'
    manifest = f'''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
 <Metadata><Identity Id="{escape(package['name'])}" Version="{escape(version)}" Publisher="{escape(package['publisher'])}" Language="en-US"/><DisplayName>{escape(package.get('displayName',package['name']))}</DisplayName><Description xml:space="preserve">{escape(package.get('description','DDTA VS Code adapter'))}</Description><Categories>Other</Categories></Metadata>
 <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code" Version="[{escape(package['engines']['vscode'].lstrip('^'))},)"/></Installation>
 <Dependencies/><Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/><Asset Type="Microsoft.VisualStudio.Code.Extension" Path="extension" Addressable="true"/></Assets>
</PackageManifest>'''.encode('utf-8')
    types = b'''<?xml version="1.0" encoding="utf-8"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="json" ContentType="application/json"/><Default Extension="js" ContentType="application/javascript"/><Default Extension="vsixmanifest" ContentType="text/xml"/></Types>'''
    content = {'[Content_Types].xml': types, 'extension.vsixmanifest': manifest, 'extension/package.json': package_raw, 'extension/extension.js': script_raw}
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
        for name in sorted(content):
            info = ZipInfo(name, EPOCH)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, content[name], compress_type=ZIP_DEFLATED, compresslevel=9)
    verify(output)
    print('VSIX:', output)
    print('SHA256:', hashlib.sha256(output.read_bytes()).hexdigest())

def verify(output: Path):
    with ZipFile(output) as z:
        names=set(z.namelist())
        for name in ('[Content_Types].xml','extension.vsixmanifest','extension/package.json','extension/extension.js'):
            if name not in names: raise ValueError('Missing VSIX member: '+name)
        for filename in ('package.json','extension.js'):
            if z.read('extension/'+filename) != (SOURCE/filename).read_bytes():
                raise ValueError('VSIX differs from source: '+filename)
        meta=json.loads(z.read('extension/package.json'))
        if meta['version'] not in z.read('extension.vsixmanifest').decode('utf-8'):
            raise ValueError('VSIX manifest version mismatch')
    print('VERIFIED: package.json and extension.js byte-for-byte match tracked sources')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output', type=Path)
    p.add_argument('--verify', type=Path)
    args=p.parse_args()
    if args.verify: verify(args.verify)
    else:
        meta=json.loads((SOURCE/'package.json').read_text(encoding='utf-8'))
        build(args.output or BASE/'dist'/f"ddta-authoring-pilot-{meta['version']}.vsix")
if __name__ == '__main__': main()
