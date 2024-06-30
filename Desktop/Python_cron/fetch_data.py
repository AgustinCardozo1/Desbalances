# import requests
# import json

# def fetch_data_from_api():
#     url = 'https://example.com/desbalances'  # Reemplaza con la URL real de la API
#     headers = {
#         'Authorization': 'Bearer TOKEN_DE_AUTENTICACION',  # Reemplaza con el token adecuado si es necesario
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         # Procesar los datos según sea necesario
#         with open('data.json', 'w') as file:
#             json.dump(data, file)
#     else:
#         print(f'Error al obtener datos: {response.status_code}')

# if __name__ == "__main__":
#     fetch_data_from_api()



import requests

url = 'http://localhost/desbalances'

try:
    response = requests.get(url)
    response.raise_for_status()  # Esto generará una excepción para respuestas con errores
    data = response.json()  # Si la respuesta está en formato JSON
    print(data)
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

