FROM python:3.8-slim-buster

# To deploy in ASW, we need AWS cli
RUN apt update -y && apt install awscli -y 
# Creating a directory called app.
WORKDIR /app 
# we will copy all the source codes.
COPY . /app
# Install all the dependencies in the virtual environment
RUN pip install -r requirments.txt
# Will run the app.py
CMD ["python3", "app.py"]