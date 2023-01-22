from django.urls import path, include
from .views import MessageAPIList, MessageAPIUpdate, MessageAPIDestroy, MessageAPIView
from. import views

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('send_message/', MessageAPIList.as_view()),
    path('get_message/<int:pk>/', MessageAPIUpdate.as_view()),
    path('delete_message/', MessageAPIDestroy.as_view()),
    path('message/', MessageAPIView.as_view()),
    path('generate_token/', views.generate_token, name='generate_token'),
]