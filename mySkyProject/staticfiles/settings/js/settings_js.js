// Password Change Form Handling
document.addEventListener('DOMContentLoaded', function() {
    const passwordForm = document.getElementById('passwordChangeForm');
    if (passwordForm) {
        passwordForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            fetch("/settings/change-password/", {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                const messageDiv = document.getElementById('passwordMessage');
                if (data.status === 'success') {
                    messageDiv.className = 'alert alert-success mt-2';
                    messageDiv.textContent = data.message;
                    this.reset();
                } else {
                    messageDiv.className = 'alert alert-danger mt-2';
                    messageDiv.textContent = data.message;
                }
            })
            .catch(error => {
                const messageDiv = document.getElementById('passwordMessage');
                messageDiv.className = 'alert alert-danger mt-2';
                messageDiv.textContent = 'An error occurred. Please try again.';
            });
        });
    }
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
