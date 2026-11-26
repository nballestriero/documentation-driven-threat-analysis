# Sample extension ontology

This example is for testing only; it is not part of the normative DDTA corpus.

```yaml ddta-namespace
module: network
prefix: network
namespace: https://example.org/ddta/network#
```

```yaml ddta-ontology
record: class
module: network
iri: network:Router
status: approved
label:
  en: Router
  it: Router
definition:
  en: An identifiable network forwarding resource.
  it: Una risorsa di rete identificabile che inoltra pacchetti.
```

```yaml ddta-ontology
record: object-properties
module: network
owner: network:Router
properties:
  - iri: network:connectsTo
    status: approved
    domain: network:Router
    range: network:Router
    label:
      en: connects to
      it: si collega a
    definition:
      en: Associates a router with another resource.
      it: Associa un router a un'altra risorsa.
```
