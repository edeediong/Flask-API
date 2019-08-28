from flask import Flask,jsonify,request,Response
import json
from settings import *

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 9780007661428
    },
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 9780385372114
    },
    {
    "name": "A",
    "price": 8.99,
    "isbn": 9785040381791
    }
]

@app.route('/books') #GET store
def get_books():
    '''Function is printed when the /home route is called'''
    return jsonify({'books': books})

@app.route('/') #GET Default
def default():
    return 'This is the Default Link'

@app.route('/books/<int:isbn>') #GET ISBN
def get_book_bs_isbn(isbn):
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)

def validBookObject(bookObject):
    if 'name' in bookObject and 'price' in bookObject and 'isbn' in bookObject:
        return True
    else:
        return False

@app.route('/books',methods = ['POST'])
def add_books():
    request_data = request.get_json()
    if (validBookObject(request_data)):
        new_book = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': request_data['isbn']
        }
        books.insert(0,new_book)
        response = Response("",201,mimetype="application/json")
        response.headers['Location'] = "books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error":'Invalid book object passed in request',
            "helpString": "Data passed om similar to this {'name':'bookname','price':7.9,'isbn': 9780007661428}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),status=400,mimetype='application/json');
        return 'False'
#PUT route
@app.route('/books/<int:isbn>',methods = ['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        "name": request_data["name"],
        "price": request_data["price"],
        "isbn": isbn
    }
    i = 0
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i+= 1
    response = Response("", status=204)

@app.route('/books/<int:isbn>',methods = ['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if "name" in request_data:
        updated_book["name"] = request_data["name"]
    if "price" in request_data:
        updated_book["price"] = request_data["price"]
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            book.update(updated_book)
    response = Response("",status=204)
    response.headers["Location"] = "/books/" + str(isbn)
    return response

@app.route('/books/<int:isbn>',methods = ['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            response = Response("",status=204)
            return response
        i += 1
    invalidBookObjectErrorMsg = {"error": "ISBN not found. Deletion couldn't be completed"}
    response = Response(json.dump(invalidBookObjectErrorMsg),status=400,mimetype= "application/json")
    return response
app.run(port = 5000) #default port of the code
