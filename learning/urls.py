from django.contrib import admin
from django.conf import settings
from django.contrib.auth  import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from schema_graph.views import Schema
from gestion.views import students, teachers, tutors
from django.contrib import admin


urlpatterns = [


    

    path('', include('enseignement.urls')),

    path('explorer/', include('explorer.urls'), name='explorer'),
 
    path('admin/', admin.site.urls, name='admin'),

    path('recrutement/', include('recrutement.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='account'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView .as_view(), name='teacher_signup'),
    path('accounts/signup/tutor/',     tutors.TutorSignUpView.as_view(), name='tutor_signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'enseignement/index.html'), name="logout"),
    path('password-reset/',
                         auth_views.PasswordResetView.as_view(template_name = 'gestion/password_reset.html'),
                         name="password_reset"),
    path('password-reset/done/',
                         auth_views.PasswordResetDoneView.as_view(template_name = 'gestion/password_reset_done.html'),
                         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
                         auth_views.PasswordResetConfirmView.as_view(template_name = 'gestion/password_reset_confirm.html'),
                         name="password_reset_confirm"),
    path('password-reset-complete/',
                         auth_views.PasswordResetCompleteView.as_view(template_name = 'gestion/password_reset_complete.html'),
                         name="password_reset_complete"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

      

    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)