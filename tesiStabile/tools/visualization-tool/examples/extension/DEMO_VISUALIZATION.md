# Guida grafica DEMO — estensione per test automatici

Questa guida contiene classi e relazioni **solo sintetiche**, non nuove classi DDTA CORE. Serve a verificare che il toolkit accetti una seconda ontologia senza adattare Python.

```yaml ddta-visualization
record: class-style
module: demo
target: demo:Processor
status: proposed
node:
  shape: rectangle
style:
  fill: "#E0F2FE"
  stroke: "#0369A1"
  color: "#0369A1"
  strokeWidth: 1.5
  strokePattern: solid
```

```yaml ddta-visualization
record: relation-style
module: demo
target: demo:leadsTo
status: proposed
representation:
  type: directed-edge
  source: subject
  destination: object
  drawEdge: true
line:
  stroke: "#0369A1"
  strokeWidth: 1.5
  strokePattern: solid
label:
  text: leadsTo
  placement: on-edge
```
