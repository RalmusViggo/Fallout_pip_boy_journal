const mysql = require('mysql2'); // Or require('mysql2') for the newer package

const connection = mysql.createConnection({
  host: 'localhost',      // Your MySQL host
  user: 'rasmus',   // Your MySQL username
  password: 'R-asmus150508', // Your MySQL password
  database: 'vault186'        // The database you want to use (optional at first)
});

connection.connect(err => {
  if (err) {
    console.error('Error connecting: ' + err.stack);
    return;
  }
  console.log('Connected as id ' + connection.threadId);
});

// ... (after connection is established in server.js)

connection.query('SELECT * FROM users', (error, results, fields) => {
  if (error) throw error;
  
  // Log the results from the database
  console.log(results); 
  
  // You can iterate over results if needed
  // results.forEach(result => {
  //     console.log(result.name);
  // });
});

// Close the connection when you are done (optional if using a pool)
connection.end();
