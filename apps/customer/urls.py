from django.urls import path

from apps.customer import views

urlpatterns = [
    path('create/', views.create_client, name='create_client'),
]
