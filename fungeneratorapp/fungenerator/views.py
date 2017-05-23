from django.shortcuts import render
from .forms import SettingsForm
from .models import UserSettings

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

def settings(request):
	current_user = request.user
	if request.method=='POST':
		form = SettingsForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			settings_object = UserSettings.objects.get(user=current_user)
			settings_object.animals = data['animals']
			settings_object.kids = data['kids']
			settings_object.fails = data['fails']
			settings_object.stereotypes = data['stereotypes']
			settings_object.language = data['language']
			settings_object.absurd = data['absurd']
			settings_object.save()

	try:
		settings_object = UserSettings.objects.get(user=current_user)
	except UserSettings.DoesNotExist:
		settings_object = UserSettings.objects.create(user = current_user, animals=False, kids=False, fails=False, stereotypes=False, language=False, absurd=False)


	return render(request, 'settings.html', {'settings': settings_object })
