from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api/feedback/', views.FeedbackListCreate.as_view(), name='feedback-list-create'),
    path('api/feedback/<int:pk>/', views.FeedbackDetail.as_view(), name='feedback-detail'),
    path('api/model-response/', views.ModelResponseListCreate.as_view(), name='model-response-list-create'),
    path('api/model-response/<int:pk>/', views.ModelResponseDetail.as_view(), name='model-response-detail'),
]