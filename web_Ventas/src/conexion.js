  
const mysql = require('mysql')

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'r1_p2',
    multipleStatements: 'true'
});

connection.connect(function(error){
    if(!!error) console.log('Error al conectar')
    else console.log('Conectado a Redes1')
})

module.exports = connection