# About DVC(Data Version Control):
If input files change, only the affected steps are re-executed, making training efficient. It keeps track of the pipeline.

**`Example:`** Instead of retraining everything, you can reuse cached stages when only part of the pipeline changes.

1. **DVC helps track large datasets** just like Git tracks code.  
2. It **stores data remotely** (Google Drive, AWS) instead of inside Git.  
3. You can **switch between dataset versions** easily.  
4. It **remembers changes** in data, preprocessing, and models.  
5. It **saves time** by reusing previous results instead of retraining everything.  
6. Teams can **share and update datasets** without conflicts.  
7. It works with **MLflow to track models and automate ML pipelines**.

### Sample DVC:
**`dvc.yaml`**:

```yaml

stages:
  data_ingestion:
    cmd: python -m src.cnnClassifier.pipeline.stage_01_data_ingestion
    deps:
      - src/cnnClassifier/pipeline/stage_01_data_ingestion.py
      - config/config.yaml
    outs:
      - artifacts/data_ingestion/PLD_3_Classes_256

  prepare_base_model:
    cmd: python -m src.cnnClassifier.pipeline.stage_02_prepare_base_model
    deps:
      - src/cnnClassifier/pipeline/stage_02_prepare_base_model.py
      - config/config.yaml
    params:
      - IMAGE_SIZE
      - INCLUDE_TOP
      - CLASSES
      - WEIGHTS
      - LEARNING_RATE
    outs:
      - artifacts/prepare_base_model

  training:
    cmd: python -m src.cnnClassifier.pipeline.stage_03_model_trainer
    deps:
      - src/cnnClassifier/pipeline/stage_03_model_trainer.py
      - config/config.yaml
      - artifacts/data_ingestion/PLD_3_Classes_256
      - artifacts/prepare_base_model
    params:
      - IMAGE_SIZE
      - EPOCHS
      - BATCH_SIZE
      - AUGMENTATION
    outs:
      - artifacts/training/model.h5

  evaluation:
    cmd: python -m src.cnnClassifier.pipeline.stage_04_model_evaluation.py
    deps:
      - src/cnnClassifier/pipeline/stage_04_model_evaluation.py
      - config/config.yaml
      - artifacts/data_ingestion/PLD_3_Classes_256
      - artifacts/training/model.h5
    params:
      - IMAGE_SIZE
      - BATCH_SIZE
    metrics:
    - scores.json:
        cache: false

```

**`Run DVC`**:
   -  ```shell
      dvc init
      ```
   -  This code will run the `dvc.yaml` file. It will run stage wise.
      ```shell
      dvc repro
      ```