from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import FileView
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_user', views.index2),
    url(r'^add_user', views.addUser),
    url(r'^save_user', views.saveUser),
    url(r'^view_users', views.viewUsers),
    url(r'^success$', views.success),
    url(r'^success2$', views.success2),
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.delete, name='destroy'), 



    path('edit2/<int:id>', views.edit2, name='edit2'),  
    path('update2/<int:id>', views.update2, name='update2'),  
    #path('delete2/<int:id>', views.destroy, name='destroy'), 
    url(r'^add_citizen', views.addCitizen),
    url(r'^save_citizen', views.saveCitizen),
    url(r'^view_citizens', views.viewcars),

    path('wanted_citizen/<int:citizen_id>/',views.wantedCitizen,name='wanted_citizen'),
    path('free_citizen/<int:citizen_id>/',views.freeCitizen,name='free_citizen'),


    url(r'^login$', views.login),
    url(r'^login_admin$', views.login_user),
    url(r'^logout', views.logout_view),
    url(r'^detectImage', views.detectImage),
    url(r'^detectWithWebcam', views.detectWithWebcam),
    url(r'^upload', FileView.as_view(), name='file-upload'),

    url(r'^spotted_criminals', views.spottedCriminals),
    url(r'^spotted_criminals2', views.spottedCriminals2),
    path('thief_location/<int:thief_id>/',views.viewThiefLocation,name='thief_location'),
    path('found_thief/<int:thief_id>/', views.foundThief, name='found_thief'),
        path('found_thief2/<int:thief_id>/', views.foundThief2, name='found_thief'),


    url(r'^reports', views.viewReports),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
