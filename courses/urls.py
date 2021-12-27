from django.urls import path
from . import  views

urlpatterns = [
    path('mine/', views.CourseListView.as_view(), name='course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

]