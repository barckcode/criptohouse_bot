import requests


def all_currencies():
    URL = f"http://0.0.0.0:8000/currencies"
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(URL, headers=headers)
    data = response.json()

    list_all_currencies = {
        f"{data[0]['name']}": f"{data[0]['symbol']}",
        f"{data[1]['name']}": f"{data[1]['symbol']}",
    }

    return list_all_currencies
