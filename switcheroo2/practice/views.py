from django.http import HttpResponse
from django.template import loader

def practice(request):
  template = loader.get_template('myhtml.html')
  return HttpResponse(template.render())