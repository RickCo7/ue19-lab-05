# Application app.py

Cette application Python interroge l'API publique JokeAPI pour afficher une blague aléatoire directement dans la console.

## Fonctionnalités
- Récupère une blague aléatoire depuis JokeAPI.
- Affiche le résultat dans le terminal.
- Facile à déployer via Docker.

## Prérequis

- **Python 3.9+** (si vous exécutez l'application localement sans Docker).
- **Docker** (si vous souhaitez exécuter l'application dans un conteneur).

## Installation et utilisation

### 1. Clonez le repository GitHub
```bash
git clone https://github.com/votre-utilisateur/ue19-lab-05.git
cd ue19-lab-05
```

### 2. Installation locale

Si vous souhaitez exécuter l'application sans Docker :

1. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

2. Lancez l'application :
   ```bash
   python app.py
   ```

### 3. Utilisation avec Docker

1. Construisez l'image Docker :
   ```bash
   docker build -t jokes-app .
   ```

2. Exécutez le conteneur :
   ```bash
   docker run --rm jokes-app
   ```

## Structure du projet

- **app.py** : Le script principal qui interroge l'API et affiche une blague.
- **requirements.txt** : Liste des dépendances Python.
- **Dockerfile** : Configuration pour créer une image Docker de l'application.
- **README.md** : Documentation de l'application.

## Exemple de sortie

Lorsque vous exécutez l'application, vous verrez une sortie comme celle-ci :

```
Voici une blague pour vous :
Pourquoi les éléphants n'utilisent-ils pas d'ordinateur ? Parce qu'ils ont peur des souris !
```

## API utilisée

[JokeAPI](https://v2.jokeapi.dev/) est un service API qui permet de récupérer des blagues de manière simple et rapide.

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre une pull request avec vos modifications ou suggérences.

## Licence

--

