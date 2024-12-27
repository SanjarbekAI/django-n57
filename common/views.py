from django.shortcuts import render


def home_page_view(request):
    return render(request, 'index.html')

def about_page_view(request):
    return render(request, 'pages/about.html')

def author_page_view(request):
    return render(request, 'pages/author.html')