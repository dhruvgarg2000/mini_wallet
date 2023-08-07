import jwt
import datetime
from mini_wallet import settings

def generate_jwt_token(customer_id):

    payload = {
        'customer_id': customer_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


def decode_jwt(token):
    try:
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    

def get_token_from_header(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header.startswith('Token '):
        token = auth_header[len('Token '):].strip()
        return token