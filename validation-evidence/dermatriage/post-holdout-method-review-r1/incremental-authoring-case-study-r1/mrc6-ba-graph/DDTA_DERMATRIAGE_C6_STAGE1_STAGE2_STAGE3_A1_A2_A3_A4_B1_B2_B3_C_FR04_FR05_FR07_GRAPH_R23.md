# DDTA DermaTriage C6 - cumulative graph through FR-C6-01-05 + FR-C6-01-07 provenance - R23

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#FFFFFF","primaryColor":"#FFFFFF","primaryTextColor":"#17324D","primaryBorderColor":"#0047B3","lineColor":"#0047B3","edgeLabelBackground":"#FFFFFF"},"themeCSS":".cluster rect { rx:28px !important; ry:28px !important; } .edgeLabel p { background:#FFFFFF !important; border-radius:10px !important; padding:2px 7px !important; }"}}%%

flowchart LR


    EnvironmentPreparation["EnvironmentPreparation<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-01</span>"]

    DermaTriage("DermaTriage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-02</span>")


    subgraph SECURITY_BOUNDARY_GITHUB["EXTERNAL - projection only"]
        direction TB

        subgraph HP_DermaTriageSourceRepositoryStore["DermaTriageSourceRepositoryStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-04</span>"]
            direction TB

            DermaTriageSourceRepositoryStore[("DermaTriageSourceRepositoryStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-03</span><br/><span style='font-size:9px'>github.com/basil-github/image_classifier</span>")]

            DermaTriageSourceTree_REMOTE@{ shape: doc, label: "DermaTriageSourceTreeArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-04</span><br/><span style='font-size:9px'>image_classifier repository tree</span>" }

            RetrainerSourceArtifact_REMOTE@{ shape: doc, label: "RetrainerSourceArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-07</span><br/><span style='font-size:9px'>retrainer.py / remote occurrence<br/>same BA identity</span>" }

            RequirementsManifestArtifact_REMOTE@{ shape: doc, label: "RequirementsManifestArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-08</span><br/><span style='font-size:9px'>requirements.txt / remote occurrence<br/>same BA identity</span>" }

            DotEnvExampleArtifact_REMOTE@{ shape: doc, label: "DotEnvExampleArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-09</span><br/><span style='font-size:9px'>.env.example / remote occurrence<br/>same BA identity</span>" }

            RAGIndexerScript_REMOTE@{ shape: doc, label: "RAGIndexerScript<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-10</span><br/><span style='font-size:9px'>rag/indexer.py / remote occurrence<br/>same BA identity</span>" }
        end
    end


    subgraph SECURITY_BOUNDARY_GOOGLEDRIVE["EXTERNAL - projection only"]
        direction TB

        subgraph HP_GoogleDriveModelStore["GoogleDriveModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-07</span>"]
            direction TB

            GoogleDriveModelStore[("GoogleDriveModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-04</span><br/><span style='font-size:9px'>Google Drive file URL</span>")]

            EfficientNetWeights_REMOTE@{ shape: doc, label: "EfficientNetB4WeightsArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-07</span><br/><span style='font-size:9px'>efficientnet_b4.pth</span>" }
        end
    end


    subgraph SECURITY_BOUNDARY_HUGGINGFACE["EXTERNAL - projection only"]
        direction TB

        subgraph HP_HuggingFaceModelStore["HuggingFaceModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-07</span>"]
            direction TB

            HuggingFaceModelStore[("HuggingFaceModelStore")]

            Qwen2VL7BModelArtifact_REMOTE@{ shape: doc, label: "Qwen2VL7BModelArtifact<br/><span style='font-size:9px'>Qwen/Qwen2-VL-7B-Instruct</span>" }

            AllMiniLML6V2ModelArtifact_REMOTE@{ shape: doc, label: "AllMiniLML6V2ModelArtifact<br/><span style='font-size:9px'>sentence-transformers/all-MiniLM-L6-v2</span>" }

            BioMistral7BModelArtifact_REMOTE@{ shape: doc, label: "BioMistral7BModelArtifact<br/><span style='font-size:9px'>BioMistral/BioMistral-7B</span>" }
        end
    end


    subgraph SECURITY_BOUNDARY_ISIC["EXTERNAL - projection only"]
        direction TB

        subgraph HP_ISICPublicDatasetStore["ISICPublicDatasetStore"]
            direction TB

            ISICPublicDatasetStore[("ISICPublicDatasetStore<br/><span style='font-size:9px'>locator: NOT SPECIFIED</span>")]

            RAGDatasetArtifact_REMOTE@{ shape: doc, label: "RAGDatasetArtifact<br/><span style='font-size:9px'>remote occurrence - same concrete BA identity</span>" }
        end
    end


    subgraph SECURITY_BOUNDARY_TRAINING_IMAGES["EXTERNAL - projection only"]
        direction TB

        subgraph HP_TrainingImageSourceStore["TrainingImageSourceStore"]
            direction TB

            TrainingImageSourceStore[("TrainingImageSourceStore<br/><span style='font-size:9px'>store / source<br/>locator: NOT SPECIFIED</span>")]

            TrainingImageArtifactCollection_REMOTE@{ shape: doc, label: "TrainingImageArtifactCollection<br/><span style='font-size:9px'>remote occurrence - same concrete BA identity</span>" }
        end
    end


    subgraph DermaTriageEnvironment["DermaTriageEnvironment"]
        direction TB

        ComputeResources("ComputeResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-03</span>")


        subgraph SoftwareComponents["SoftwareComponents<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-04</span>"]
            direction TB

            subgraph HP_DermaTriageSourceCodeStore["DermaTriageSourceCodeStore"]
                direction TB

                DermaTriageSourceCodeStore[("DermaTriageSourceCodeStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-01</span><br/><span style='font-size:9px'>image_classifier/</span>")]

                DermaTriageSourceTree_LOCAL@{ shape: doc, label: "DermaTriageSourceTreeArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-05</span><br/><span style='font-size:9px'>local repository tree</span>" }

                RetrainerSourceArtifact_LOCAL@{ shape: doc, label: "RetrainerSourceArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-06 / BAP-FRC6-01-07-07</span><br/><span style='font-size:9px'>retrainer.py / local occurrence<br/>same BA identity</span>" }

                RequirementsManifestArtifact_LOCAL@{ shape: doc, label: "RequirementsManifestArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-02-03 / BAP-FRC6-01-07-08</span><br/><span style='font-size:9px'>requirements.txt / local occurrence<br/>same BA identity</span>" }

                DotEnvExampleArtifact_LOCAL@{ shape: doc, label: "DotEnvExampleArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-09</span><br/><span style='font-size:9px'>.env.example / local occurrence<br/>same BA identity</span>" }

                DotEnvConfigurationFile_STORE@{ shape: doc, label: "DotEnvConfigurationFile<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-04-05</span><br/><span style='font-size:9px'>.env / local storage occurrence<br/>same BA identity</span>" }

                RAGIndexerScript_LOCAL@{ shape: doc, label: "RAGIndexerScript<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-03 / BAP-FRC6-01-07-10</span><br/><span style='font-size:9px'>rag/indexer.py / local occurrence<br/>same BA identity</span>" }
            end
        end


        subgraph ModelResources["ModelResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-05</span>"]
            direction TB

            ImageUrgencyModelResource("ImageUrgencyModelResource<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-01</span>")

            ClinicalDescriptionModelResource("ClinicalDescriptionModelResource<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-01</span>")

            EmbeddingModelResource("EmbeddingModelResource<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A3-01</span>")

            TriageSynthesisModelResource("TriageSynthesisModelResource<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A4-01</span>")

            subgraph HP_ActiveClassifierStore["ActiveClassifierStore"]
                direction TB

                ActiveClassifierStore[("ActiveClassifierStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-05</span><br/><span style='font-size:9px'>models/</span>")]

                EfficientNetWeights_LOCAL@{ shape: doc, label: "EfficientNetB4WeightsArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-08</span><br/><span style='font-size:9px'>efficientnet_b4.pth</span>" }
            end

            subgraph HP_Qwen2LocalModelStore["Qwen2LocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-05</span>"]
                direction TB

                Qwen2LocalModelStore[("Qwen2LocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-05</span><br/><span style='font-size:9px'>locator: NOT SPECIFIED</span>")]

                Qwen2VL7BModelArtifact_LOCAL@{ shape: doc, label: "Qwen2VL7BModelArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-08</span><br/><span style='font-size:9px'>local occurrence - same concrete BA identity</span>" }
            end


            subgraph HP_MiniLMLocalModelStore["MiniLMLocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A3-05</span>"]
                direction TB

                MiniLMLocalModelStore[("MiniLMLocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A3-05</span><br/><span style='font-size:9px'>locator: NOT SPECIFIED</span>")]

                AllMiniLML6V2ModelArtifact_LOCAL@{ shape: doc, label: "AllMiniLML6V2ModelArtifact<br/><span style='font-size:9px'>local occurrence - same concrete BA identity</span>" }
            end


            subgraph HP_BioMistralLocalModelStore["BioMistralLocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A4-05</span>"]
                direction TB

                BioMistralLocalModelStore[("BioMistralLocalModelStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A4-05</span><br/><span style='font-size:9px'>locator: NOT SPECIFIED</span>")]

                BioMistral7BModelArtifact_LOCAL@{ shape: doc, label: "BioMistral7BModelArtifact<br/><span style='font-size:9px'>local occurrence - same concrete BA identity</span>" }
            end
        end


        subgraph DataResources["DataResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-06</span>"]
            direction TB

            DermaTriageRAGDataset("DermaTriageRAGDataset<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03B1-01</span>")

            subgraph HP_RAGDatasetStore["RAGDatasetStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03B1-05</span>"]
                direction TB

                RAGDatasetStore[("RAGDatasetStore<br/><span style='font-size:9px'>locator: data/RAG_dataset.csv</span>")]

                RAGDatasetArtifact_LOCAL@{ shape: doc, label: "RAGDatasetArtifact<br/><span style='font-size:9px'>data/RAG_dataset.csv</span>" }
            end

            subgraph HP_ProcessedTrainingDataStore["ProcessedTrainingDataStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03B2-05</span>"]
                direction TB

                ProcessedTrainingDataStore[("ProcessedTrainingDataStore<br/><span style='font-size:9px'>locator: data/processed/</span>")]

                ValidationDatasetArtifact@{ shape: doc, label: "ValidationDatasetArtifact<br/><span style='font-size:9px'>data/processed/val.csv</span>" }

                TestDatasetArtifact@{ shape: doc, label: "TestDatasetArtifact<br/><span style='font-size:9px'>data/processed/test.csv</span>" }

                BalancedTrainingDatasetArtifact@{ shape: doc, label: "BalancedTrainingDatasetArtifact<br/><span style='font-size:9px'>data/processed/train_balanced.csv</span>" }
            end


            TrainingImageCollection("TrainingImageCollection<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03C-01</span>")

            HistoricalCaseDescription("HistoricalCaseDescription<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-07</span><br/><span style='font-size:9px'>current source field: DermaTriageRAGDataset.image_description</span>")

            HistoricalCaseEmbedding("HistoricalCaseEmbedding<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FR03-03-06 / BAP-FR03-03-08</span><br/><span style='font-size:9px'>logical intermediate result</span>")

            HistoricalCaseVectorIndex("HistoricalCaseVectorIndex<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FR03-03-08 / BAP-FRC6-01-05-06</span><br/><span style='font-size:9px'>logical initialized vector index</span>")

            subgraph HP_ChromaDBVectorStore["ChromaDBVectorStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-04</span>"]
                direction TB

                ChromaDBVectorStore[("ChromaDBVectorStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-04</span><br/><span style='font-size:9px'>engine: ChromaDB<br/>locator: chroma_db/</span>")]

                HistoricalCaseVectorIndexArtifact@{ shape: doc, label: "HistoricalCaseVectorIndexArtifact<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-05 / BAP-FRC6-01-05-06</span><br/><span style='font-size:9px'>persistent ChromaDB index<br/>chroma.sqlite3 + index files</span>" }
            end

            subgraph HP_TrainingImageStore["TrainingImageStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03C-02</span>"]
                direction TB

                TrainingImageStore[("TrainingImageStore<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03C-02</span><br/><span style='font-size:9px'>locator: data/images/</span>")]

                TrainingImageArtifactCollection_LOCAL@{ shape: doc, label: "TrainingImageArtifactCollection<br/><span style='font-size:9px'>local occurrence - same concrete BA identity</span>" }
            end
        end

        subgraph HP_EnvironmentConfiguration["EnvironmentConfiguration<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-07</span>"]
            direction TB

            EnvironmentConfiguration("EnvironmentConfiguration<br/><span style='font-size:9px'>logical configuration</span>")

            DotEnvConfigurationFile_CONFIG@{ shape: doc, label: "DotEnvConfigurationFile<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-04-04</span><br/><span style='font-size:9px'>.env / configuration realization occurrence<br/>same BA identity</span>" }
        end
    end


    subgraph EnvironmentSetupProcedure["EnvironmentSetupProcedure<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-01</span>"]
        direction TB

        subgraph RepositoryAcquisitionStage["1 - RepositoryAcquisitionStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-02</span>"]
            direction TB

            DermaTriageRepositoryAcquisition("DermaTriageRepositoryAcquisition<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-07-02</span>")
        end


        subgraph SoftwareDependencyInstallationStage["2 - SoftwareDependencyInstallationStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-03</span>"]
            direction TB

            SoftwareDependencyInstallation("SoftwareDependencyInstallation<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-02-04</span><br/><span style='font-size:9px'>pip install -r requirements.txt</span>")
        end


        subgraph ModelResourceAcquisitionStage["3 - ModelResourceAcquisitionStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-04</span>"]
            direction TB

            EfficientNetModelAcquisition("EfficientNetModelAcquisition<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-09</span>")

            Qwen2ModelAcquisition("Qwen2ModelAcquisition<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-09</span>")


            MiniLMModelAcquisition("MiniLMModelAcquisition")


            BioMistralModelAcquisition("BioMistralModelAcquisition")
        end


        subgraph EnvironmentConfigurationStage["4 - EnvironmentConfigurationStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-05</span><br/><span style='font-size:7px;color:#FFFFFF'>FR-C6-01-04</span>"]
            direction TB

            EnvironmentConfigurationMaterialization["EnvironmentConfigurationMaterialization<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-04-02 / BAP-FRC6-01-04-03</span><br/><span style='font-size:9px'>cp .env.example -> .env; edit .env</span>"]

            DotEnvDocumentedConfiguration[".env documented configuration<br/><span style='font-size:8px'>NON-BA source-preservation projection</span><br/><br/><span style='font-size:8px'><b>resource/model</b><br/>EFFICIENTNET_MODEL · RAG_CSV_PATH · CHROMA_DB_PATH<br/>EMBEDDING_MODEL · QWEN2_MODEL · BIOMISTRAL_MODEL<br/><br/><b>retrieval/service</b><br/>TOP_K_RESULTS=5 · API_HOST=0.0.0.0 · API_PORT=5000<br/><br/><b>integration/auth</b><br/>YOUR_API_KEY · B4_API_KEY · B4_BASE_URL<br/>B4_USERNAME · B4_PASSWORD<br/><br/><b>lifecycle</b><br/>RETRAINING_THRESHOLD=50<br/>CNN retraining trigger count</span>"]
        end

        subgraph LocalResourceInitializationStage["5 - LocalResourceInitializationStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-06</span><br/><span style='font-size:7px;color:#FFFFFF'>FR-C6-01-05</span>"]
            direction TB

            HistoricalCaseEmbeddingGeneration["HistoricalCaseEmbeddingGeneration<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-01 / BAP-FR03-03-06 / BAP-FR03-03-07</span>"]

            HistoricalCaseVectorIndexing["HistoricalCaseVectorIndexing<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-05-02 / BAP-FRC6-01-05-03 / BAP-FR03-03-08</span>"]
        end

        subgraph ServiceStartupStage["6 - ServiceStartupStage<br/><span style='font-size:7px;color:#FFFFFF'>BAP-DECC6-01-07</span>"]
            direction TB
            Stage6Anchor[" "]
        end


        RepositoryAcquisitionStage --> SoftwareDependencyInstallationStage
        SoftwareDependencyInstallationStage --> ModelResourceAcquisitionStage
        ModelResourceAcquisitionStage --> EnvironmentConfigurationStage
        EnvironmentConfigurationStage --> LocalResourceInitializationStage
        LocalResourceInitializationStage --> ServiceStartupStage
    end


    subgraph HardwareConfigurationProfile["HardwareConfigurationProfile<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-01-05</span>"]
        direction TB

        MinimumRAM("minimumRAM = 16 GB<br/><span style='font-size:7px;color:#FFFFFF'>BAP-CRC6-01-01-01</span>")

        MinimumStorage("minimumStorage = 50 GB<br/><span style='font-size:7px;color:#FFFFFF'>BAP-CRC6-01-01-02</span>")
    end


    RequiredSoftwareDependencies["RequiredSoftwareDependencies<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-02-01</span>"]

    SoftwareCompositionProfile["SoftwareCompositionProfile<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-02-02</span>"]

    DependencySourceGap["Dependency source / package registry<br/><b>NOT SPECIFIED</b><br/><span style='font-size:8px'>projection of documentation gap - not BA</span>"]

    ImageUrgencyAnalysis("ImageUrgencyAnalysis<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FR03-01-02</span>")

    ClinicalDescriptionGeneration("ClinicalDescriptionGeneration<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FR03-02-02</span>")

    EfficientNetB4["EfficientNet-B4<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A1-03</span>"]

    Qwen2VL7BInstruct["Qwen2-VL-7B-Instruct<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A2-03</span>"]



    ClinicalDescriptionEmbeddingGeneration("ClinicalDescriptionEmbeddingGeneration")

    AllMiniLML6V2["all-MiniLM-L6-v2<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A3-03</span>"]


    MultiSourceTriageSynthesis("MultiSourceTriageSynthesis")

    BioMistral7B["BioMistral-7B<br/><span style='font-size:7px;color:#FFFFFF'>BAP-FRC6-01-03A4-03</span>"]


    RAGDatasetAcquisition("RAGDatasetAcquisition")


    DatasetSplitting("DatasetSplitting")

    PrepareDataScript("PrepareDataScript<br/><span style='font-size:9px'>prepare_data.py</span>")

    TrainingSplit("TrainingSplit<br/><span style='font-size:9px'>logical intermediate result</span>")

    ValidationSplit("ValidationSplit<br/><span style='font-size:9px'>logical result</span>")

    TestSplit("TestSplit<br/><span style='font-size:9px'>logical result</span>")

    TrainingSetBalancing("TrainingSetBalancing")

    SMOTEBalancing["SMOTEBalancing"]

    SMOTEBalancingScript("SMOTEBalancingScript<br/><span style='font-size:9px'>smote_balance.py</span>")

    BalancedTrainingSplit("BalancedTrainingSplit<br/><span style='font-size:9px'>logical result</span>")


    EnvironmentPreparation -->|produce| DermaTriageEnvironment

    DermaTriage -.->|dependOn| DermaTriageEnvironment

    EnvironmentSetupProcedure -.->|realize| EnvironmentPreparation

    HardwareConfigurationProfile -.->|constrain| DermaTriageEnvironment

    RequiredSoftwareDependencies -.->|constrain| DermaTriageEnvironment

    SoftwareCompositionProfile -.->|realize| RequiredSoftwareDependencies

    SoftwareDependencyInstallation -.-|open relation - no BA operator| SoftwareCompositionProfile

    DependencySourceGap -.-|resolution source? OPEN| SoftwareDependencyInstallation

    EfficientNetB4 -.->|realize| ImageUrgencyModelResource

    EfficientNetB4 -.->|realize| ImageUrgencyAnalysis

    Qwen2VL7BModelArtifact_LOCAL -.->|realize| Qwen2VL7BInstruct

    Qwen2VL7BInstruct -.->|realize| ClinicalDescriptionModelResource

    Qwen2VL7BInstruct -.->|realize| ClinicalDescriptionGeneration

    DermaTriageSourceTree_REMOTE -->|transfer| DermaTriageSourceTree_LOCAL

    EfficientNetWeights_REMOTE -->|transfer| EfficientNetWeights_LOCAL

    Qwen2VL7BModelArtifact_REMOTE -->|transfer| Qwen2VL7BModelArtifact_LOCAL

    DermaTriageRepositoryAcquisition -.-|behavior| DermaTriageSourceTree_LOCAL

    EfficientNetModelAcquisition -.-|behavior| EfficientNetWeights_LOCAL

    Qwen2ModelAcquisition -.-|behavior| Qwen2VL7BModelArtifact_LOCAL


    AllMiniLML6V2ModelArtifact_LOCAL -.->|realize| AllMiniLML6V2

    AllMiniLML6V2 -.->|realize| EmbeddingModelResource

    AllMiniLML6V2 -.->|realize| HistoricalCaseEmbeddingGeneration

    AllMiniLML6V2 -.->|realize| ClinicalDescriptionEmbeddingGeneration

    AllMiniLML6V2ModelArtifact_REMOTE -->|transfer| AllMiniLML6V2ModelArtifact_LOCAL

    MiniLMModelAcquisition -.-|behavior| AllMiniLML6V2ModelArtifact_LOCAL


    BioMistral7BModelArtifact_LOCAL -.->|realize| BioMistral7B

    BioMistral7B -.->|realize| TriageSynthesisModelResource

    BioMistral7B -.->|realize| MultiSourceTriageSynthesis

    BioMistral7BModelArtifact_REMOTE -->|transfer| BioMistral7BModelArtifact_LOCAL

    BioMistralModelAcquisition -.-|behavior| BioMistral7BModelArtifact_LOCAL


    RAGDatasetArtifact_LOCAL -.->|realize| DermaTriageRAGDataset

    RAGDatasetArtifact_REMOTE -->|transfer| RAGDatasetArtifact_LOCAL

    RAGDatasetAcquisition -.-|behavior| RAGDatasetArtifact_LOCAL


    DatasetSplitting -->|produce| TrainingSplit

    DatasetSplitting -->|produce| ValidationSplit

    DatasetSplitting -->|produce| TestSplit

    PrepareDataScript -.->|realize| DatasetSplitting

    ValidationDatasetArtifact -.->|realize| ValidationSplit

    TestDatasetArtifact -.->|realize| TestSplit

    TrainingSplit -->|input| TrainingSetBalancing

    TrainingSetBalancing -->|produce| BalancedTrainingSplit

    SMOTEBalancing -.->|realize| TrainingSetBalancing

    SMOTEBalancingScript -.->|realize| SMOTEBalancing

    BalancedTrainingDatasetArtifact -.->|realize| BalancedTrainingSplit

    TrainingImageArtifactCollection_REMOTE -->|transfer| TrainingImageArtifactCollection_LOCAL

    TrainingImageArtifactCollection_LOCAL -.->|realize| TrainingImageCollection


    DotEnvConfigurationFile_CONFIG -.->|realize| EnvironmentConfiguration



    DotEnvExampleArtifact_LOCAL -->|input| EnvironmentConfigurationMaterialization

    EnvironmentConfigurationMaterialization -->|produce| DotEnvConfigurationFile_STORE


    DermaTriageRAGDataset -->|hasPart| HistoricalCaseDescription

    HistoricalCaseDescription -->|input| HistoricalCaseEmbeddingGeneration

    HistoricalCaseEmbeddingGeneration -->|produce| HistoricalCaseEmbedding

    HistoricalCaseEmbedding -->|input| HistoricalCaseVectorIndexing

    HistoricalCaseVectorIndexing -->|produce| HistoricalCaseVectorIndex

    RAGIndexerScript_LOCAL -.->|realize| HistoricalCaseVectorIndexing

    HistoricalCaseVectorIndexArtifact -.->|realize| HistoricalCaseVectorIndex


    DermaTriageSourceTree_REMOTE -->|hasPart| RetrainerSourceArtifact_REMOTE
    DermaTriageSourceTree_REMOTE -->|hasPart| RequirementsManifestArtifact_REMOTE
    DermaTriageSourceTree_REMOTE -->|hasPart| DotEnvExampleArtifact_REMOTE

    DermaTriageSourceTree_LOCAL -->|hasPart| RetrainerSourceArtifact_LOCAL
    DermaTriageSourceTree_LOCAL -->|hasPart| RequirementsManifestArtifact_LOCAL
    DermaTriageSourceTree_LOCAL -->|hasPart| DotEnvExampleArtifact_LOCAL

    DermaTriageSourceTree_REMOTE -->|hasPart| RAGIndexerScript_REMOTE

    DermaTriageSourceTree_LOCAL -->|hasPart| RAGIndexerScript_LOCAL


    classDef BAProduceActor fill:#212121,stroke:#000000,stroke-width:2px,color:#FFFFFF;

    classDef BAReferentD0 fill:#0066FF,stroke:#0047B3,stroke-width:2px,color:#FFFFFF;
    classDef BAReferentD1 fill:#267DFF,stroke:#0047B3,stroke-width:2px,color:#FFFFFF;
    classDef BAReferentD2 fill:#4C94FF,stroke:#0047B3,stroke-width:2px,color:#FFFFFF;

    classDef BARealizationD0 fill:#5F6368,stroke:#3F4347,stroke-width:2px,color:#FFFFFF;
    classDef BARealizationD1 fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF;
    classDef BARealizationD2 fill:#8F9295,stroke:#4C5054,stroke-width:2px,color:#FFFFFF;

    classDef BAConstrainD0 fill:#6F42C1,stroke:#55308F,stroke-width:2px,color:#FFFFFF;
    classDef BAConstrainD1 fill:#855ECA,stroke:#55308F,stroke-width:2px,color:#FFFFFF;

    classDef BAStore fill:#EEF4F9,stroke:#275D86,stroke-width:2px,color:#17324D;

    classDef BAContent fill:#FFFFFF,stroke:#275D86,stroke-width:2px,color:#17324D;

    classDef BALogicalData fill:#FFFFFF,stroke:#5C99C1,stroke-width:2px,color:#23313D;

    classDef BATransferBehavior fill:#FFF4E3,stroke:#A96A16,stroke-width:2px,color:#17324D;

    classDef BADocumentationGap fill:#FFFDF2,stroke:#8A6D1D,stroke-width:1.8px,stroke-dasharray:5 4,color:#5B4A00;
    classDef BANonBAProjection fill:#FFFDF7,stroke:#8A6D1D,stroke-width:1.5px,stroke-dasharray:5 4,color:#5B4A00;

    classDef HiddenAnchor fill:transparent,stroke:transparent,color:transparent;


    class EnvironmentPreparation BAProduceActor;

    class DermaTriage,ImageUrgencyAnalysis,ClinicalDescriptionGeneration,ClinicalDescriptionEmbeddingGeneration,MultiSourceTriageSynthesis BAReferentD0;

    class ComputeResources,EnvironmentConfiguration BAReferentD1;

    class ImageUrgencyModelResource,ClinicalDescriptionModelResource,EmbeddingModelResource,TriageSynthesisModelResource BAReferentD2;

    class TrainingSplit,ValidationSplit,TestSplit,BalancedTrainingSplit,TrainingImageCollection,HistoricalCaseDescription,HistoricalCaseEmbedding,HistoricalCaseVectorIndex BALogicalData;

    class RequiredSoftwareDependencies BAConstrainD0;

    class SoftwareCompositionProfile,EfficientNetB4,Qwen2VL7BInstruct,AllMiniLML6V2,BioMistral7B,PrepareDataScript,SMOTEBalancing,SMOTEBalancingScript BARealizationD0;

    class EnvironmentConfigurationStage,LocalResourceInitializationStage,ServiceStartupStage BARealizationD1;

    class SoftwareDependencyInstallation BARealizationD2;

    class MinimumRAM,MinimumStorage BAConstrainD1;

    class DermaTriageSourceRepositoryStore,DermaTriageSourceCodeStore,GoogleDriveModelStore,ActiveClassifierStore,HuggingFaceModelStore,Qwen2LocalModelStore,MiniLMLocalModelStore,BioMistralLocalModelStore,ISICPublicDatasetStore,RAGDatasetStore,ProcessedTrainingDataStore,TrainingImageStore,TrainingImageSourceStore,ChromaDBVectorStore BAStore;

    class DermaTriageSourceTree_REMOTE,DermaTriageSourceTree_LOCAL,RetrainerSourceArtifact_REMOTE,RetrainerSourceArtifact_LOCAL,RequirementsManifestArtifact_REMOTE,RequirementsManifestArtifact_LOCAL,DotEnvExampleArtifact_REMOTE,EfficientNetWeights_REMOTE,EfficientNetWeights_LOCAL,Qwen2VL7BModelArtifact_REMOTE,Qwen2VL7BModelArtifact_LOCAL,AllMiniLML6V2ModelArtifact_REMOTE,AllMiniLML6V2ModelArtifact_LOCAL,BioMistral7BModelArtifact_REMOTE,BioMistral7BModelArtifact_LOCAL,RAGDatasetArtifact_REMOTE,RAGDatasetArtifact_LOCAL,ValidationDatasetArtifact,TestDatasetArtifact,BalancedTrainingDatasetArtifact,TrainingImageArtifactCollection_REMOTE,TrainingImageArtifactCollection_LOCAL,RAGIndexerScript_REMOTE,RAGIndexerScript_LOCAL,HistoricalCaseVectorIndexArtifact BAContent;

    class DermaTriageRepositoryAcquisition,EfficientNetModelAcquisition,Qwen2ModelAcquisition,MiniLMModelAcquisition,BioMistralModelAcquisition,RAGDatasetAcquisition BATransferBehavior;

    class DatasetSplitting,TrainingSetBalancing,EnvironmentConfigurationMaterialization,HistoricalCaseEmbeddingGeneration,HistoricalCaseVectorIndexing BAProduceActor;

    class DependencySourceGap BADocumentationGap;

    class DotEnvExampleArtifact_LOCAL,DotEnvConfigurationFile_STORE,DotEnvConfigurationFile_CONFIG BAContent;
    class DotEnvDocumentedConfiguration BANonBAProjection;

    class Stage6Anchor HiddenAnchor;

    class DermaTriageRAGDataset BALogicalData;


    style DermaTriageEnvironment fill:#0066FF,stroke:#0047B3,stroke-width:2.5px,color:#FFFFFF

    style SoftwareComponents fill:#267DFF,stroke:#0047B3,stroke-width:2.3px,color:#FFFFFF

    style ModelResources fill:#267DFF,stroke:#0047B3,stroke-width:2.3px,color:#FFFFFF


    style DataResources fill:#267DFF,stroke:#0047B3,stroke-width:2.3px,color:#FFFFFF

    style HP_EnvironmentConfiguration fill:#267DFF,stroke:#0047B3,stroke-width:2.3px,color:#FFFFFF

    style SECURITY_BOUNDARY_GITHUB fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A

    style SECURITY_BOUNDARY_GOOGLEDRIVE fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A

    style SECURITY_BOUNDARY_HUGGINGFACE fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A


    style SECURITY_BOUNDARY_ISIC fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A

    style SECURITY_BOUNDARY_TRAINING_IMAGES fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A

    style HP_DermaTriageSourceRepositoryStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_DermaTriageSourceCodeStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_GoogleDriveModelStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_ActiveClassifierStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_HuggingFaceModelStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D


    style HP_ISICPublicDatasetStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_RAGDatasetStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_ProcessedTrainingDataStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_TrainingImageStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_ChromaDBVectorStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_TrainingImageSourceStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_Qwen2LocalModelStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_MiniLMLocalModelStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style HP_BioMistralLocalModelStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D

    style EnvironmentSetupProcedure fill:#5F6368,stroke:#3F4347,stroke-width:2.5px,stroke-dasharray:6 4,color:#FFFFFF

    style RepositoryAcquisitionStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style SoftwareDependencyInstallationStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style ModelResourceAcquisitionStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style EnvironmentConfigurationStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style LocalResourceInitializationStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style ServiceStartupStage fill:#777A7F,stroke:#4C5054,stroke-width:2px,color:#FFFFFF

    style HardwareConfigurationProfile fill:#6F42C1,stroke:#55308F,stroke-width:2.5px,stroke-dasharray:6 4,color:#FFFFFF




    linkStyle 0 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 1 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 2 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 3 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 4 stroke:#7A7E83,stroke-width:1.3px;

    linkStyle 5 stroke:#0047B3,stroke-width:2px;
    linkStyle 6 stroke:#C69214,stroke-width:1.5px,stroke-dasharray:6 4;
    linkStyle 7 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 8 stroke:#6F42C1,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 9 stroke:#6F42C1,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 10 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 11 stroke:#8A6D1D,stroke-width:1.5px,stroke-dasharray:4 4;
    linkStyle 12 stroke:#8A6D1D,stroke-width:1.5px,stroke-dasharray:4 4;

    linkStyle 13 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 14 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 15 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 16 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 17 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 18 stroke:#C62828,stroke-width:3px;
    linkStyle 19 stroke:#C62828,stroke-width:3px;
    linkStyle 20 stroke:#C62828,stroke-width:3px;

    linkStyle 21 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;
    linkStyle 22 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;
    linkStyle 23 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;

    linkStyle 24 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 25 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 26 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 27 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 28 stroke:#C62828,stroke-width:3px;

    linkStyle 29 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;

    linkStyle 30 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 31 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 32 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 33 stroke:#C62828,stroke-width:3px;
    linkStyle 34 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;

    linkStyle 35 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 36 stroke:#C62828,stroke-width:3px;
    linkStyle 37 stroke:#A96A16,stroke-width:1.5px,stroke-dasharray:5 5;

    linkStyle 38 stroke:#0047B3,stroke-width:2px;
    linkStyle 39 stroke:#0047B3,stroke-width:2px;
    linkStyle 40 stroke:#0047B3,stroke-width:2px;
    linkStyle 41 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 42 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 43 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 44 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 45 stroke:#0047B3,stroke-width:2px;
    linkStyle 46 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 47 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 48 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 49 stroke:#C62828,stroke-width:3px;
    linkStyle 50 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 51 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;

    linkStyle 52 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 53 stroke:#0047B3,stroke-width:2px;



    linkStyle 54 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 55 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 56 stroke:#0047B3,stroke-width:2px;
    linkStyle 57 stroke:#7A7E83,stroke-width:1.3px;
    linkStyle 58 stroke:#0047B3,stroke-width:2px;
    linkStyle 59 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 60 stroke:#5F6368,stroke-width:1.8px,stroke-dasharray:6 4;
    linkStyle 61 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 62 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 63 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 64 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 65 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 66 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 67 stroke:#0047B3,stroke-width:1.8px;
    linkStyle 68 stroke:#0047B3,stroke-width:1.8px;
```
