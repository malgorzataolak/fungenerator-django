$( document ).ready(function(){
$(".helptext").html("Nick powinien zawierać jedynie liczby lub cyfry.");
$("label[for='id_username']").html("Nick");
$("label[for='id_first_name']").html("Imię");
$("label[for='id_email']").html("E-mail");


});


$(function() {
    $("#register-form").validate({
        rules: {
            username: {required: true, minlength: 3},
            first_name: {required: true, minlength: 1},
            password: {
                required: true,
                minlength: 6,
            },
            password: {
                required: true,
                minlength: 6,
            },
            password2: {
                required: true,
                minlength: 6,
                equalTo: "#id_password"
            }
        },
        messages: {
            username: "Podaj swój login (co najmniej trzy znaki)",
            first_name: "Podaj swoje imię",
            email: "Proszę podać prawidłowy adres email",
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
