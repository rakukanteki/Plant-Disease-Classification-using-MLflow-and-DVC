# About: 
This documentation gives a concise idea about all the files and directories of this project.

## About the Directories:
- **`templates DIR`**: Contains the frontend, backend codes.

- **`src\cnnClassifier DIR`**: Contains all the dirs, files for modular coding.
    ```
    > components
        - __init__.py
        - data_ingestion.py
        - model_evaluation_mlflow.py
        - model_trainer.py
        - prepare_base_model.py
    
    > config
        - __init__.py
        - configuration.py
    
    > constants
        - __init__.py
    
    > entity
        - __init__.py
        - config_entity.py

    > pipeline
        - __init__.py
        - stage_01_data_ingestion.py
        - stage_02_prepare_base_model.py
        - stage_03_model_trainer.py
        - stage_04_model_evaluation.py
    
    > utils
        - __init__.py
        - common.py
    ```

- **`research DIR`**:
    ```
    - 01_data_ingestion.ipynb
    - 02_prepare_base_model.ipynb
    - 03_model_trainer.ipynb
    - 04_model_evaluation.ipynb
    - trails.ipynb
    ```

- **`logs DIR`**: Contains the project logs, messages, and errors.

- **`documentations DIR`**: Contains the necessary documentations.

- **`config DIR`**: Contains the config.yaml file.

- **`artifacts DIR`**: Contains the dataet, zip file, models, and etc.

## About the files:
- **`template.py`**: Creating the project directory structure.

- **`setup.py`**: To maintain the project metadata. Also to make the project modular, reusable, and clean structure.

- **`requirments.txt`**: The packages needed to be installed within the environment.

- **`params.yaml`**: Stores all the parameters of the model.

- **`main.py`**: The endpoint of the project which we will run.
    ```shell
    python main.py
    ```

- **`dvc.yaml`**:

- **`.gitignore`**: Here we define the functions, files, dirs, and etc to be ignored during pushing to the GitHub repo.

