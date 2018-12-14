from functools import wraps

import jwt
from django.http.response import JsonResponse

from .config import CONNECT_ARGS
from .verify import verify_jwt_token

HTTP_401_UNAUTHORIZED = 401


def get_jwt_token_from_request(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')

    auth_header_prefix = CONNECT_ARGS.auth_header_prefix

    if CONNECT_ARGS.verify:
        if not auth_header:
            raise jwt.InvalidTokenError('The Authorization header must not be empty.')
        if not auth_header.startswith(auth_header_prefix):
            raise jwt.InvalidTokenError('The Authorization header must start with "{}".'.format(auth_header_prefix))

    token = auth_header[len(auth_header_prefix) + 1:]

    return token


def jwt_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                token = get_jwt_token_from_request(request)
                verify_jwt_token(token)
            except jwt.InvalidTokenError as e:
                return panic(str(e))

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


class JWTRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            token = get_jwt_token_from_request(request)
            verify_jwt_token(token)
        except jwt.InvalidTokenError as e:
            return panic(str(e))

        return super(JWTRequiredMixin, self).dispatch(request, *args, **kwargs)


def panic(message):
    return JsonResponse({'error': 'Unauthorized Error: ' + message}, status=HTTP_401_UNAUTHORIZED)
