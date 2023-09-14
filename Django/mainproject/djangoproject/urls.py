
from django.contrib import admin
from django.urls import path, include, re_path
from new_app.views import NewCompany, FormManage
import new_app.urls

# static
#   - css/
#       - main.css
#       - managers.css
#       - styles.css (общие стили для всех)
#   - images/
    # - icons/
    # - backgrounds/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', NewCompany.main, name="main"),
    path('news/', NewCompany.news, name="news"),
    path('about/', NewCompany.about, name="about"),
    path('managers/', include(new_app.urls)),
    path('authorization/', FormManage.authorization, name="authorization"),
    path('reauthorization/', FormManage.check_authorization, name="check_authorization"),
    path('subscribe/', FormManage.subscribe, name="subscribe"),
    path('create_article/', FormManage.create_article, name="create_article"),
    path('registartion/', FormManage.registration, name="registration"),
    re_path(r'^\w+', NewCompany.main),
]
