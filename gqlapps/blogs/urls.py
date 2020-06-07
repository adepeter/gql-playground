from django.urls import include, path

urlpatterns = [
    path('graphql/', include('gqlapps.blogs.graphql.urls'))
]
