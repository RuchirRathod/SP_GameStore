from django.urls import path, include

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('games', views.get_games, name='games'),
    path('html', views.get_html, name='html'),
    #path('create', views.create, name='create'),
    #path("loguser", views.login_user, name="loguser"),
    #path('login', views.login_view, name='login'),
    #path('logout', views.logout_view, name='logout'),
    #path('signup', views.signup, name='signup'),

]
