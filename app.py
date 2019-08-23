from flask import Flask,jsonify,request

app = Flask(__name__)

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

@app.route('/books',methods = ['POST'])
def add_books():
    return jsonify(request.get_json())

app.run(port = 5000) #default port of the code
