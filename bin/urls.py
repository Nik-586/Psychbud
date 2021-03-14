from django.contrib import admin
from django.urls import path,include
from Psychbudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base_view,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.form_view, name='register'),

    path('accounts',include('django.contrib.auth.urls')),
]
