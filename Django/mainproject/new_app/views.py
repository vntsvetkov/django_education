from django.shortcuts import render
from django.http import HttpResponse

class Page:

    @staticmethod
    def view(request):
        return HttpResponse(f"""
        <h1> Добро пожаловать! </h1><br> 
        <p> Это моя первая страница на django! </p>
        """)
    
    def view_html(request):
        return render(request, 'home.html')
