// det meste av det som er under de komentarene har jeg fått hjelp av KI til å skrive eller feilsøke
// Health bar code - only initialize if health element exists
let currentHealth = 100;
let maxHealth = 100;

if (document.getElementById('health')) {
    currentHealth = parseInt(document.getElementById('health').value) || 100;  // Fallback to 100 if invalid
    maxHealth = currentHealth;  

    const stored = localStorage.getItem('currentHealth'); // dette gjør sånn at koden "spør" nettleseren om den har lagret noe med nøkkelen 'currentHealth', om nettleseren ikke finner noe kommer 'null' tilbake
    if (stored !== null) { // her gjør det sånn at hvis nettleseren sender tilbake 'null', så sier dette 'hvis du fant noe (det er ikke 'null')
        const num = Number(stored); // siden 'localStorage' lagrer all data som strings, så må vi omgjøre det tilbake til integers, dette er funksjonen til 'Number(stored)', den gjør om det inne i parantesende til tall så 'Number("100")' blir til 'Number(100)'
        if (Number.isFinite(num)) { // her sjekker koden om 'Number' er et gyldig tall; om nettleseren har lagret søppeldata, så kan det hende at 'Number()' returnerer 'NaN', 'isFinite' avviser 'NaN', 'Infinity' og '-Infinity'
            currentHealth = num; // her blir 'currentHealth' satt til verdien av 'num'
        }
    }
}

function changeHealth(amount) { // denne funksjonen er for å endre 'Health' mengden
    if (!document.getElementById('health')) return; // Skip if health element doesn't exist
    currentHealth += amount; // her står det egentlig 'currentHealth = currentHealth + amount'
    if (currentHealth > maxHealth) { // gjør det sånn at hvis 'currentHealth' er større enn 'maxHealth' så vil 'currentHealth' bli satt til å være like mye som 'maxHealth' 
        currentHealth = maxHealth;
    }
    else if (currentHealth < 0) { // gjør det sånn at 'currentHealth' ikke kan være mindre enn null
        currentHealth = 0;
    }
    try { 
        localStorage.setItem('currentHealth', currentHealth); // dette lagrer etter hver input av brukeren, så verdien alltid er korrekt, selv når fanen i nettleseren blir oppdatert.
    } catch(e) {} // ignorerer error

    updateHealthBar();
}

function updateHealthBar() {
    const healthBar = document.getElementById('health-bar'); // her er 'document' hele siden, og 'getElementById' søker gjennom siden (html-en) for å finne et element med 'health-bar' id-en
    const healthText = document.getElementById('health-text'); 
    
    if (!healthBar || !healthText) return; // ! i kode betyr veldig ofte "NEI", "IKKE" eller "NOT", så f.eks. !== betyr "er ikke lik", i denne konteksten betyr det at hvis ingen av elementene finnes, stop funksjonen nå

    const healthPercentage = (currentHealth / maxHealth) * 100; // dette regner ut prosenten av hp som er igjen ved å dele 'currentHealth' på 'maxHealth' også gange med 100

    healthBar.style.width = healthPercentage + '%'; // dette sier at bredden til 'healthBar' er det samme som 'healthPercentage' + '%', "+ '%'" delen av dette gjør sånn at verdien blir lagret med et '%' symbol på slutten av den. 

    healthText.innerHTML = `${currentHealth}/${maxHealth}`;

    // Update the <output> element's value and text
    const healthOutput = document.getElementById('health');
    healthOutput.value = currentHealth;
    healthOutput.textContent = currentHealth;  // For display

    if (healthPercentage <= 25) {
        healthBar.style.backgroundColor = 'rgb(249,0,0)';
    } else if (healthPercentage <= 50) {
        healthBar.style.backgroundColor = 'rgb(166,249,0)';
    } else {
        healthBar.style.backgroundColor = 'rgb(95,249,0)';
    }
}

updateHealthBar();

function applyChangeFromInput(sign) {
    const input = document.getElementById('health-input');
    const raw = input ? input.value : ''; // dette betyr " hvis 'input' finnes, bruk dens verdi, ellers bruk en tom 'string'("") "
    const value = Number(raw);

    if (!Number.isFinite(value)) return;

    changeHealth(sign * value);

}

// Only update health bar on pages where it exists
if (document.getElementById('health-bar') && document.getElementById('health-text')) {
    updateHealthBar();
}

// Radio Player with persistent state
let radioPlayer = new Audio();
let isPlaying = false;

// Get all station radio inputs
const stationInputs = document.querySelectorAll('input[name="station"]');

// Function to save radio state to localStorage
function saveRadioState(stationUrl, playing) {
    localStorage.setItem('radioStation', stationUrl);
    localStorage.setItem('radioPlaying', playing ? 'true' : 'false');
}

// Function to load and restore radio state
function restoreRadioState() {
    const savedStation = localStorage.getItem('radioStation');
    const wasPlaying = localStorage.getItem('radioPlaying') === 'true';
    
    if (savedStation) {
        // Find and select the station
        const stationInput = document.querySelector(`input[name="station"][value="${savedStation}"]`);
        if (stationInput) {
            stationInput.checked = true;
            
            // If it was playing, resume it
            if (wasPlaying) {
                setTimeout(() => {
                    playStation();
                }, 100);
            }
        }
    }
}

// Function to play the selected station
function playStation() {
    const selectedStation = document.querySelector('input[name="station"]:checked');
    
    if (!selectedStation) {
        alert('Please select a station first');
        return;
    }
    
    const stationUrl = selectedStation.value;
    
    // If playing a different station, stop and load the new one
    if (radioPlayer.src !== stationUrl) {
        radioPlayer.src = stationUrl;
    }
    
    radioPlayer.play();
    isPlaying = true;
    saveRadioState(stationUrl, true);
    console.log('Playing: ' + stationUrl);
}

// Function to stop the radio
function stopStation() {
    radioPlayer.pause();
    isPlaying = false;
    const selectedStation = document.querySelector('input[name="station"]:checked');
    if (selectedStation) {
        saveRadioState(selectedStation.value, false);
    }
    console.log('Radio stopped');
}

// Function to toggle play/pause
function togglePlayPause() {
    if (isPlaying) {
        stopStation();
    } else {
        playStation();
    }
}

// Add event listeners to station inputs to update when user selects a different one
stationInputs.forEach(input => {
    input.addEventListener('change', () => {
        if (isPlaying) {
            playStation(); // Immediately switch to new station
        }
    });
});

// Restore radio state when page loads
window.addEventListener('load', restoreRadioState);

