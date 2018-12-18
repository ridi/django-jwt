import jwt


def encode_jwt(payload, private_key):
    return jwt.encode(payload, private_key, algorithm='RS256').decode()
