#  hello/views.py

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/layout.html')

def poema_1_view(request):
	return render(request, 'website/poema_1.html')

def poema_2_view(request):
	return render(request, 'website/poema_2.html')

def poema_3_view(request):
	return render(request, 'website/poema_3.html')