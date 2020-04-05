#from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import datetime

from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover, Person

tmdb = TMDb()
tmdb.api_key = 'a14e33fe467a60557f2ce3b666abfba7'
tmdb.language = 'en'
# tmdb.debug = True
movie = Movie()
discover = Discover()
person = Person()


"""
Hello world
"""
@api_view(['GET'])
def hello_world(request):
	return Response({"message": "Hello, world!"})


"""
get 10 earliest movies
"""
@api_view(['GET'])
def get_earliest(request):
	current_year = str(datetime.datetime.now().year)
	current_year_start = current_year + '-01-01'

	movie = discover.discover_movies({
		'primary_release_date.gte': current_year_start,
		'sort_by': 'release_date.desc'
	})

	return Response({'earliest_10_movies_for_' + current_year:', '.join([str(x) for x in movie[:10]])})


"""
get latest 10 movies for set of actors
"""
@api_view(['GET', 'POST'])
def get_latest_movies_for_actors(request):
	if 'actors' not in request.data or request.method != 'POST':
		return Response({'message':'invalid request'})
	else:
		try:
			actor_ids = ','.join([str(person.search(actor)[0].id) for actor in request.data['actors'].split(',')])
		except IndexError:
			return Response({'message':'invalid actor/s'})

		movie = discover.discover_movies({
			'with_cast' : actor_ids,
			'sort_by' : 'release_date.desc'
			})
		return Response({'movies':', '.join([str(x) for x in movie[:10]])})
