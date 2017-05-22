$(function() {
    $("#settings-account-form").validate({
        rules: {
            password_old: {
                required: "#settings-account-password-new:filled"
            },
            password_new: {
                required: "#settings-account-password-old:filled",
                minlength: 6
            },
            password_new2: {
                required: "#settings-account-password-new:filled",
                minlength: 6,
                equalTo: "#settings-account-password-new"
            }
        },
        messages: {
            password_old: {
                required: "Podaj hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków"
            },
            password_new: {
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
