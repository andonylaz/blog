from django.shortcuts import render

# Create your views here.

def index(request):
	"""
    displays the homepage
	"""
	return render(request, 'index.html')


def blog_detail(request, pk):

	return render(request, 'index.html')