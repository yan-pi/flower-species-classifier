# MLOps-UFBA Project

Este projeto demonstra um pipeline básico de MLOps usando Docker, Kubernetes e Pyenv para gerenciar ambientes Python. Ele inclui um modelo de classificação treinado com o conjunto de dados Iris.

Este modelo é uma API simples que fornece previsões sobre a espécie de uma flor com base em suas características. Ela é construída usando um modelo de aprendizado de máquina Random Forest treinado com o conjunto de dados Iris e scikit-learn.

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

## Uso

A API estará disponível em `http://<external-ip>`. Utilize um cliente HTTP (como curl ou Postman) para enviar requisições POST para `/predict`.

Exemplo de requisição:
```json
{
  "input": [5.1, 3.5, 1.4, 0.2]
}
```
> Esses dados são os valores das características da flor que queremos classificar. O código extrai esses valores do JSON recebido, os transforma em um array numpy bidimensional (necessário para que o modelo possa fazer previsões) e, em seguida, faz a previsão usando o modelo carregado. A previsão é convertida em um número inteiro e retornada ao cliente que fez a solicitação em formato JSON.


A resposta retornada será semelhante a:
```json
{
  "prediction": 0
}
```

> Aqui, `"prediction"` representa a classe prevista para a espécie da flor. No conjunto de dados Iris, os números são atribuídos da seguinte forma: 
> - 0: Setosa
> - 1: Versicolor
> - 2: Virginica

Portanto, no exemplo acima, a previsão `"prediction": 0` indica que a flor é prevista como uma espécie Setosa.