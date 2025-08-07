// SweetAlert2 basic usage demo
// This file is a placeholder for SweetAlert2 integration in Django static files

// Example: Show a success alert
function showSuccessAlert(message) {
    Swal.fire({
        icon: 'success',
        title: 'Success',
        text: message,
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'OK'
    });
}

// Example: Show an error alert
function showErrorAlert(message) {
    Swal.fire({
        icon: 'error',
        title: 'Error',
        text: message,
        confirmButtonColor: '#d33',
        confirmButtonText: 'OK'
    });
}

// Example: Confirm dialog
function showConfirmDialog(message, callback) {
    Swal.fire({
        icon: 'warning',
        title: 'Are you sure?',
        text: message,
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            callback();
        }
    });
}

// Make sure SweetAlert2 is loaded via CDN in your base template:
// <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
// <script src="{% static 'js/sweetalert.js' %}"></script>
