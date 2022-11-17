from django.contrib import admin
from django.urls import path,re_path,include
from second_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    re_path(r'^users/',include('second_app.urls'))
]
