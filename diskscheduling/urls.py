from django.urls import path
from diskscheduling import views


urlpatterns = [
    path('', views.home, name='home'),
    path('fifo/', views.fifo, name='fifo'),
    path('sstf/', views.sstf, name='sstf'),
    path('scan/', views.scan, name='scan'),
    path('c-scan/', views.cscan, name='cscan'),
    path('look/', views.look, name='look'),
    path('c-look/', views.clook, name='clook'),

# <str:job_count>/<str:previously_served>/<str:starting_position>/<str:starting_track>/<str:ending_track>/
]