# PCCalculatePublic — contratti ed elementi

```mermaid
flowchart TB
    F["Calcola A<br/>Function"]
    Ci0["PCCalculatePublicInputContract<br/>Contract"]
    F -->|"hasInputContract"| Ci0
    Ei0_0["Generatore g<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_0
    Ei0_1["Modulus p<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_1
    Ei0_2["Segreto privato a<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_2
    Co0["PCCalculatePublicOutputContract<br/>Contract"]
    F -->|"hasOutputContract"| Co0
    Eo0_0["Valore pubblico A<br/>ContractElement [1..1]"]
    Co0 -->|"hasContractElement"| Eo0_0
```
