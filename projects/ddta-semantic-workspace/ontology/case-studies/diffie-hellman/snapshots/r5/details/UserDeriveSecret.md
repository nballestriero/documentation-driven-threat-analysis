# UserDeriveSecret — contratti ed elementi

```mermaid
flowchart TB
    F["Deriva K_User<br/>Function"]
    Ci0["UserDeriveSecretInputContract<br/>Contract"]
    F -->|"hasInputContract"| Ci0
    Ei0_0["A_r accettato (richiesto)<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_0
    Ei0_1["Modulus p<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_1
    Ei0_2["Segreto privato b<br/>ContractElement [1..1]"]
    Ci0 -->|"hasContractElement"| Ei0_2
    Co0["UserDeriveSecretOutputContract<br/>Contract"]
    F -->|"hasOutputContract"| Co0
    Eo0_0["Segreto condiviso K_User<br/>ContractElement [1..1]"]
    Co0 -->|"hasContractElement"| Eo0_0
```
