from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#configuracion conexion mysql
#local
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'redes1p2'
#topologia
"""app.config['MYSQL_HOST'] = '192.168.137.140'
app.config['MYSQL_USER'] = 'redes'
app.config['MYSQL_PASSWORD'] = 'redes'
app.config['MYSQL_DB'] = 'r1_p2'"""

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Libro')
    data = cur.fetchall()
    return render_template('index.html', libros = data)

@app.route('/addBook', methods = ['POST'])
def addBook():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Libro (NOMBRE,PRECIO) VALUES (%s,%s)',(nombre,precio))
        mysql.connection.commit()
        flash('Book added successfully!')
        return redirect(url_for('index'))

@app.route('/vendedores')
def vendedores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM vendedor')
    data = cur.fetchall()
    return render_template('vendedor.html', vendedores = data)

@app.route('/addVendedor', methods = ['POST'])
def addVendedor():
    if request.method == 'POST':
        dpi = request.form['dpi']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO vendedor (DPI,NOMBRE,APELLIDO,DIRECCION,TELEFONO) VALUES (%s,%s,%s,%s,%s)',(dpi,nombre,apellido,direccion,telefono))
        mysql.connection.commit()
        flash('Seller added successfully!')
        return redirect(url_for('vendedores'))

@app.route('/ventas')
def ventas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id_vendedor,nombre FROM vendedor')
    list_vendedores = cur.fetchall()
    cur.execute('SELECT id,nombre FROM libro')
    list_libros = cur.fetchall()
    cur.execute('SELECT venta.fecha,libro.nombre,vendedor.nombre FROM venta,libro,vendedor WHERE venta.id_libro = libro.id AND venta.id_vendedor = vendedor.id_vendedor')
    list_ventas = cur.fetchall()
    return render_template('ventas.html', vendedores = list_vendedores, libros = list_libros, ventas = list_ventas)

@app.route('/addVenta', methods = ['POST'])
def addVenta():
    if request.method == 'POST':
        id_libro = request.form['id_libro']
        id_vendedor = request.form['id_vendedor']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO venta (FECHA,ID_LIBRO,ID_VENDEDOR) VALUES (CURRENT_TIMESTAMP,%s,%s)',(id_libro,id_vendedor))
        mysql.connection.commit()
        flash('Sale added successfully!')
        return redirect(url_for('ventas'))

@app.route('/showBook')
def showBook():
    return 'Books'

if __name__ == '__main__':
    app.run(port = 3000, debug=True)