from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html')),
    path('signup/', views.SignUp.as_view(), name='signup')
]
