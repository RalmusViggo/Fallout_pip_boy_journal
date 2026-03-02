/* import isDarkColor from './isDarkColor.js';
import { createApp } from 'vue'
import App from './App.vue' // Importing the "Root" component

createApp(App).mount('#app')
*/

// global state
let currentHealth = 0;
const maxHealth = 100;

// template injected this before the file
const username = window.username || '';
console.log('JS sees username:', username);

async function initHealth() {
  const stored = localStorage.getItem('currentHealth');
  if (stored !== null) {
    const num = Number(stored);
    if (Number.isFinite(num)) {
      currentHealth = num;
      updateHealthBar();
      return;
    }
  }

  try {
    // use the real username when calling the API
    const resp = await fetch(`/api/health-sum?username=${encodeURIComponent(username)}`);
    if (resp.ok) {
      const json = await resp.json();
      const num = Number(json.total);
      if (Number.isFinite(num)) currentHealth = num;
    }
  } catch (e) {
    // fallback
  }

  if (!Number.isFinite(currentHealth) || currentHealth <= 0) {
    currentHealth = maxHealth;
  }
  updateHealthBar();
}

// call on load
initHealth();

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

