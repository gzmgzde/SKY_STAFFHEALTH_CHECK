//Questions progression bar
let currentQuestion = 0;
const totalQuestions = 14;

function updateProgressBar() {
  const progressBar = document.getElementById("progressBar");
  const progressPercentage = (currentQuestion / totalQuestions) * 100;
  progressBar.style.width = progressPercentage + "%";
  progressBar.textContent = `${progressPercentage.toFixed(0)}%`;
}

// Event listener for "Next Question" button
document
  .getElementById("nextQuestionBtn")
  .addEventListener("click", function () {
    if (currentQuestion < totalQuestions) {
      currentQuestion++;
      updateProgressBar();
    }
  });

// Event listener for comment form submission
document
  .getElementById("surveyForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent page reload

    const commentInput = document.getElementById("commentInput");
    const commentText = commentInput.value.trim();

    if (commentText !== "") {
      displayComment(commentText);
      commentInput.value = "";
    }
  });

//Additional Comments display
function displayComment(comment) {
  const commentList = document.getElementById("commentsList");
  const newComment = document.createElement("li");
  newComment.textContent = comment;
  commentList.appendChild(newComment);

  // Create remove button
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "Remove";
  removeBtn.classList.add("remove-btn");
  removeBtn.onclick = function () {
    commentList.removeChild(newComment);
  };

  newComment.appendChild(removeBtn);
  commentList.appendChild(newComment);
}
