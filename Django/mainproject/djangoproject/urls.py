
from django.contrib import admin
from django.urls import path, include, re_path
from new_app.views import NewCompany
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
    # path('managers/<str:page>', NewCompany.dynamic_path),
    path('managers/', include(new_app.urls)),
    re_path(r'^\w+', NewCompany.main),
]
