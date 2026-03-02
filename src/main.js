/* import isDarkColor from './isDarkColor.js';
import { createApp } from 'vue'
import App from './App.vue' // Importing the "Root" component

createApp(App).mount('#app')
*/

let currentHealth = 100;
const maxHealth = 100;

function changeHealth(amount) {
    currentHealth += amount;

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

    // Calculate the percentage: (current / max) * 100
    const healthPercentage = (currentHealth / maxHealth) * 100;

    // Update the width of the inner bar
    healthBar.style.width = healthPercentage + '%';
    
    // Update the displayed text
    healthText.innerHTML = `${currentHealth}/${maxHealth}`;

    // Optional: Change color based on percentage
    if (healthPercentage <= 25) {
        healthBar.style.backgroundColor = '#ff0000'; // Red
    } else if (healthPercentage <= 50) {
        healthBar.style.backgroundColor = '#ffa500'; // Orange
    } else {
        healthBar.style.backgroundColor = 'rgb(43, 194, 83)'; // Green
    }
}

// Initialize the health bar on page load
updateHealthBar();
