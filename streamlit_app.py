/roulette-game
|-- index.html
|-- styles.css
|-- app.js

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roulette Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <h1>Roulette Game</h1>
        <div id="bet-area">
            <h2>Place Your Bet</h2>
            <input type="number" id="bet-amount" placeholder="Enter your bet amount" min="1">
            <select id="bet-type">
                <option value="number">Number (0-36)</option>
                <option value="red">Red</option>
                <option value="black">Black</option>
            </select>
            <input type="number" id="bet-number" placeholder="Enter number (0-36)" min="0" max="36" style="display: none;">
            <button id="place-bet-btn">Place Bet</button>
        </div>
        <div id="result-area" style="display: none;">
            <h2>Result</h2>
            <p id="result-number"></p>
            <p id="result-message"></p>
        </div>
    </div>
    <script src="app.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
    text-align: center;
}

#app {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

input, select {
    margin: 10px 0;
    padding: 10px;
    width: 100%;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
    text-align: center;
}

#app {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

input, select {
    margin: 10px 0;
    padding: 10px;
    width: 100%;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

const betAmountInput = document.getElementById('bet-amount');
const betTypeSelect = document.getElementById('bet-type');
const betNumberInput = document.getElementById('bet-number');
const placeBetBtn = document.getElementById('place-bet-btn');
const resultArea = document.getElementById('result-area');
const resultNumberText = document.getElementById('result-number');
const resultMessageText = document.getElementById('result-message');

betTypeSelect.addEventListener('change', () => {
    if (betTypeSelect.value === 'number') {
        betNumberInput.style.display = 'block';
    } else {
        betNumberInput.style.display = 'none';
    }
});

placeBetBtn.addEventListener('click', () => {
    const betAmount = parseInt(betAmountInput.value);
    const betType = betTypeSelect.value;
    const betNumber = parseInt(betNumberInput.value);
    
    if (isNaN(betAmount) || betAmount <= 0) {
        alert('Please enter a valid bet amount.');
        return;
    }

    const winningNumber = Math.floor(Math.random() * 37); // Random number between 0-36
    const winningColor = getColor(winningNumber);
    
    resultNumberText.textContent = `Winning Number: ${winningNumber} (${winningColor})`;
    
    let message = 'You lost!';
    if (betType === 'number' && betNumber === winningNumber) {
        message = `You win! You get ${betAmount * 35} chips!`;
    } else if (betType === 'red' && winningColor === 'red') {
        message = `You win! You get ${betAmount * 2} chips!`;
    } else if (betType === 'black' && winningColor === 'black') {
        message = `You win! You get ${betAmount * 2} chips!`;
    }
    
    resultMessageText.textContent = message;
    resultArea.style.display = 'block';
});

function getColor(number) {
    if (number === 0) return 'green';
    const redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
    return redNumbers.includes(number) ? 'red' : 'black';
}
