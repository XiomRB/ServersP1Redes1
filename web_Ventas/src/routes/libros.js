const express = require('express');
const router = express.Router();
const libros_controller = require('../controllers/libros_controller')

router.get('/', libros_controller.list)

router.post('/add',libros_controller.add)

module.exports = router;