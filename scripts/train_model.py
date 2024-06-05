import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Obtém o caminho absoluto para o diretório 'app'
script_dir = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(script_dir, '..', 'app')
output_file = os.path.join(output_dir, 'model.pkl')

# Cria o diretório 'app' se ele não existir
os.makedirs(output_dir, exist_ok=True)

# Carrega o conjunto de dados Iris
iris = load_iris()
X, y = iris.data, iris.target

# Divide os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salva o modelo em um arquivo .pkl
with open(output_file, 'wb') as f:
    pickle.dump(model, f)

print(f"Modelo treinado e salvo como {output_file}")
