import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    
    my_title = "My Page"
    qs = PageVisit.objects.all()
    page_visit_count = qs.count()
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_visit_count
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)


def about_view(request, *args, **kwargs):
    
    my_title = "My Page"
    qs = PageVisit.objects.all()
    page_visit_count = qs.count()
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_visit_count
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)