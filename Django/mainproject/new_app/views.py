from django.shortcuts import render
from django.http import HttpResponse

class Page:

    @staticmethod
    def view(request):
        return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1> Добро пожаловать! </h1>
                <p> Меня зовут Николай и это моя первая страница на django! </p>
            </body>
        </html>
        """)
    
    def view_html(request):
        return render(request, 'home.html')
