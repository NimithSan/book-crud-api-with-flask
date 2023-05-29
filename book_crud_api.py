from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for books
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book[0])

# CREATE a new book
@app.route('/books', methods=['POST'])
def create_book():
    title = request.form.get('title')
    author = request.form.get('author')

    if not title or not author:
        return jsonify({'error': 'Please provide title and author'}), 400

    new_book = {
        'id': len(books) + 1,
        'title': title,
        'author': author
    }
    books.append(new_book)
    return jsonify(new_book), 201

# UPDATE an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'}), 404

    title = request.form.get('title', book[0]['title'])
    author = request.form.get('author', book[0]['author'])

    book[0]['title'] = title
    book[0]['author'] = author

    return jsonify(book[0])

# DELETE a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'}), 404

    books.remove(book[0])
    return jsonify({'message': 'Book deleted'})

# Run the Flask app
if __name__ == '__main__':
    app.run()
