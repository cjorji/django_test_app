from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class statusTests(APITestCase):

	def test_hello_world(self):
		"""
		check if we get "Hello, world!" from hello_world endpoint
		"""

		url = 'hello_world'
		data = {}
		expected = {"message": "Hello, world!"}
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response, expected)


	def test_earliest_10_movies_of_current_year(self):
		"""
		ensure we get the same movies for each req
		"""

		url = 'earliest_10_movies_of_current_year'
		data = {}
		expected = {"earliest_10_movies_for_2020": "Merrily We Roll Along, Avatar 5, Black Blood, Avatar 4, Son Göktürk, Doc Savage, Fantastic Beasts 5, Untitled Evel Knievel Project, Rogue, Untitled Kevin Hart/Malcolm D. Lee Action-Comedy"}
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response, expected)

	def test_get_latest_movies_for_actors(self):
		"""
		make sure we get the correct movies for given actors
		"""

		url = 'get_latest_movies_for_actors'
		data = {"actors":"Bruce Willis, Sylvester Stallone"}
		expected = {"movies": "The Expendables 2, The Expendables, Vanity Fair: Killers Kill, Dead Men Die, Jackie Chan: My Story"}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response, expected)

