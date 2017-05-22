from django.shortcuts import render

# Create your views here.

def main_page(request):
	return render(request, 'main.html')

def tickle(request):
	return render(request, 'tickle.html')

def funny_movies(request):
	return render(request, 'funny_movies.html')

def funny_pictures(request):
	return render(request, 'funny_pictures.html')

def jokes(request):
	return render(request, 'jokes.html')

def bubblewrap(request):
	return render(request, 'bubblewrap.html')