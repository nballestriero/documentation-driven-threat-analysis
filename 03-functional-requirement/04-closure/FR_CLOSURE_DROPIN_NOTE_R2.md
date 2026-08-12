# FR documentation-layer closure drop-in note - R2

Target research repository baseline:

`61df2c935abd1e77dfb9fa0d9b2ebefe45228e26`

This checkpoint coordinates the Macro Requirement, Decision and Functional Requirement working semantics after the final hierarchy discussion.

## Deliberate changes

- project problem framing is a required method precondition, not yet a governed document type;
- documentation hierarchy for thesis scope is normalized to `MR -> Decision -> FR -> SpecializedRequirement`;
- each FR has exactly one parent Decision; MR ownership is derived through that Decision;
- no Decision is a child of FR;
- rare singleton-solution cases use a controlled necessity/default Decision rather than removing the layer;
- FR semantics are strengthened around operational behavior, normative prose and supporting SPO references;
- cross-MR capability consumption does not transfer ownership; exact formal target is deferred to Base Analysis;
- thesis specialized-requirement work will next formalize SecurityRequirement only;
- earlier simplified direct-MR FR examples are excluded from closure evidence.

## Validation corpus

`03-functional-requirement/03-example-order-fulfillment/ORDER_FULFILLMENT_COMPLETE_AUTHORING_PROBE_R3.*`

The warehouse branch explicitly chooses internal inventory authority and includes a counterfactual external-WMS branch to show how the responsibility boundary changes downstream FRs.

## Reopen rule

Reopen the documentation metamodel only for a concrete counterexample from SecurityRequirement, Base Analysis or overlay/plugin integration that cannot be represented without changing these semantics.

Suggested local commit message:

`research: close document hierarchy through Functional Requirement`
