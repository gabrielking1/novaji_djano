from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('verification/', include('verify_email.urls')),
    # path('email',views.email, name = 'email'),
    # path('change_password', views.change_password, name='change_password'),
    # path("password_reset", views.password_reset_request, name="password_reset"),
    #     #path('accounts/', include('django.contrib.auth.urls')),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='persons/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="persons/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='persons/password_reset_complete.html'), name='password_reset_complete'),
    


    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]



urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)