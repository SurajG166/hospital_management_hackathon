from django.shortcuts import render

def serve_home_page(request):
    return render(request, 'home.html')

def serve_login_page(request):
    return render(request, 'login.html')