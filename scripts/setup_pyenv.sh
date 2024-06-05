#!/bin/bash

# Verifica se pyenv está instalado
if ! command -v pyenv &> /dev/null
then
    echo "Pyenv não encontrado, instalando..."
    curl https://pyenv.run | bash

    # Adiciona pyenv ao PATH e inicializa
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    # eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
else
    echo "Pyenv já está instalado"
fi

# Adiciona pyenv ao PATH e inicializa no caso de script standalone
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Instala a versão do Python especificada
PYTHON_VERSION=3.8.10
pyenv install -s $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION mlops-env

# Ativa o ambiente virtual
pyenv activate mlops-env

# Instala as dependências
pip install --no-cache-dir -r ../app/requirements.txt

echo "Configuração do Pyenv completa."
