from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from institute.controller.institute import Institute

router = SimpleRouter()
api_route = [
    path('create-new-institute', Institute.as_view({'post':'create_new_institute'}),name='create_new_institute'),
    path('list-institute-details', Institute.as_view({'post':'list_all_institute'}),name='list_all_institute'),
]
urlpatterns = api_route
urlpatterns = format_suffix_patterns( urlpatterns)
