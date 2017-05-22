$(function() {
    $("#login-form").validate({
        rules: {
            nick: "required",
            password: {
                required: true,
                minlength: 6
            }
        },
        messages: {
            nick: "Podaj swój login",
            password: {
                required: "Podaj hasło",
                minlength: "Hasło musi mieć co najmniej 6 znaków"
            }
        }
    });
});
