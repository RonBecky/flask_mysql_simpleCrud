**MySQL Database with Flask**

This is a simple Flask app that allows you to interact with a MySQL database. The app allows you to add, update, and delete data from the database.

**Requirements**

* Python 3
* Flask
* MySQL

**Instructions**

1. Install the requirements:

```
pip install -r requirements.txt
```

2. Create a MySQL database and a table called `cars`. The table should have the following columns:

    * `id` (integer, primary key)
    * `colour` (string)
    * `module` (integer)

3. Set the `db_config` variable in `app.py` to your MySQL database connection details.

4. Run the app:

```
flask run
```

The app will be available at `http://localhost:5000`.

**Usage**

The app has three main pages:

* **The home page** shows a list of all the cars in the database.
* **The add data page** allows you to add a new car to the database.
* **The update data page** allows you to update an existing car in the database.

To use the app, simply click on the appropriate link on the home page.

**Troubleshooting**

If you have any problems running the app, please check the following:

* Make sure that you have installed all of the requirements.
* Make sure that your MySQL database is running and that you have created the `cars` table.
* Make sure that the `db_config` variable in `app.py` is set to your MySQL database connection details.

If you are still having problems, please open an issue on the GitHub repository.

**Contributing**

Contributions are welcome! Please open a pull request on the GitHub repository if you have any changes or improvements.

**License**

This project is licensed under the MIT License.