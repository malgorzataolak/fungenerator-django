$(function() {
    $("#register-form").validate({
        rules: {
            nick: "required",
            password: {
                required: true,
                minlength: 6
            },
            password2: {
                required: true,
                minlength: 6,
                equalTo: "#register-password"
            }
        },
        messages: {
            nick: "Podaj swój login",
            password: {
                required: "Podaj hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków"
            },
            password2: {
                required: "Powtórz hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków",
                equalTo: "Hasła muszą się zgadzać."
            }
        }
    });
});
