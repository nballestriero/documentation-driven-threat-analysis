# Common BAProposition contract

The shared fields are declared in [`ba-proposition.yaml`](ba-proposition.yaml). `id` is locally unique within an owning document, `semanticOperatorKey` selects an operator defined in `../operators/`, `roles` are validated using its guide, and `polarity` is explicitly required. Negative polarity needs an expressly governed negation, not missing evidence.

`temporalScope` is optional. An absent field is valid; an empty or duplicate field is an error. A supplied value yields `BA-TEMPORAL-SCOPE-UNVERIFIED` until temporal semantics have a reviewed grammar.

Current BA parsing supports fenced plain-text propositions inside MR/Decision/FR documents. Cross-document BAReferent resolution, standalone BA files and semantic evidence checking are not implemented. A structural PASS is not a semantic approval.
