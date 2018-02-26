from http import client
from urllib.parse import quote_plus
import json

def geocode(address):
    hostname = 'maps.google.com'
    base = '/maps/api/geocode/json'
    add_plus = quote_plus(address)
    direcion = '{}?address={}'.format(base, add_plus)
    print(hostname+direcion)

    connection = client.HTTPConnection(hostname)
    connection.request('GET', direcion)

    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    results =  reply["results"]
    diccionario_base = results[0]
    address_components = diccionario_base["geometry"]
    location = address_components["location"]
    print(location)

if __name__ == '__main__':
    address = 'UMSS'
    geocode(address)
    address = 'CEIS UMSS (Centro de estudiantes)'
    address += 'cochabamba'
    geocode(address)
