from django.urls import path, include
from . import views
from gestion.views import students, teachers, tutors

urlpatterns = [

    path('',views.home, name='site-home'),
    path('contact/',views.contact, name='site-contact'),
    path('students/', include(([
    path('my/', students.StudentsEcuesView.as_view(), name='accueil-student'),
    path('ecues/<int:pk>/', students.StudentsCoursListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', students.StudentsCoursDetailView.as_view(), name='course-detail')

    
    ], 'classroom'), namespace='students')),

]
