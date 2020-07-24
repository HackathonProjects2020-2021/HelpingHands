
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
    # path('dashboard/', views.dashboard, name='dashboard'),
		path('profile/<name>', views.profile, name='profile'),
		path('job/<name>', views.job, name='job'),
    # path('contact/', views.contact_form, name='contact'),

]