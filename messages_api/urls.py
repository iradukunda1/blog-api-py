from django.urls import path
from . import views

app_name = 'messages_api'

urlpatterns = [
    path('messages/', views.MessageListView.as_view()),
    path('messages/<int:pk>', views.MessageDetails.as_view())
]
