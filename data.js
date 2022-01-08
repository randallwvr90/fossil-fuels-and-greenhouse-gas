var pg = require('pg')

var config = {database: 'fuels'}

var pool = new pg.Pool(config);

pool.connect((err, client, done) => {
    if (err) throw err;
    client.query('SELECT * FROM COUNTRY_MASTER', (err, res)=> {
        if (err)
            console.log(err.stack);
        else {
            console.log(res.rows);
        }
    })
})