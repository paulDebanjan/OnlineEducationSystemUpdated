from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import handler500, handler400
from django.conf import settings
from django.views.static import serve

from django.contrib.auth import views as auth_view

from OnlineTrainingPortal import userAuthentication
# Root App Urls
from OnlineTrainingPortal.views import home,about,gideLine
# from OnlineTrainingPortal.views import enquiry
from OnlineTrainingPortal.views import thank

from django.conf.urls.static import static
# Authentication 
from OnlineTrainingPortal.userAuthentication import views as user_auth_views

#VideoCall App
from OnlineTrainingPortal.videoCall.views import videoCall 
# AdminSite App


# Error Handler
from OnlineTrainingPortal.userAuthentication.views.classroom import Error500View as error500
from OnlineTrainingPortal.userAuthentication.views.classroom import Error400View as error400



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about, name='about'),
    path('thank/',thank, name='thank'),
    path('gideLine/',gideLine, name='gideLine'),
    
    # Course app Urls
    path('course/',include('OnlineTrainingPortal.course.urls')),
    path('quiz/',include('OnlineTrainingPortal.quizes.urls')),

    # Blog App Urls
    path('blog/',include('OnlineTrainingPortal.blog.urls')),
    # path('blog/',blog,name='blog'),
    # path('blog/<slug>',blogDetail),
    
    # Authentication App
    path('accounts/',include('OnlineTrainingPortal.userAuthentication.urls')),
    
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='userAuthentication/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='userAuthentication/password_reset_complete.html'),name='password_reset_complete'),
    

    #teacher
    path('teacher/',include('OnlineTrainingPortal.teacher.urls')),
    #adminSite
    path('administration/',include('OnlineTrainingPortal.administration.urls')),

    #Message URL
    path('message/',include('OnlineTrainingPortal.message.urls')),

    # VideoCall App urls
    path('videoCall/',videoCall,name='videoCall'),

    # Enquiry App
    path('enquiry/',include('OnlineTrainingPortal.enquiry.urls')),

    #Debug Fase Mode
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
handler500 = error500.as_view()
handler400 = error400.as_view()
# For Media
if settings.DEBUG:
        urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)