from flask import Flask, jsonify, request, Response
import json
from settings import *
from bookModel import *

@app.route('/books')  # GET store
def get_books():
    '''Function is printed when the /home route is called'''
    return jsonify({'books': Book.get_all_books()})


@app.route('/')  # GET Default
def default():
    return 'This is the Default Link'


@app.route('/books/<int:isbn>')  # GET ISBN
def get_book_bs_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)


def validBookObject(bookObject):
    if 'name' in bookObject and 'price' in bookObject and 'isbn' in bookObject:
        return True
    else:
        return False


@app.route('/books', methods=['POST'])
def add_books():
    request_data = request.get_json()
    if (validBookObject(request_data)):
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "books/" + str(new_book['isbn'])
        return response
    else:
        error_msg = str({
            'name': 'bookname',
            'price': 7.9,
            'isbn': 9780007661428})
        invalidAddBookObjectErrorMsg = {
            "error": 'Invalid book object passed in request',
            "helpString": "Data passed om similar to this " + error_msg
        }
        json_file = json.dumps(invalidAddBookObjectErrorMsg)
        response = Response(json_file, status=400, mimetype='application/json')
        return 'False'
# PUT route
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response("", status=204)


@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if "name" in request_data:
        Book.update_book_name(isbn, request_data["name"])
    if "price" in request_data:
        Book.update_book_price(isbn, request_data["price"])
    response = Response("", status=204)
    response.headers["Location"] = "/books/" + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    if(Book.delete_book(isbn)):
        response = Response("", status=204)
        return response
    invalidDelBookObjectErrorMsg = {"error": "ISBN not found. Couldn't delete"}
    json_file = json.dump(invalidDelBookObjectErrorMsg)
    response = Response(json_file, status=400, mimetype="application/json")
    return response


app.run(port=5000)  # default port of the code
