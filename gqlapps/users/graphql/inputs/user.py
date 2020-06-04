import graphene


class UserCreateInput(graphene.InputObjectType):
    email = graphene.String()
    username = graphene.String()
    password = graphene.String()


class UserDeleteInput(graphene.InputObjectType):
    id = graphene.Int()
    slug = graphene.String()


class UserEditPatchInput(graphene.InputObjectType):
    dob = graphene.String()


class UserEditInput(graphene.InputObjectType):
    id = graphene.Int()
    slug = graphene.String()
    patch = graphene.InputField(UserEditPatchInput)
