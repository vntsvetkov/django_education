from django.urls import path, re_path
from new_app.views import NewCompany

urlpatterns = [
    path('', NewCompany.managers, kwargs={"page": ""}, name="managers"),
    path('director/', NewCompany.managers, kwargs={"page": "director"}, name="director"),
    path('dev_manager/', NewCompany.managers, kwargs={"page": "dev_manager"}, name="dev_manager"),
]