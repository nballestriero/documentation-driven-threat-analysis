# PCGeneratePrivate — contratti ed elementi

```mermaid
flowchart TB
    F["Genera segreto a<br/>Function"]
    Ci0["PCGeneratePrivateInputContract<br/>Contract"]
    F -->|"hasInputContract"| Ci0
    Ei0_0["Materiale casuale imprevedibile<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_0
    Ei0_1["Modulus p<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_1
    Ei0_2["Ordine q (se applicabile)<br/>ContractElement [0..1]"]
    Ci0 -->|"hasContractElement"| Ei0_2
    Co0["PCGeneratePrivateOutputContract<br/>Contract"]
    F -->|"hasOutputContract"| Co0
    Eo0_0["Segreto privato a<br/>ContractElement [1..1]"]
    Co0 -->|"hasContractElement"| Eo0_0
```
