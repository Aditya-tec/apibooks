from django.urls import path
from .views import CustomTokenObtainPairView, BookDetail

from . import views

urlpatterns = [
    path('books/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/notfound/', views.BookNotFound.as_view(), name='book-notfound'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
