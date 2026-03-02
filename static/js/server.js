const express = require('express');
const mysql = require('mysql2/promise');

const app = express();
const pool = mysql.createPool({
  host: 'localhost',
  user: 'rasmus',
  password: 'R-asmus150508',
  database: 'vault186',
  waitForConnections: true,
  connectionLimit: 5
});

app.get('/api/health-sum', async (req, res) => {
  try {
    const [rows] = await pool.query(
      'SELECT COALESCE(SUM(endurance),0) + COALESCE(SUM(luck),0) AS total FROM users WHERE username = ?',
      [req.query.username]
    );
    const total = rows && rows[0] ? Number(rows[0].total) : 0;
    res.json({ total });
  } catch (err) {
    res.status(500).json({ error: 'db error' });
  }
});

app.listen(3000);
