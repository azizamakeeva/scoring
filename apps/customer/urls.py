from django.urls import path

from apps.customer import views

urlpatterns = [
    # path('create/', views., name='myurl'),
    path('all/', views.ClientViewList.as_view(), name='client_list'),
    path('create/', views.AddClient.as_view(), name='create_client'),
    path('<int:pk>/update/', views.UpdateClient.as_view(), name='update_client'),
    path('<int:pk>/delete/', views.deleteClient, name='delete_client'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    # path('client/<int:pk>/delete/', views.DeleteClient.as_view(), name='delete_client'),
]
