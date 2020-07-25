
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  # front-end urls
    path('admin/', admin.site.urls),
		path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout,name="log"),

  # backend urls
    path('publishJob/',views.publishJob,name="publishJob"),
    path('jobList/',views.jobList,name="jobList"),
		path('profile/', views.ownprofile, name='ownprofile'),
    path('profile/<name>', views.publicprofile, name='publicprofile'),
    path('update/', views.updateprofile, name='update'),
		path('job/<name>', views.job, name='job'),
    path('apply/<name>', views.apply, name='apply'),
    #path('delete/<name>', views.delete, name='delete'),
    path('contact/', views.contact, name='contact'),
]