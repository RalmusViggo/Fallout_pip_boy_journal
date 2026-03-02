/* import isDarkColor from './isDarkColor.js';
import { createApp } from 'vue'
import App from './App.vue' // Importing the "Root" component

createApp(App).mount('#app')
*/

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

// Attempt to remember health in localStorage so it survives reloads in the same browser
let currentHealth = 100;
const stored = localStorage.getItem('currentHealth');
if (stored !== null) {
    // parse the saved value and ignore if it's not a number
    const num = Number(stored);
    if (Number.isFinite(num)) {
        currentHealth = num;
    }
}
const maxHealth = 100;

function changeHealth(amount) {
    currentHealth += amount;

    // store after every change so reloads see the updated value
    try {
        localStorage.setItem('currentHealth', currentHealth);
    } catch (e) {
        // localStorage might be unavailable (e.g. privacy modes); ignore errors
    }

    // Constrain health within valid range (0 to maxHealth)
    if (currentHealth > maxHealth) {
        currentHealth = maxHealth;
    } else if (currentHealth < 0) {
        currentHealth = 0;
    }

    updateHealthBar();
}

function updateHealthBar() {
    const healthBar = document.getElementById('health-bar');
    const healthText = document.getElementById('health-text');

    // If the expected DOM elements are missing, do nothing (prevents console errors)
    if (!healthBar || !healthText) return;

    // Calculate the percentage: (current / max) * 100
    const healthPercentage = (currentHealth / maxHealth) * 100;

    // Update the width of the inner bar
    healthBar.style.width = healthPercentage + '%';
    
    // Update the displayed text
    healthText.innerHTML = `${currentHealth}/${maxHealth}`;

    // Optional: Change color based on percentage
    if (healthPercentage <= 25) {
        healthBar.style.backgroundColor = 'rgb(249, 0, 0)';
    } else if (healthPercentage <= 50) {
        healthBar.style.backgroundColor = 'rgb(166, 249, 0)';
    } else {
        healthBar.style.backgroundColor = 'rgb(95, 249, 0)';
    }
}

// Initialize the health bar on page load
updateHealthBar();

// Helper used by the buttons: read the numeric input and apply sign (1 or -1)
function applyChangeFromInput(sign) {
    const input = document.getElementById('health-input');
    const raw = input ? input.value : '';
    const value = Number(raw);

    // If user enters something invalid, treat as 0
    if (!Number.isFinite(value)) return;

    changeHealth(sign * value);
}

