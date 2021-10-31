from django.shortcuts import render

# Create your views here.
def loginuser(request):
	return render(request, 'user/login.html')

def book(request):
	return render(request, 'user/book.html')

def home(request):
	return render(request, 'user/home.html')