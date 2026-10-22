# Base Analysis — Operator guides

The canonical operator catalog is the set of Markdown files in [`operators/`](operators/). There is no separate operator registry. Each sheet defines the operator meaning and its executable `yaml ba-rule` contract.

An operator is **recognized** only if it has a valid sheet in `operators/`. `reviewStatus: reviewed` activates its structural rule; `draft` is recognized but not executable. Missing sheets mean unknown operators. Invalid sheets fail closed.

The common BAProposition fields are declared in [`contracts/ba-proposition.yaml`](contracts/ba-proposition.yaml). `polarity` is mandatory; `temporalScope` is optional, but its temporal meaning cannot yet be validated. Neither is an operator role.

[`GUIDE.md`](GUIDE.md) describes general BA authoring. [`templates/BA_OPERATOR_GUIDE_TEMPLATE.md`](templates/BA_OPERATOR_GUIDE_TEMPLATE.md) is the format template. Mermaid projection is independent of the BA operator contracts.

A structural PASS checks declared shape, not source sufficiency, BAReferent identity continuity, temporal semantics, or human semantic approval.
