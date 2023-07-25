from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'RonBeky159487',
    'database': 'garage',
}

@app.route('/')
def display_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SELECT query to retrieve data from the 'cars' table
        query = "SELECT * FROM cars"
        cursor.execute(query)

        # Fetch all the rows from the table
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return render_template('index.html', data=data)
    except mysql.connector.Error as e:
        return f"Error: {e}"

# Route to display the "Add Data" form
@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add.html')

# Route to add new data
@app.route('/add', methods=['POST'])
def add_data():
    if request.method == 'POST':
        colour = request.form['colour']
        module = request.form['module']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # INSERT query to add data to the 'cars' table
            query = "INSERT INTO cars (colour, module) VALUES (%s, %s)"
            data = (colour, module)
            cursor.execute(query, data)

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return "Data added successfully!"
        except mysql.connector.Error as e:
            return f"Error: {e}"

# Route to update data
@app.route('/update', methods=['POST', 'GET'])
def update_data():
    if request.method == 'POST':
        id_to_update = request.form['id']
        new_colour = request.form['colour']
        new_module = request.form['module']

        try:
            # Additional validation to check if the module field is empty
            if not new_module:
                raise ValueError("Module field cannot be empty.")

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # UPDATE query to modify data in the 'cars' table
            query = "UPDATE cars SET colour = %s, module = %s WHERE id = %s"
            data = (new_colour, new_module, id_to_update)
            cursor.execute(query, data)

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return "Data updated successfully!"
        except mysql.connector.Error as e:
            return f"Error: {e}"
        except ValueError as ve:
            return str(ve)  # Return the validation error message

    elif request.method == 'GET':
        return render_template('index.html', data=get_data_from_database())  # Replace with your function to get data from the database


# Route to delete data
@app.route('/delete', methods=['POST'])
def delete_data():
    if request.method == 'POST':
        id_to_delete = request.form['id']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # DELETE query to remove data from the 'cars' table
            query = "DELETE FROM cars WHERE id = %s"
            data = (id_to_delete,)
            cursor.execute(query, data)

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return "Data deleted successfully!"
        except mysql.connector.Error as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
