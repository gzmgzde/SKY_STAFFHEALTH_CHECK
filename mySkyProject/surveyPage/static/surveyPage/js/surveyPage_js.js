// Function to update the progress bar
function updateProgressBar(currentQuestion) {
  console.log("Updating progress bar for question:", currentQuestion);

  // Loop through all questions BEFORE the current question and mark them as completed
  for (let i = 1; i < currentQuestion; i++) {
    console.log(`Processing question ${i}`);

    // Mark the circle for the previous questions as completed
    const circle = document.querySelector(`#q${i} .circle`);
    if (circle) {
      circle.classList.add("completed");
      console.log(`Marked circle for question ${i} as completed`);
    } else {
      console.error(`Circle for question ${i} not found`);
    }

    // Mark the forward micro-circles as completed
    const micro1 = document.querySelector(`#q${i}-micro-1`);
    const micro2 = document.querySelector(`#q${i}-micro-2`);
    if (micro1) {
      micro1.classList.add("completed");
      console.log(`Marked micro-circle 1 for question ${i} as completed`);
    } else {
      console.warn(`Micro-circle 1 for question ${i} not found`);
    }
    if (micro2) {
      micro2.classList.add("completed");
      console.log(`Marked micro-circle 2 for question ${i} as completed`);
    } else {
      console.warn(`Micro-circle 2 for question ${i} not found`);
    }
  }
}

// Get the current question number from the data attribute
const progressData = document.getElementById("progress-data");
if (progressData) {
  const currentQuestion = parseInt(progressData.dataset.currentQuestion);
  updateProgressBar(currentQuestion);
} else {
  console.error(
    "Progress data not found. Ensure the 'progress-data' div is present in the HTML."
  );
}

// Function to handle voting
function setupVoting() {
  const scalePoints = document.querySelectorAll(".scale-point");
  const scaleSlider = document.getElementById("scaleSlider");

  // Function to update the selected point
  function updateSelectedPoint(value) {
    // Remove 'selected' class from all points
    scalePoints.forEach((point) => point.classList.remove("selected"));

    // Add 'selected' class to the corresponding point
    const selectedPoint = document.querySelector(
      `.scale-point[data-value="${value}"]`
    );
    if (selectedPoint) {
      selectedPoint.classList.add("selected");
    }

    console.log(`Selected Value: ${value}`); // Log the selected value
  }

  // Add click event listeners to scale points
  scalePoints.forEach((point) => {
    point.addEventListener("click", () => {
      const value = point.dataset.value;

      // Update the slider position
      scaleSlider.value = value;

      // Update the selected point
      updateSelectedPoint(value);
    });
  });

  // Add input event listener to the slider
  scaleSlider.addEventListener("input", () => {
    const value = scaleSlider.value;

    // Update the selected point
    updateSelectedPoint(value);
  });

  // Initialize the default selected point
  updateSelectedPoint(scaleSlider.value);
}

// Initialize the voting functionality
setupVoting();

//Additional comment field
document.addEventListener("DOMContentLoaded", () => {
  const commentForm = document.getElementById("surveyForm");
  const commentInput = document.getElementById("commentInput");
  const commentsList = document.getElementById("commentsList");

  // Function to add a comment
  function addComment(text) {
    const commentItem = document.createElement("li");
    commentItem.classList.add("comment-item");

    const commentText = document.createElement("span");
    commentText.classList.add("comment-text");
    commentText.textContent = text;

    const buttonsContainer = document.createElement("div");
    buttonsContainer.classList.add("comment-buttons");

    // Edit button
    const editButton = document.createElement("button");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", () =>
      editComment(commentItem, commentText)
    );

    // Remove button
    const removeButton = document.createElement("button");
    removeButton.textContent = "Remove";
    removeButton.classList.add("remove-btn");
    removeButton.addEventListener("click", () => removeComment(commentItem));

    buttonsContainer.appendChild(editButton);
    buttonsContainer.appendChild(removeButton);

    commentItem.appendChild(commentText);
    commentItem.appendChild(buttonsContainer);

    commentsList.appendChild(commentItem);
  }

  // Function to edit a comment
  function editComment(commentItem, commentText) {
    const newText = prompt("Edit your comment:", commentText.textContent);
    if (newText !== null && newText.trim() !== "") {
      commentText.textContent = newText.trim();
    }
  }

  // Function to remove a comment
  function removeComment(commentItem) {
    commentsList.removeChild(commentItem);
  }

  // Handle form submission
  commentForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const commentText = commentInput.value.trim();
    if (commentText !== "") {
      addComment(commentText);
      commentInput.value = ""; // Clear the input field
    }
  });
});
