from django.shortcuts import render

# Create your views here.

def homepage(request):
	return render(request, 'home.html')

def convert_length(request):
	meter1 = request.GET['meter']
	c = meter1 * 2
	return render(request, 'convert_length.html',{'centimeter':float(c) })

