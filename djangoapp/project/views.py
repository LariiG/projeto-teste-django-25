from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Página inicial
def home(request):
    return render(request, 'home.html')

@login_required
def admin_page(request):
    return render(request, 'admin_page.html')
