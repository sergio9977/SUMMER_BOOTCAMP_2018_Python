from pygeocoder import Geocoder
import os

if __name__ == '__name__':
    autor = os.getenv('AUTOR')
    print(autor)
    direccion = 'UMSS'
    print(Geocoder.geocode(direccion)[0].coordinates)