from collections import namedtuple

ConnectArgsType = namedtuple('ConnectArgsType', [
    'verify', 'verify_expiration', 'key', 'audience', 'issuer', 'algorithm', 'auth_header_prefix', 'decode_options'
])

CONNECT_ARGS = ConnectArgsType(
    verify=None,
    verify_expiration=None,
    key=None,
    audience=None,
    issuer=None,
    algorithm=None,
    auth_header_prefix=None,
    decode_options=None,
)


def configure(
    key,
    audience,
    issuer,
    algorithm,
    verify=True,
    verify_expiration=True,
    auth_header_prefix='Bearer',
    decode_options=None,
):
    global CONNECT_ARGS
    CONNECT_ARGS = ConnectArgsType(
        verify=verify,
        verify_expiration=verify_expiration,
        key=key,
        audience=audience,
        issuer=issuer,
        algorithm=algorithm,
        auth_header_prefix=auth_header_prefix,
        decode_options=decode_options or {},
    )


__all__ = ["configure", "CONNECT_ARGS"]
