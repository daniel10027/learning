from django.urls import path, include
from . import views
from gestion.views import students, teachers, tutors

urlpatterns = [

    path('',views.home, name='site-home'),
    path('contact/',views.contact, name='site-contact'),


    path('students/', include(([
    path('my/', students.StudentsEcuesView.as_view(), name='accueil-student'),
    path('ecues/<int:pk>/', students.StudentsCoursListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', students.StudentsCoursDetailView.as_view(), name='course-detail'),
    path('myprofile/', students.profile, name='student-profile'),
], 'classroom'), namespace='students')),


 path('teacher/', include(([
    path('my/', teachers.home, name='accueil-teacher'),
    path('dossier/<int:pk>/', teachers.DossierListView.as_view(), name='jury-dossier'),
    path('dossier_mark/<int:pk>/', teachers.ResulatCreateView.as_view(), name='resultat'),
    path('dossier_detail/<int:pk>/', teachers.DossierDetailView.as_view(), name='dossier-detail'), 
    path('global/', teachers.RecrutementListView.as_view(), name='recru-list'), 
    path('resultats/<int:pk>/', teachers.ResultatFinal.as_view(), name='resultat-final'),
    path('myprofile/', teachers.profile, name='teacher-profile'),
    path('statistiques/', teachers.Stat.as_view(), name='site-stat'),
     
], 'classroom'), namespace='teachers')),


 path('tutors/', include(([
    path('my/', tutors.home, name='accueil-tutor'),
    path('myprofile/', tutors.TutorProfilet, name='tutor-profile'),
], 'classroom'), namespace='tutors')),


]
