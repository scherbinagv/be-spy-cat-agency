import requests

THE_CAT_API_URL = "https://api.thecatapi.com/v1/breeds"

def is_valid_breed(breed: str) -> bool:
    try:
        response = requests.get(THE_CAT_API_URL, timeout=5)
        response.raise_for_status()
        breeds = [b["name"].lower() for b in response.json()]
        return breed.lower() in breeds
    except requests.RequestException:
        return False
