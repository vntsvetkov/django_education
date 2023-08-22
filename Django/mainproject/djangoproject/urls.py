
from django.contrib import admin
from django.urls import path, include, re_path
from new_app.views import NewCompany

managers_patterns = [
    path('', NewCompany.managers, kwargs={"page": ""}, name="managers"),
    path('director/', NewCompany.managers, kwargs={"page": "director"}, name="director"),
    path('dev_manager/', NewCompany.managers, kwargs={"page": "dev_manager"}, name="dev_manager"),
    re_path(r'\w+', NewCompany.managers, kwargs={"page": ""}, name="managers"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', NewCompany.main, name="main"),
    path('news/', NewCompany.news, name="news"),
    path('about/', NewCompany.about, name="about"),
    path('managers/', include(managers_patterns)),
]
