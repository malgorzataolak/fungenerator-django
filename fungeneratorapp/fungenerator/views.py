from django.shortcuts import render
from .forms import SettingsForm
from .forms import ChangePasswordForm
from .models import UserSettings
from django.http import HttpResponse

from .fun_content import images
from .fun_content import videos
from .fun_content import tickler

# Create your views here.

def main_page(request):
	return render(request, 'main.html')

def tickle(request):
	return render(request, 'tickle.html')

def tickle_start(request):
	if request.is_ajax():
		tickler.spin()
		return HttpResponse("ok")

def tickle_fast(request):
	if request.is_ajax():
		tickler.quick_rotation()
		return HttpResponse("ok")

def tickle_normal(request):
	if request.is_ajax():
		tickler.normal_rotation()
		return HttpResponse("ok")

def tickle_slow(request):
	if request.is_ajax():
		tickler.slow_rotation()
		return HttpResponse("ok")

def funny_movies(request):
	request_user = request.user
	if len(request_user.username) == 0:
		displayed_movies = { "animals" }
	else:
		displayed_movies = set()
		try:
			settings_object = UserSettings.objects.get(user=request_user)
		except UserSettings.DoesNotExist:
			settings_object = UserSettings.objects.create(user = current_user, animals=True, kids=False, fails=False, stereotypes=False, language=False, absurd=False)
		if settings_object.animals:
			displayed_movies.add("animals")
		if settings_object.kids:
			displayed_movies.add("kids")
		if settings_object.fails:
			displayed_movies.add("fails")
		if settings_object.stereotypes:
			displayed_movies.add("stereotypes")
		if settings_object.language:
			displayed_movies.add("language")
		if settings_object.absurd:
			displayed_movies.add("absurd")
	return render(request, 'funny_movies.html', { "movies" : displayed_movies })

def funny_pictures(request):
	request_user = request.user
	if len(request_user.username) == 0:
		displayed_images = images.animals
	else:
		displayed_images = set()
		try:
			settings_object = UserSettings.objects.get(user=request_user)
		except UserSettings.DoesNotExist:
			settings_object = UserSettings.objects.create(user = current_user, animals=True, kids=False, fails=False, stereotypes=False, language=False, absurd=False)
		if settings_object.animals:
			displayed_images = displayed_images | images.animals
		if settings_object.kids:
			displayed_images = displayed_images | images.kids
		if settings_object.fails:
			displayed_images = displayed_images | images.fails
		if settings_object.stereotypes:
			displayed_images = displayed_images | images.stereotypes
		if settings_object.language:
			displayed_images = displayed_images | images.language
		if settings_object.absurd:
			displayed_images = displayed_images | images.absurd
	return render(request, 'funny_pictures.html', { "images" : displayed_images })

def jokes(request):
	request_user = request.user
	if len(request_user.username) == 0:
		displayed_jokes = { "animals" }
	else:
		displayed_jokes = set()
		try:
			settings_object = UserSettings.objects.get(user=request_user)
		except UserSettings.DoesNotExist:
			settings_object = UserSettings.objects.create(user = current_user, animals=True, kids=False, fails=False, stereotypes=False, language=False, absurd=False)
		if settings_object.animals:
			displayed_jokes.add("animals")
		if settings_object.kids:
			displayed_jokes.add("kids")
		if settings_object.fails:
			displayed_jokes.add("fails")
		if settings_object.stereotypes:
			displayed_jokes.add("stereotypes")
		if settings_object.language:
			displayed_jokes.add("language")
		if settings_object.absurd:
			displayed_jokes.add("absurd")
	return render(request, 'jokes.html', { "jokes" : displayed_jokes })

def bubblewrap(request):
	return render(request, 'bubblewrap.html')

def change_password(request):
	current_user = request.user
	message = "Nie dokonano zmian w haśle"
	if request.method=='POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			if not current_user.check_password(data['old_password']):
				message = "Podano niepoprawne stare hasło. Hasło nie zostało zmienione"
			else:
				current_user.set_password(data['new_password'])
				current_user.save()
				message = "Pomyślnie zmieniono hasło"
	
	return render(request, 'change_password.html', {"message": message })


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
