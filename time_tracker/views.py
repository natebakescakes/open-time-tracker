from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Category, WorkLog
# Create your views here.


@login_required
def index(request):
    categories = WorkLog.objects.filter(member__)
    template = loader.get_template('time_tracker/index.html')
    context = {
        'categories': categories
    }
    return HttpResponse(template.render(context, request))


@login_required
def reports(request):
    template = loader.get_template('time_tracker/reports.html')
    context = {}
    return HttpResponse(template.render(context, request))
