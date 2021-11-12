from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User  # pylint: disable=imported-auth-user


class AuthWSGIRequest(WSGIRequest):
    user: User