from django.shortcuts import render

def serve_home_page(request):
    return render(request, 'index.html')
