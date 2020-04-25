from django.urls import path, include
from . import views
from gestion.views import students, teachers, tutors

urlpatterns = [

    path('',views.home, name='site-home'),
    path('students/', include(([
    path('ecue/', students.StudentsEcuesView.as_view(), name='accueil-student'),
    ], 'classroom'), namespace='students')),

]
