from .models import Response
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ResponseForm


def review(request):
	if request.method == 'POST':
		form = ResponseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('portfolio')
	return render(request,'review.html',{'form': form})
def home(request):
  template = loader.get_template('landimg.html')
  return HttpResponse(template.render())

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


