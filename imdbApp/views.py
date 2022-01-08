from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Movie,Language,Status,Category

def moviesite(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()
    languages = Language.objects.all()
    status = Status.objects.all()
    return render(request, 'index.html', {"movies":movies,"categories":categories,'languages':languages,'status':status})

def search_results(request):
    title = 'Search'
    if 'title' in request.GET and request.GET['title']:
        search_term = request.GET.get('title')
        found_results = Movie.search_by_title(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'search_term':search_term,'movies': found_results, 'message': message})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})

def language_filter(request, movie_language):
    languages = Language.objects.all()
    language = Language.get_language_id(movie_language)
    movies = Movie.filter_by_language(movie_language)
    title = f'{language} Photos'
    return render(request, 'language.html', {'movies':movies, 'languages':languages, 'language':language})

def category_filter(request, movie_category):
    categories = Category.objects.all()
    category = Category.get_category_id(movie_category)
    movies = Movie.filter_by_category(movie_category)
    title = f'{category} Photos'
    return render(request, 'category.html', {'movies':movies, 'categories':categories, 'category':category})

def status_filter(request, movie_status):
    statuses = Status.objects.all()
    status = Status.get_status_id(movie_status)
    movies = Movie.filter_by_status(movie_status)
    title = f'{status} Photos'
    return render(request, 'status.html', {'movies':movies, 'statuses':statuses, 'status':status})

def movie_filter(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"single.html",{"movie":movie})