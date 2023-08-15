
from django.contrib import admin
from django.urls import path, include
from new_app.views import Page, NewCompany

managers_patterns = [
    path('', NewCompany.managers),
    path('director/', NewCompany.managers, kwargs={"page": "director"}),
    path('dev_manager/', NewCompany.managers, kwargs={"page": "dev_manager"}),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', 
        Page.view, 
        kwargs={"name": "Николай", "company": "Google"}),
    path('index/', Page.view_by_get),
    path('main/', NewCompany.main),
    path('news/', NewCompany.news),
    path('managers/', include(managers_patterns)),
]
