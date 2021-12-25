from django.contrib.contenttypes import fields
from django.core import files
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin
from django.views import generic
from . import models
from django.urls import reverse_lazy


class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin):
    model = models.Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url= reverse_lazy('course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'


class CourseListView(generic.ListView, OwnerCourseMixin): 
    template_name = 'courses/manage/course/list.html'


class CourseCreateView(OwnerCourseEditMixin, generic.CreateView):
    pass

class CourseUpdateView(OwnerCourseEditMixin, generic.UpdateView):
    pass

class CourseDeleteView(OwnerCourseMixin, generic.DeleteView):
    template_name = 'courses/manage/course/delete.html'