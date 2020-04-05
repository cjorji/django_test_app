# Initializing the app

one dir up from project root:
```
python -m venv django_test_app
cd django_test_app
```
for windows: ```./Scripts/activate```
for linux/osx: ```source ./Scripts/activate```

```
pip install -r pip_reqs.txt
cd myapp
python manage.py runserver
```

the server should now be up and running locally

# endpoints

## hello_world
GET: returns a hello world message json obj

## earliest_10_movies_of_current_year
GET: returns a list of 10 earliest movies of the current year

## latest_movies_for_actors
POST: post a json object with a single field "actors" and the api will return a list of maximum 10 latest movies 
object example:
```
{"actors":"Bruce Willis, Sylvester Stallone"}
```

### current issue:
unit tests, can't get the testing part connect to the rest of the app fully and all tests return 404
