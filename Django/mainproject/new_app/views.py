from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from abc import ABC, abstractmethod
import time

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
            Article("Новость 2", "Иванов И.И.", "Описание 2"),
            Article("Новость 3", "Иванов И.И.", "Описание 3"),
            Article("Новость 4", "Иванов И.И.", "Описание 4"),
            Article("Новость 5", "Иванов И.И.", "Описание 5"),
            Article("Новость 6", "Иванов И.И.", "Описание 6"),
            Article("Новость 7", "Иванов И.И.", "Описание 7")
        ]

        return render(request, 'news.html', {
            "news_list": context[:5]
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
            return HttpResponseRedirect('/main')
        else:
            return render(request, 'authorization.html', {
                "error": "Неврерный логин или пароль"
            })

    def subscribe(request):
        user_email = request.POST.get("useremail")

        # Записать в БД email, с условием что его еще там нет

        time.sleep(1)
        return render(request, 'main.html', {
                "subscribe": """ <div class="alert alert-success d-flex alert-dismissible fade show" role="alert">
                                     <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
                                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                                    </svg>
                                    <strong> Подписка на новости успешно оформлена </strong>
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                 </div>
                             """
            })


        
