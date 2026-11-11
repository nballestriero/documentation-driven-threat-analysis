# Query SPARQL — esempi del caso

Le query utilizzano gli IRI **candidati** del Turtle R5A. Non si devono eseguire tutte insieme come una sola interrogazione.

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX proc: <https://w3id.org/ddta/process#>
PREFIX dh: <https://example.org/ddta/dh-deterministic-r4#>
PREFIX viz: <https://example.org/ddta/view#>
# 1: dall'attivita' locale alla funzione e ai suoi contratti
SELECT ?parent ?step ?subProcess ?function ?inputContract ?outputContract
WHERE {
  ?parent ddta:hasStep ?step .
  ?step proc:invokesProcess ?subProcess .
  ?subProcess ddta:realizesFunction ?function .
  OPTIONAL { ?function ddta:hasInputContract ?inputContract . }
  OPTIONAL { ?function ddta:hasOutputContract ?outputContract . }
}
ORDER BY ?parent ?step
```

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX proc: <https://w3id.org/ddta/process#>
PREFIX dh: <https://example.org/ddta/dh-deterministic-r4#>
PREFIX viz: <https://example.org/ddta/view#>
# 2: contenuti comunicati dai sottoprocessi (output della funzione emittente)
SELECT ?subProcess ?function ?channel ?element
WHERE {
  ?subProcess ddta:realizesFunction ?function .
  ?function a ddta:CommunicationFunction ;
            viz:communicationRole "send" ;
            ddta:usesChannel ?channel ;
            ddta:hasOutputContract ?contract .
  ?contract ddta:hasContractElement ?element .
}
ORDER BY ?channel ?element
```

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX proc: <https://w3id.org/ddta/process#>
PREFIX dh: <https://example.org/ddta/dh-deterministic-r4#>
PREFIX viz: <https://example.org/ddta/view#>
# 3: transizioni e guardie per processo
SELECT ?process ?transition ?from ?to ?condition
WHERE {
  ?process proc:hasTransition ?transition .
  ?transition proc:fromStep ?from ; proc:toStep ?to .
  OPTIONAL { ?transition proc:hasGuard ?condition . }
}
ORDER BY ?process ?transition
```

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX proc: <https://w3id.org/ddta/process#>
PREFIX dh: <https://example.org/ddta/dh-deterministic-r4#>
PREFIX viz: <https://example.org/ddta/view#>
# 4: canali con estremi racchiusi in boundary diversi
SELECT ?channel ?sourceBoundary ?destinationBoundary
WHERE {
  ?channel a ddta:CommunicationChannel ;
           ddta:hasSource ?src ; ddta:hasDestination ?dst .
  ?sourceBoundary ddta:encloses ?src .
  ?destinationBoundary ddta:encloses ?dst .
  FILTER (?sourceBoundary != ?destinationBoundary)
}
ORDER BY ?channel
```
