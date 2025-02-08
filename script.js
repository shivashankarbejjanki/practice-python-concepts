// Store the current question index and correct answers
let currentQuestionIndex = 0;
let correctAnswers = 0;

// List of questions and their correct answers
const questions = [
    {
        question: "What is 1 + 0?",
        answers: [1, 2, 3],
        correctAnswer: 1
    },
    {
        question: "What is 2 + 2?",
        answers: [1, 4, 5],
        correctAnswer: 4
    },
    {
        question: "What is 1 + 2?",
        answers: [1, 3, 4],
        correctAnswer: 3
    }
];

// Load the first question when the page loads
window.onload = function() {
    loadQuestion();
};

// Function to load the current question and answers
function loadQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    
    // Display the current question
    document.getElementById('question').innerText = currentQuestion.question;

    // Set the possible answers for the current question
    const buttons = document.querySelectorAll('.answer');
    buttons[0].textContent = currentQuestion.answers[0];
    buttons[1].textContent = currentQuestion.answers[1];
    buttons[2].textContent = currentQuestion.answers[2];

    // Attach click events to the buttons
    buttons[0].onclick = () => checkAnswer(currentQuestion.answers[0]);
    buttons[1].onclick = () => checkAnswer(currentQuestion.answers[1]);
    buttons[2].onclick = () => checkAnswer(currentQuestion.answers[2]);
}

// Function to check if the user's answer is correct
function checkAnswer(answer) {
    const currentQuestion = questions[currentQuestionIndex];

    // Check if the answer is correct
    if (answer === currentQuestion.correctAnswer) {
        correctAnswers++;
        document.getElementById("result").innerText = "Correct!";
    } else {
        document.getElementById("result").innerText = "Oops, try again!";
    }

    // Move to the next question or show the final message if all questions are answered correctly
    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            loadQuestion();
            document.getElementById("result").innerText = ""; // Clear the result message
        } else if (correctAnswers === questions.length) {
            displayLoveMessage();
        }
    }, 1000);  // Delay to simulate the transition to the next question
}

// Display the love proposal message if all questions are answered correctly
function displayLoveMessage() {
    document.getElementById("question-container").innerHTML = `
        <p>Everyone wants to be someone's sun to light up their life, but can I be your moon, to shine in your darkest time <br><strong>I LOVE YOU</strong></p>
    `;
}
