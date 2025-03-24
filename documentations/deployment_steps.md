# AWS CICD Deployment with GitHub Actions
Steps to deploy the project:

1. Login to AWS console.
2. Create IAM user for deployment.
    ```
    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR(Elastic Container Registery)

    3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess
    ```

3. Create ECR repo to store/save docker image
    ```
    Save the URI: 
    ```

4. Create EC2 Machine(Ubuntu).

5. Open EC2 and install docker in EC2 Machine:
    ```
    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker
    ```

6. Connect EC2 with GitHub:
    ```
    Open GitHub > Open Repo > Go to settings > Go to Action > Select Runner > Click Self Hosted Runner > Run the commands
    ```
    AWS terminal will require `Enter the name of runner` which will be `self-hosted`

7 Setup GitHub Secrets:
    ```
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
    ```