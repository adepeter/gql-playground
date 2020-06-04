from django.urls import include, path

urlpatterns = [
    path('graphql/', include('gqlapps.users.graphql.urls')),
    # path('user/', include('gqlapps.users.urls.user')),
]
