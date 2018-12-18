import jwt

from .config import CONNECT_ARGS


def verify_jwt_token(token):
    if len(token) < 1 and not CONNECT_ARGS.verify:
        return

    # get payload from token, BEFORE verification, to get individual secret key
    unverified_payload = jwt.decode(token, None, False)

    options = {'verify_exp': CONNECT_ARGS.verify_expiration}
    options.update(CONNECT_ARGS.decode_options)

    issuer = CONNECT_ARGS.issuer
    if callable(issuer):
        issuer = issuer(unverified_payload)

    key = CONNECT_ARGS.key
    if callable(key):
        key = key(unverified_payload)

    return jwt.decode(
        token,
        key,
        verify=CONNECT_ARGS.verify,
        options=options,
        issuer=issuer,
        audience=CONNECT_ARGS.audience,
        algorithms=[CONNECT_ARGS.algorithm],
    )


__all__ = ['verify_jwt_token']
