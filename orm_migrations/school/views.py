from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {
        'object_list': Student.objects.order_by('group').all().prefetch_related('teacher')
    }
    return render(request, template, context)
