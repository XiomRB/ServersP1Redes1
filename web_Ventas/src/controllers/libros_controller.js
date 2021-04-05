const connection = require('../conexion')
const controller = {};

controller.list = (req, res) =>{
    //res.render('libro');
    connection.query('SELECT * FROM Libro', (err, rows)=>{
        if(err) res.json(err);
        res.render('libro', {
            data: rows
        })
    })
    /*req.getConnection((err, conn)=>{
        conn.query('SELECT * FROM Libro', (err, rows)=>{
            if(err) res.json(err);
            res.render('libro', {
                data: rows
            })
        })
    })*/
}

controller.add = (req, res) =>{
    
const data = req.body
    console.log(data)
    connection.query(`INSERT INTO Libro (nombre,precio) VALUES ('${data.name}', ${data.price})`, (err,libro)=>{
        console.log(libro)
        res.redirect('/');
    })
}

module.exports = controller;