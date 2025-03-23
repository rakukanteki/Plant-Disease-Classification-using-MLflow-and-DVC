# ML*flow* in remote server(**DagsHub**):
- **`DagsHub`**: is used to manager complex Data Science, Machine Learning, and Deep Learning Projects. We can launch our ML*flow* server using DagsHub.

- **`How to do this`**?
- For this you must need a repository for your project in GitHub.
    1. Click on `Create Repo`
    2. Click on `Connect a repo`
    3. Click on `Select repo(add revoke) option`
    4. Then select your `repo` and connect.
    5. Get your URI, name, and password. Like this:
    ```
    MLFLOW_TRACKING_URI = "https://dagshub.com/rakukanteki/Plant-Disease-Classification-using-MLflow-and-DVC.mlflow"

    MLFLOW_TRACKING_USERNAME = your_github_username

    MLFLOW_TRACKING_PASSWORD = your_password
    ```
    6. Now open up terminal(if doesn't work then use `GitBash`) and run the following commands one by one:
    ```shell
    export MLFLOW_TRACKING_URI=https://dagshub.com/rakukanteki/Plant-Disease-Classification-using-MLflow-and-DVC.mlflow

    export MLFLOW_TRACKING_USERNAME=your_github_username

    export MLFLOW_TRACKING_PASSWORD=your_password
    ```
    7. Use the following code to run experiments on ML*flow*. (Use ChatGPT)
    ```python
    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")
    ```