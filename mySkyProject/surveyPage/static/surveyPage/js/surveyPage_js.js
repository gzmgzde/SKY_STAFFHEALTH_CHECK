// Function to update the progress bar
function updateProgressBar(currentQuestion) {
  console.log("Updating progress bar for question:", currentQuestion);

  // Loop through all questions BEFORE the current question and mark them as green
  for (let i = 1; i < currentQuestion; i++) {
    console.log(`Processing question ${i}`);

    // Mark the circle for the previous questions as green
    const circle = document.querySelector(`#q${i} .circle`);
    if (circle) {
      circle.style.backgroundColor = "green";
      console.log(`Marked circle for question ${i} as green`);
    } else {
      console.error(`Circle for question ${i} not found`);
    }

    // Mark the forward micro-circles as green
    const micro1 = document.querySelector(`#q${i}-micro-1`);
    const micro2 = document.querySelector(`#q${i}-micro-2`);
    if (micro1) {
      (micro1.style.backgroundColor = "green"), "important";
      console.log(`Marked micro-circle 1 for question ${i} as green`);
    } else {
      console.warn(`Micro-circle 1 for question ${i} not found`);
    }
    if (micro2) {
      (micro2.style.backgroundColor = "green"), "important";
      console.log(`Marked micro-circle 2 for question ${i} as green`);
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
