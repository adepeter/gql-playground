from django.contrib.auth import get_user_model

import graphene

from ..types.user import UserType

User = get_user_model()


class UserQueries(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
