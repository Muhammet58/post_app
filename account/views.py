from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "account/login.html",
                {"error": "Kullanıcı adınızı yada parola bilginizi yanlış girdiniz !"},
            )

    return render(
        request,
        "account/login.html",
    )


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["repassword"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(
                    request,
                    "account/register.html",
                    {
                        "error": "Bu kullanıcı adı başkası tarafından kullanılıyor lütfen başka oluşturunuz !",
                        "username": username,
                        "name": name,
                        "surname": surname,
                        "email": email,
                    },
                )
            else:
                if User.objects.filter(email=email).exists():
                    return render(
                        request,
                        "account/register.html",
                        {
                            "error": "Bu email zaten kayıtlı lütfen başka giriniz !",
                            "username": username,
                            "name": name,
                            "surname": surname,
                            "email": email,
                        },
                    )
                else:
                    user = User.objects.create_user(
                        username=username,
                        first_name=name,
                        last_name=surname,
                        password=password1,
                    )
                    user.save()
                    return redirect("login_url")
        else:
            return render(
                request,
                "account/register.html",
                {
                    "error": "Şifreler birbiri ile uyuşmuyor !",
                    "username": username,
                    "name": name,
                    "surname": surname,
                    "email": email,
                },
            )

    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("home")
