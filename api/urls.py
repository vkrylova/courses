from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

# For POST, DELETE add header
# Key:Authorization:
# Value:ApiKey admin:wasd12345

# api/v1/courses/ GET, POST
# api/v1/courses/{pk}/ GET, DELETE
# api/v1/categories/ GET
# api/v1/categories/{pk}/ GET

urlpatterns = [
    path('', include(api.urls), name='index'),
]