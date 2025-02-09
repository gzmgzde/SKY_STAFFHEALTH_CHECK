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
    event.preventDefault();

    const commentInput = document.getElementById("commentInput");
    const commentText = commentInput.value.trim();

    if (commentText !== "") {
      displayComment(commentText);
      commentInput.value = "";
    }
  });

// Function to display submitted comments with edit & remove buttons
function displayComment(comment) {
  const commentList = document.getElementById("commentsList");

  const newComment = document.createElement("li");

  const commentText = document.createElement("span");
  commentText.textContent = comment;
  commentText.classList.add("comment-text");

  // Create action container
  const actionContainer = document.createElement("div");
  actionContainer.classList.add("comment-actions");

  // Create edit button
  const editBtn = document.createElement("button");
  editBtn.textContent = "Edit";
  editBtn.classList.add("edit-btn");
  editBtn.onclick = function () {
    const newText = prompt("Edit your comment:", commentText.textContent);
    if (newText !== null && newText.trim() !== "") {
      commentText.textContent = newText.trim();
    }
  };

  // Create remove button
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "Remove";
  removeBtn.classList.add("remove-btn");
  removeBtn.onclick = function () {
    commentList.removeChild(newComment);
  };

  newComment.appendChild(commentText);
  actionContainer.appendChild(editBtn);
  actionContainer.appendChild(removeBtn);
  newComment.appendChild(actionContainer);
  commentList.appendChild(newComment);
}
