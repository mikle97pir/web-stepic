from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_questions, name='root'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>/', views.question_details, name='question-id'),
    path('ask/', views.question_add, name='ask'),
    path('popular/', views.popular_questions, name='popular'),
    path('new/', views.test, name='popular'),
]