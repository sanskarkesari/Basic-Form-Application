from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'


mysql = MySQL(app)

# Route for displaying the form
@app.route('/',methods=['GET','POST'])
def form():
    
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        age = request.form['age']
       
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO form (id, name, address, age) VALUES (%s, %s, %s, %s)",(id, name, address, age))
            
        mysql.connection.commit()
        cursor.close()

        return "Success"
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)
