from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_register'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_course_enroll'),
    path('courses/', views.StudentCourseList.as_view(), name='student_course_list'),
    path('course/<pk>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),

]