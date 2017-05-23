$(function() {
    $("#settings-account-form").validate({
        rules: {
            old_password: {
                required: "#new_password:filled"
            },
            new_password: {
                required: "#old_password:filled",
                minlength: 6
            },
            password_new2: {
                required: "#new_password:filled",
                minlength: 6,
                equalTo: "#new_password"
            }
        },
        messages: {
            old_password: {
                required: "Podaj hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków"
            },
            new_password: {
                required: "Podaj nowe hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków"
            },
            password_new2: {
                required: "Powtórz nowe hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków",
                equalTo: "Hasła muszą się zgadzać."
            }
        }
    });
});
