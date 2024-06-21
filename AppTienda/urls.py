from django.urls import path
from .views import index, crear_juego, buscar_juego, registro_usuario, about_me, logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('crear_juego/', crear_juego, name='crear_juego'),
    path('buscar_juego/', buscar_juego, name='buscar_juego'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
    path('about-me/', about_me, name='about_me'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
