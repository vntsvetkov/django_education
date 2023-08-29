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
    

class Article:

    def __init__(self, title, author, desc) -> None:
        self.title = title
        self.author = author
        self.desc = desc

class NewCompany(TemplateWebSite):

    # http://127.0.0.1:8000/main/?name=Google
    def main(request):

        return render(request, 'main.html')

    # http://127.0.0.1:8000/news
    def news(request):
        
        context = [
            Article("Новость 1", "Иванов И.И.", "Описание 1"),
            Article("Новость 2", "Иванов И.И.", "Описание 2")
        ]

        return render(request, 'news.html', {
            "news_list": context
        })

    # http://127.0.0.1:8000/about
    def about(request):
        return render(request, 'about.html')

    # http://127.0.0.1:8000/managers/
    # http://127.0.0.1:8000/managers/director
    # http://127.0.0.1:8000/managers/dev_manager
    def managers(request, page):
        if not page:
            return render(request, f'managers/managers.html')

        return render(request, f'managers/{page}.html')
    
    def dynamic_path(request, page):
        # Надо как то знать о страницах 
        if not page:
            return render(request, f'managers/managers.html')

        return render(request, f'managers/{page}.html')


class FormManage:

    def authorization(request):
        return render(request, 'authorization.html')

    def check_authorization(request):
        name = request.POST.get("login")
        password = request.POST.get("password")
        
        users = [
            {"логин": "user1", "пароль": "password1"},
            {"логин": "user2", "пароль": "password2"},
        ]

        a = [True for record in users if record['логин'] == name and record['пароль'] == password]


        if len(a) > 0: 
            return render(request, 'main.html')
        else:
            return render(request, 'authorization.html', {
                "error": "Неврерный логин или пароль"
            })
