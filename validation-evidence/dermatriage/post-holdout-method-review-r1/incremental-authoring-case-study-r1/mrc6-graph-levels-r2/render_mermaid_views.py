from pathlib import Path
import re, math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parent

BG=HexColor('#F5F8FB')
MR_BG=HexColor('#E9F4FE'); MR_BORDER=HexColor('#73AED6')
NODE_BG=HexColor('#FFFFFF'); NODE_BORDER=HexColor('#3D637C')
ENV_BG=HexColor('#FFFDF6'); ENV_BORDER=HexColor('#B18A22')
PART_BG=HexColor('#F4FAFE'); PART_BORDER=HexColor('#5C99C1')
PROFILE_BG=HexColor('#F4FBF7'); PROFILE_BORDER=HexColor('#4F8B68')
TEXT=HexColor('#23313D'); MUTED=HexColor('#66788A')
GREEN=HexColor('#2F7E58'); BLUE=HexColor('#4E7195')
W,H=1600,900

NODE_RE=re.compile(r'^\s*([A-Za-z0-9_]+)\["(.*)"\]\s*$')
EDGE_RE=re.compile(r'^\s*([A-Za-z0-9_]+)\s+(-\.->|-->)\|"(.*)"\|\s+([A-Za-z0-9_]+)\s*$')
CLASS_RE=re.compile(r'class\s+([^;]+?)\s+([A-Za-z0-9_]+);')

def parse(path):
    txt=path.read_text(encoding='utf-8')
    nodes={}; edges=[]; classes={}
    for line in txt.splitlines():
        m=NODE_RE.match(line)
        if m: nodes[m.group(1)]=m.group(2).replace('\\n','\n')
        m=EDGE_RE.match(line)
        if m: edges.append((m.group(1),m.group(2),m.group(3).replace('\\n','\n'),m.group(4)))
        for cm in CLASS_RE.finditer(line):
            for nid in cm.group(1).split(','): classes[nid.strip()]=cm.group(2)
    return txt,nodes,edges,classes

def rr(c,x,y,w,h,fill,border,r=16,lw=2,dash=None):
    c.saveState(); c.setFillColor(fill); c.setStrokeColor(border); c.setLineWidth(lw)
    if dash: c.setDash(dash)
    c.roundRect(x,y,w,h,r,stroke=1,fill=1); c.restoreState()

def tx(c,x,y,s,size=18,bold=False,color=TEXT,align='left'):
    c.setFont('Helvetica-Bold' if bold else 'Helvetica',size); c.setFillColor(color)
    if align=='center': c.drawCentredString(x,y,s)
    elif align=='right': c.drawRightString(x,y,s)
    else: c.drawString(x,y,s)

def node(c,x,y,w,h,label,kind='core',title_size=19,sub_size=11):
    fill,border={'core':(NODE_BG,NODE_BORDER),'part':(PART_BG,PART_BORDER),'profile':(PROFILE_BG,PROFILE_BORDER),'env':(ENV_BG,ENV_BORDER)}[kind]
    rr(c,x,y,w,h,fill,border,16,2)
    lines=label.split('\n')
    tx(c,x+w/2,y+h/2+9,lines[0],title_size,True,TEXT,'center')
    if len(lines)>1:
        tx(c,x+w/2,y+h/2-24,' / '.join(lines[1:]),sub_size,False,MUTED,'center')

def arrowhead(c,x1,y1,x2,y2,color):
    ang=math.atan2(y2-y1,x2-x1); ah=12; aw=6
    p1=(x2,y2); p2=(x2-ah*math.cos(ang)+aw*math.sin(ang),y2-ah*math.sin(ang)-aw*math.cos(ang)); p3=(x2-ah*math.cos(ang)-aw*math.sin(ang),y2-ah*math.sin(ang)+aw*math.cos(ang))
    p=c.beginPath(); p.moveTo(*p1); p.lineTo(*p2); p.lineTo(*p3); p.close(); c.drawPath(p,stroke=0,fill=1)

def poly(c,pts,color,lw=3,dashed=False,label='',label_xy=None):
    c.saveState(); c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(lw)
    if dashed: c.setDash(8,6)
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    c.drawPath(p,stroke=1,fill=0)
    arrowhead(c,*pts[-2],*pts[-1],color)
    c.restoreState()
    if label and label_xy:
        parts=label.split('\n')
        tx(c,label_xy[0],label_xy[1],parts[0],13,True,color,'center')
        if len(parts)>1: tx(c,label_xy[0],label_xy[1]-16,parts[1],10,False,MUTED,'center')

def outer(c):
    c.setFillColor(BG); c.rect(0,0,W,H,stroke=0,fill=1)
    rr(c,50,55,1500,790,MR_BG,MR_BORDER,30,2)
    tx(c,80,810,"MR-C6 - Predisposizione e inizializzazione dell'ambiente DermaTriage",18,True,HexColor('#2D6A93'))

def edge_lookup(edges,src,dst):
    for s,t,l,d in edges:
        if s==src and d==dst: return t,l
    raise KeyError((src,dst))

def draw_common_left(c,nodes,edges,env_box):
    node(c,95,575,330,125,nodes['DT'],'core')
    node(c,120,355,380,130,nodes['EP'],'core')
    node(c,145,120,390,130,nodes['PROC'],'core')
    # semantic edges read from Mermaid
    typ,lab=edge_lookup(edges,'DT','ENV')
    poly(c,[(425,637),(620,637),(620,env_box[1]+env_box[3]*0.67),(env_box[0],env_box[1]+env_box[3]*0.67)],GREEN,3,typ=='-.->',lab,(575,660))
    typ,lab=edge_lookup(edges,'EP','ENV')
    poly(c,[(500,420),(env_box[0],420)],GREEN,3,typ=='-.->',lab,(620,442))
    typ,lab=edge_lookup(edges,'PROC','EP')
    poly(c,[(340,250),(340,355)],BLUE,3,typ=='-.->',lab,(315,308))

def render_g0(path,nodes,edges):
    c=canvas.Canvas(str(path),pagesize=(W,H)); outer(c)
    env=(1010,350,380,145)
    node(c,*env,nodes['ENV'],'env',20,11)
    draw_common_left(c,nodes,edges,env)
    tx(c,800,82,'G0 - top-level MR-C6 / DEC-C6-01 projection; no environment composition or FR-level detail.',11,False,MUTED,'center')
    c.save()

def render_env_parts(c,nodes,env):
    x,y,w,h=env
    rr(c,x,y,w,h,ENV_BG,ENV_BORDER,22,2)
    tx(c,x+25,y+h-38,'DermaTriageEnvironment',24,True,TEXT)
    tx(c,x+25,y+h-67,'BAReferent - execution environment / whole',11,False,MUTED)
    pos={
        'CR':(x+40,y+h-210,260,100), 'SC':(x+390,y+h-210,260,100),
        'MR':(x+40,y+h-365,260,100), 'DR':(x+390,y+h-365,260,100),
        'EC':(x+215,y+h-520,260,100),
    }
    for nid,p in pos.items(): node(c,*p,nodes[nid],'part',15,9.5)

def render_g1(path,nodes,edges):
    c=canvas.Canvas(str(path),pagesize=(W,H)); outer(c)
    env=(710,120,790,620)
    render_env_parts(c,nodes,env)
    draw_common_left(c,nodes,edges,env)
    tx(c,800,82,'G1 - G0 + direct MR-C6 hasPart composition rendered by containment; no FR-level constraints.',11,False,MUTED,'center')
    c.save()

def render_g2(path,nodes,edges):
    c=canvas.Canvas(str(path),pagesize=(W,H)); outer(c)
    env=(710,205,790,535)
    render_env_parts(c,nodes,env)
    draw_common_left(c,nodes,edges,env)
    # profile below environment, still inside MR-C6 container
    hcp=(800,60,610,100)
    node(c,*hcp,nodes['HCP'],'profile',20,11)
    typ,lab=edge_lookup(edges,'HCP','ENV')
    # target is the environment whole: line lands on environment border, not on a resource part.
    poly(c,[(hcp[0]+hcp[2]/2,hcp[1]+hcp[3]),(hcp[0]+hcp[2]/2,180),(env[0]+230,180),(env[0]+230,env[1])],BLUE,2.7,typ=='-.->',lab,(1035,198))
    tx(c,800,32,'G2 - adds only the accepted named configuration constraint; former FR-C6-01-01 candidate dependOn edges are absent.',11,False,MUTED,'center')
    c.save()

for level in (0,1,2):
    txt,nodes,edges,classes=parse(ROOT/f'MRC6_G{level}_R2.mmd')
    if level==2:
        forbidden=[e for e in edges if e[0]=='PROC' and e[2].startswith('dependOn')]
        if forbidden: raise RuntimeError(f'Forbidden old candidate edges still present: {forbidden}')
        if not any(e[0]=='HCP' and e[3]=='ENV' and e[2].startswith('constrain') for e in edges):
            raise RuntimeError('G2 missing HCP constrain ENV')
    out=ROOT/f'MRC6_G{level}_R2_mermaid_render.pdf'
    [render_g0,render_g1,render_g2][level](out,nodes,edges)
    print(out)
