from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from abc import ABC, abstractmethod

class Page:

    @staticmethod
    def view(request, name, company):
        return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1> Добро пожаловать! </h1>
                <p> Меня зовут <b>{name}</b> и это моя первая страница на django! </p>
                <p> Я python-разработчик компании <b>{company}</b></p>
            </body>
        </html>
        """)
    
    @staticmethod
    def view_by_get(request):
        # http://127.0.0.1:8000/index/?name=John&company=Apple
        name = request.GET.get("name", "Undefind")
        company = request.GET.get("company", "Undefind")

        return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1> Добро пожаловать! </h1>
                <p> Меня зовут <b>{name}</b> и это моя первая страница на django! </p>
                <p> Я python-разработчик компании <b>{company}</b></p>
            </body>
        </html>
        """)
    

class TemplateWebSite(ABC):

    @abstractmethod
    def main(request):
        return HttpResponseNotFound(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1> 404 ERROR: PAGE NOT FOUND </h1>
            </body>
        </html>
        """)
    
    @abstractmethod
    def news(request):
        return HttpResponseNotFound("Not Found")

    @abstractmethod
    def about(request):
        return HttpResponseNotFound("Not Found")

    @abstractmethod
    def managers(request):
        return HttpResponseNotFound("Not Found")
    

class NewCompany(TemplateWebSite):

    def main(request):
        return render(request, 'main.html', {
            "name": "Google",
        })

    def news(request):
        
        return render(request, 'news.html', {
            "news_list": ["Новость 1", "Новость 2", "Новость 3"]
        })

    def about(request):
        return render(request, 'about.html')

    def managers(request, page):
        if not page:
            return render(request, f'managers/managers.html')

        return render(request, f'managers/{page}.html')
