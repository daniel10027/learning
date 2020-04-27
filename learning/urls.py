from django.contrib import admin
from django.conf import settings
from django.contrib.auth  import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from gestion.views import students, teachers, tutors


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('enseignement.urls')),
    path('recrutement/', include('recrutement.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='account'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView .as_view(), name='teacher_signup'),
    path('accounts/signup/tutor/',     tutors.TutorSignUpView.as_view(), name='tutor_signup'),
    path('accounts/login/student/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name="login-student"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'enseignement/index.html'), name="logout"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)