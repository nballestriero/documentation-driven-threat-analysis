# PCKeyAgreement — contratti ed elementi

```mermaid
flowchart TB
    F["PCKeyAgreement<br/>Function"]
    Ci0["PCKeyAgreementInputContract<br/>Contract"]
    F -->|"hasInputContract"| Ci0
    Ei0_0["Generatore g<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_0
    Ei0_1["Modulus p<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_1
    Ei0_2["Valore pubblico B<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_2
    Ei0_3["Ordine q (se applicabile)<br/>ContractElement [0..1]"]
    Ci0 -->|"hasContractElement"| Ei0_3
    Co0["PCKeyAgreementOutputContract<br/>Contract"]
    F -->|"hasOutputContract"| Co0
    Eo0_0["Valore pubblico A<br/>ContractElement [1..1]"]
    Co0 -->|"hasContractElement"| Eo0_0
    Eo0_1["Segreto condiviso K_PC<br/>ContractElement [1..1]"]
    Co0 -->|"hasContractElement"| Eo0_1
```
