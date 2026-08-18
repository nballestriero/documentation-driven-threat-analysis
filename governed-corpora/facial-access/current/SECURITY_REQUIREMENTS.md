# Security Requirements — FR-3.4.2 current R1

Questi documenti sono `SecurityRequirement`, quindi specializzazioni concrete di `SpecializedRequirement`. Ognuno possiede un solo `protectedSecurityProperty`; il failure mode è esplicito nella clausola normativa.

## SEC-3.4.2-C — Confidentiality of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `Confidentiality`

Durante l'esecuzione di `FR-3.4.2`, il contenuto biometrico della `RecognitionCapture` MUST NOT diventare intelligibile a soggetti non autorizzati alla sua conoscenza prima della sua accettazione da parte del `RecognitionProcessor`.

**Failure mode:** contenuto biometrico intelligibile a un soggetto non autorizzato durante il comportamento di delivery.

## SEC-3.4.2-I — Integrity of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `Integrity`

Una modifica non autorizzata della `RecognitionCapture` durante l'esecuzione di `FR-3.4.2` MUST NOT poter essere accettata dal `RecognitionProcessor` come capture valida associata alla richiesta.

**Failure mode:** una capture modificata senza autorizzazione viene accettata come valida.

## SEC-3.4.2-P — Authorized provenance of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `AuthorizedProvenance`

Una `RecognitionCapture` ricevuta nell'esecuzione di `FR-3.4.2` MUST NOT essere accettata come valida se non è stabilito che la sua origine è autorizzata a fornire evidenza per la relativa `RecognitionRequest`.

**Failure mode:** evidenza proveniente da un'origine non autorizzata o non stabilita viene accettata come valida.

## Realization boundary

TLS, mTLS, firme, certificati, WPA, VLAN, device credentials o altri meccanismi non sono prescritti da questi Security Requirements. Se scelti, appartengono a Decision/realization successive.

La correttezza della correlation `RecognitionCapture` ↔ `RecognitionRequest` resta prima di tutto semantica funzionale di `FR-3.4.1/2`; la security analysis potrà chiedere come proteggerla da sostituzione o manipolazione senza riclassificare automaticamente ogni correlation come SecurityRequirement.
