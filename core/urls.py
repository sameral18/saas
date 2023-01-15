
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
path('',login_page,name='login'),

path('signup/',SignupView.as_view(),name='signup'),
path('logout/',logout_user,name='logout'),
path('add-course/',add_courseView.as_view(),name='add-course'),
path('all-courses/',all_coursesView.as_view(),name='all-courses'),

path('add-worker/',add_workerView.as_view(),name='add-worker'),
path('all-workers/',all_workersView.as_view(),name='all-workers'),

path('add-student/',add_studentView.as_view(),name='add-student'),
path('all-students/',all_studentsView.as_view(),name='all-students'),


path('profile/',profile,name='profile'),
path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),

]
