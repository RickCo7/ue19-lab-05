# app.py
import requests
import sys

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            print("Erreur lors de la récupération de la blague.")
            return

        if data.get("type") == "single":
            print(f"Blague : {data['joke']}")
        elif data.get("type") == "twopart":
            print(f"Blague : {data['setup']}\nRéponse : {data['delivery']}")
        else:
            print("Format de blague inconnu.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_joke()
