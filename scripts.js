// Login form submission handling
document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get the username and password from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Set the correct login credentials
    const correctUsername = 'Myworld';  // Username
    const correctPassword = 'youndme'; // Password

    // Check if the entered credentials match
    if (username === correctUsername && password === correctPassword) {
        // If credentials match, redirect to the welcome page
        window.location.href = 'welcome.html';
    } else {
        // If credentials are incorrect, show an error alert
        alert('Invalid username or password. Please try again.');
    }
});


