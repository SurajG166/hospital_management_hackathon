from django.shortcuts import render, redirect


def serve_home_page(request):
    return render(request, 'index.html')