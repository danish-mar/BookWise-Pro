from flask import Flask, request, redirect, url_for

import mysql.connector

app = Flask(__name__)

@app.route('/add-book', methods=['GET','POST'])
def add_book():
    if request.method == 'POST':
        try:
            # Get book details from the form
            title = request.form['title']
            author = request.form['author']
            publisher = request.form['publisher']
            isbn = request.form['isbn']
            price = request.form['price']
            category = request.form['category']
            publishYear = request.form['publishYear']
            scheme = request.form['scheme']
            source = request.form['source']  # Added source field

            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='test@123',
                database='library0'
            )

            cursor = connection.cursor()

            # Insert book details into the Books table
            cursor.execute("INSERT INTO Books (title, authorName, publisher, isbn, price, category, publishYear, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (title, author, publisher, isbn, price, category, publishYear, source))

            # Commit changes and close the database connection
            connection.commit()
            connection.close()

            return redirect(url_for('success'))
        except Exception as e:
            # Handle any exceptions that might occur during the database operation
            return f"An error occurred: {str(e)}"
    elif  request.method == 'GET':
        pass

@app.route('/success')
def success():
    return "Book added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
