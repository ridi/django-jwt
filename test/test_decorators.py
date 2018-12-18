from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from test.utils import encode_jwt


class TestDecorators(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.private_key = b"""-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDdlatRjRjogo3WojgGHFHYLugdUWAY9iR3fy4arWNA1KoS8kVw
33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQsHUfQrSDv+MuSUMAe8jzKE4qW
+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5Do2kQ+X5xK9cipRgEKwIDAQAB
AoGAD+onAtVye4ic7VR7V50DF9bOnwRwNXrARcDhq9LWNRrRGElESYYTQ6EbatXS
3MCyjjX2eMhu/aF5YhXBwkppwxg+EOmXeh+MzL7Zh284OuPbkglAaGhV9bb6/5Cp
uGb1esyPbYW+Ty2PC0GSZfIXkXs76jXAu9TOBvD0ybc2YlkCQQDywg2R/7t3Q2OE
2+yo382CLJdrlSLVROWKwb4tb2PjhY4XAwV8d1vy0RenxTB+K5Mu57uVSTHtrMK0
GAtFr833AkEA6avx20OHo61Yela/4k5kQDtjEf1N0LfI+BcWZtxsS3jDM3i1Hp0K
Su5rsCPb8acJo5RO26gGVrfAsDcIXKC+bQJAZZ2XIpsitLyPpuiMOvBbzPavd4gY
6Z8KWrfYzJoI/Q9FuBo6rKwl4BFoToD7WIUS+hpkagwWiz+6zLoX1dbOZwJACmH5
fSSjAkLRi54PKJ8TFUeOP15h9sQzydI8zJU+upvDEKZsZc/UhT/SySDOxQ4G/523
Y0sz/OZtSWcol/UMgQJALesy++GdvoIDLfJX5GBQpuFgFenRiRDabxrE9MNUZ2aP
FaFp+DyAe+b4nDwuJaW2LURbr8AEZga7oQj0uYxcYw==
-----END RSA PRIVATE KEY-----"""

        self.public_key = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd
UWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs
HUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D
o2kQ+X5xK9cipRgEKwIDAQAB
-----END PUBLIC KEY-----"""

        self.settings = {
            'audience': 'audience',
            'issuer': 'issuer',
        }

        from ridi.django_jwt.config import configure
        configure(
            key=self.public_key,
            audience='audience',
            issuer='issuer',
            algorithm='RS256',
        )

    def test_jwt_required(self):
        from ridi.django_jwt.decorators import jwt_required

        @jwt_required()
        def view(request):
            return HttpResponse('view')

        encoded_jwt = encode_jwt({
            'aud': self.settings['audience'],
            'iss': self.settings['issuer'],
        }, self.private_key)

        request = self.factory.get('/', HTTP_AUTHORIZATION='Bearer ' + encoded_jwt)
        response = view(request)

        self.assertEqual(response.status_code, 200)

    def test_jwt_required_mixin(self):
        from ridi.django_jwt.decorators import JWTRequiredMixin
        from django.views.generic import View

        class IndexView(JWTRequiredMixin, View):
            def get(self, request):
                return HttpResponse()

        encoded_jwt = encode_jwt({
            'aud': self.settings['audience'],
            'iss': self.settings['issuer'],
        }, self.private_key)

        request = self.factory.get('/', HTTP_AUTHORIZATION='Bearer ' + encoded_jwt)
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
