from bottle import get, request

@get('/cars') 
def getcars():
    cars= [ {'name': 'Audi', 'price': 34535}, {'name': 'Skoda', 'price': 2342234}]

    return dict(data=cars)