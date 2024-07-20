# flower-species-classifier Project

This project demonstrates a basic MLOps pipeline using Docker, Kubernetes, and Pyenv to manage Python environments. It includes a classification model trained with the Iris dataset.

This model is a simple API that provides predictions about a flower's species based on its characteristics. It is built using a Random Forest machine learning model trained with the Iris dataset and scikit-learn.

## Setup

### Prerequisites

- Docker
- Kubernetes
- Pyenv

### Installation

1. Set up Pyenv:
    ```sh
    cd scripts
    ./setup_pyenv.sh
    ```

2. Train the model:
    ```sh
    cd scripts
    python train_model.py
    ```

3. Build the Docker image:
    ```sh
    cd app
    docker build -t mlops-app:latest .
    ```

4. Deploy on Kubernetes:
    ```sh
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

## Usage

The API will be available at `http://<external-ip>`. Use an HTTP client (like curl or Postman) to send POST requests to `/predict`.

Example request:
```json
{
  "input": [5.1, 3.5, 1.4, 0.2]
}
```
> These data are the feature values of the flower we want to classify. The code extracts these values from the received JSON, transforms them into a bidimensional numpy array (necessary for the model to make predictions), and then makes the prediction using the loaded model. The prediction is converted into an integer and returned to the client who made the request in JSON format.

The returned response will be similar to:
```json
{
  "prediction": 0
}
```

> Here, `"prediction"` represents the predicted class for the flower species. In the Iris dataset, the numbers are assigned as follows:
> - 0: Setosa
> - 1: Versicolor
> - 2: Virginica

Therefore, in the above example, the prediction `"prediction": 0` indicates that the flower is predicted to be of the Setosa species.
