from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import UsersView

app_name = 'users'

urlpatterns = [
    url('users/register/', UsersView.as_view()),
    url("admin/login/", obtain_auth_token, name='login')
]
