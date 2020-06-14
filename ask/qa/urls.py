from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_questions, name='root'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>', views.test, name='question-id'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='popular'),
]