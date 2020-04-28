from django.urls import path, include
from . import views


urlpatterns = [
     path('',views.RecrutementListView.as_view(), name='recrutement-home'),
     path('detail/<int:pk>/', views.RecrutementDetailView.as_view(), name='recrutement-detail'),
     path('postuler/',views.DossierRecrutementCreateView.as_view(), name='postuler'),
     
]