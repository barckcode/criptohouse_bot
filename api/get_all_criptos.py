import requests


def all_criptos():
    URL = f"http://0.0.0.0:8000/criptos"
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(URL, headers=headers)
    data = response.json()

    list_all_criptos = {
        f"{data[0]['name']}": f"{data[0]['symbol']}",
        f"{data[1]['name']}": f"{data[1]['symbol']}",
        f"{data[2]['name']}": f"{data[2]['symbol']}",
        f"{data[3]['name']}": f"{data[3]['symbol']}",
        f"{data[4]['name']}": f"{data[4]['symbol']}",
        f"{data[5]['name']}": f"{data[5]['symbol']}",
        f"{data[6]['name']}": f"{data[6]['symbol']}",
        f"{data[7]['name']}": f"{data[7]['symbol']}",
    }

    return list_all_criptos
