from django.urls import include, path

urlpatterns = [
    path('blogs/', include('gqlapps.blogs.urls')),
    path('categories/', include('gqlapps.categories.urls')),
    path('users/', include('gqlapps.users.urls')),
]
