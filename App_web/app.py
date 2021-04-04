from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#configuracion conexion mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'redes1p2'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libro')
    data = cur.fetchall()
    return render_template('index.html', libros = data)

@app.route('/addBook', methods = ['POST'])
def addBook():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO libro (NOMBRE,PRECIO) VALUES (%s,%s)',(nombre,precio))
        mysql.connection.commit()
        flash('Book added successfully!')
        return redirect(url_for('index'))

@app.route('/showBook')
def showBook():
    return 'Books'

if __name__ == '__main__':
    app.run(port = 3000, debug=True)