# django-jwt

[![Build Status](https://travis-ci.com/ridi/django-jwt.svg?branch=master)](https://travis-ci.com/ridi/django-jwt)
[![PyPI](https://img.shields.io/pypi/v/ridi-django-jwt.svg)](https://pypi.org/project/ridi-django-jwt/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ridi-django-jwt.svg)](https://pypi.org/project/ridi-django-jwt/)
[![Coverage Status](https://coveralls.io/repos/github/ridi/django-jwt/badge.svg?branch=master)](https://coveralls.io/github/ridi/django-jwt?branch=master)

Provides JSON Web Token based authentication for RIDI's micro services made with django


## Installation

```bash
$ pip install ridi-django-jwt
```

## Usage

In your `settings.py`, call `configure` function to specify token specs.

```python
from ridi.django_jwt.config import configure

configure(
    key=open("key.pub", "rb"),
    audience='recommend',
    issuer='store',
    algorithm='RS256',
)
```

In your `views.py`, add `jwt_required` decorator to your view functions.

```pyton
from ridi.django_jwt.decorators import jwt_required

@jwt_required()
def index(request):
    # ...
```

If you want to add JWT authentication to your [Class-Based views](https://docs.djangoproject.com/en/stable/topics/class-based-views/), you can use mixin class instead.

```pytho
from django.views.generic import TemplateView
from ridi.django_jwt.decorators import JWTRequiredMixin

class IndexView(JWTRequiredMixin, TemplateView):
    template_name = "index.html"
```

## API

TBA

## Todo

- [ ] Provide authentication middleware
- [ ] Add unit tests
- [ ] Integrate with travis-ci
