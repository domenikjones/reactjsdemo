from django.shortcuts import render
from demo.logger.demo_logger import *

# Create your views here.
def index(request):

    ctx = {}
    template = 'layouts/default.html'

    return render(request,
                  template,
                  ctx,
    )