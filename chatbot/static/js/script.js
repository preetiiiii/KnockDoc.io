document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get user input
    const userInput = document.getElementById('user-input').value;

    if (userInput.trim() === '') {
        return;
    }

    // Append user message to chat
    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input field
    document.getElementById('user-input').value = '';

    // Fetch response from the Python backend
    fetch('/get-response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        botMessage.textContent = data.response;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
