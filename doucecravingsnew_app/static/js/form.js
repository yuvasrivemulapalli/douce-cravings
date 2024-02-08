function togglePasswordVisibility() {
        var passwordInput = document.getElementById('passwordInput');
        var togglePassword = document.getElementById('togglePassword');

        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            togglePassword.textContent = 'Hide Password';
        } else {
            passwordInput.type = 'password';
            togglePassword.textContent = 'Show Password';
        }
    }