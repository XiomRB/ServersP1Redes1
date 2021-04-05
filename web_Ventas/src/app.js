const express = require('express');
const path =require('path');
const mysql = require('mysql');
const libros_routes = require('./routes/libros');

const app = express();

//config
app.set('port', process.env.PORT || 3000);
app.set('view engine','ejs');
app.set('views', path.join(__dirname, 'views'));

/*/middlewares
app.use(myConnect(mysql,{
    host: 'localhost',
    user: 'root',
    password: 'root',
    port: 3306,
    database: 'r1_p2'
}, 'single'))*/

app.use(express.urlencoded({extended: false}))

//routes
app.use('/',libros_routes)

//static files
app.use(express.static(path.join(__dirname, 'public')))

app.listen(app.get('port'), '192.168.137.130', ()=>{
    console.log("Escuchando");
})

