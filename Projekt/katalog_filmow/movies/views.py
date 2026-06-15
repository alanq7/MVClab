from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm


def movie_list(request):
    query = request.GET.get('q')

    if query:
        movies = (
            Movie.objects.filter(title__icontains=query)
            | Movie.objects.filter(director__icontains=query)
        ).order_by('-rating', 'title')
    else:
        movies = Movie.objects.all().order_by('-rating', 'title')

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'query': query,
    })


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', slug=movie.slug)
    else:
        form = MovieForm()

    return render(request, 'movies/movie_form.html', {'form': form})


def movie_update(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', slug=movie.slug)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {'form': form, 'movie': movie})


def movie_delete(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})