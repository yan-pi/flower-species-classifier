# MLOps-UFBA Project

Este projeto demonstra um pipeline básico de MLOps usando Docker, Kubernetes e Pyenv para gerenciar ambientes Python. Ele inclui um modelo de classificação treinado com o conjunto de dados Iris.

## Configuração

### Pré-requisitos

- Docker
- Kubernetes
- Pyenv

### Instalação

1. Configure o Pyenv:
    ```sh
    cd scripts
    ./setup_pyenv.sh
    ```

2. Treine o modelo:
    ```sh
    cd scripts
    python train_model.py
    ```

3. Construa a imagem Docker:
    ```sh
    cd app
    docker build -t mlops-app:latest .
    ```

4. Faça o deploy no Kubernetes:
    ```sh
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

### Uso

A API estará disponível em `http://<external-ip>`. Utilize um cliente HTTP (como curl ou Postman) para enviar requisições POST para `/predict`.

Exemplo de requisição:
```json
{
  "input": [5.1, 3.5, 1.4, 0.2]
}
