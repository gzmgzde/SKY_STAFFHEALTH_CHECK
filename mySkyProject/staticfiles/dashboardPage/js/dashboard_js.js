// Function to toggle the dropdown menu
function toggleDropdown() {
  const profileContainer = document.querySelector(".navbar-right");
  const dropdownMenu = document.querySelector(".dropdown-menu");

  // Add click event listener to the profile container
  profileContainer.addEventListener("click", () => {
    dropdownMenu.classList.toggle("active");
  });

  // Close the dropdown if clicked outside
  document.addEventListener("click", (event) => {
    if (!profileContainer.contains(event.target)) {
      dropdownMenu.classList.remove("active");
    }
  });
}

// Call the function to activate the dropdown functionality
toggleDropdown();
