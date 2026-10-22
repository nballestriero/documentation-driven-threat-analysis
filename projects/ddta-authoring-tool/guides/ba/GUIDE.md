# Base Analysis — General Guide

## What is Base Analysis

Base Analysis identifies governed meanings as BAReferents and records assertions about them as BAPropositions. Each proposition uses an operator defined in its own canonical guide.

## BAProposition

The shared contract is [`contracts/ba-proposition.yaml`](contracts/ba-proposition.yaml). An explicit `polarity` is required: `affirmative` asserts the governed fact and `negative` expressly negates it. Missing evidence is neither polarity. `temporalScope` is optional; when supplied, its semantics are not yet verified.

## Operator catalog

See [`operators/`](operators/). These files are the complete recognized-operator set. A sheet with `reviewStatus: reviewed` provides an executable structural rule; draft sheets are not yet executable.

## Validation boundary

The validator checks the declared BA structure, but it cannot by itself establish that a documented assertion is semantically justified or that a BAReferent's identity is consistent across documents.
