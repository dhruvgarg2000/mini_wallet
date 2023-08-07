from django.http import JsonResponse
from authentication.handlers.authentication import decode_jwt
from rest_framework import  status


class JWTAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_path = ['/api/v1/init/', '/authentication/api/v1/signup/', '/authentication/api/v1/login/']

        token = self.get_token_from_header(request)
        decoded_payload = decode_jwt(token)
        if decoded_payload or request.path in url_path:
            if decoded_payload:
                request.user_id = decoded_payload.get('customer_id')
            response = self.get_response(request)
            return response
        return JsonResponse({'error': 'Invalid or expired token.'}, status=status.HTTP_401_UNAUTHORIZED)

    
    def get_token_from_header(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Token '):
            token = auth_header[len('Token '):].strip()
            return token