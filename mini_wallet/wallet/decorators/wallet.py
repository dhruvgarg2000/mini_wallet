from rest_framework.response import Response
from rest_framework import  status
from django.shortcuts import get_object_or_404

from wallet.models import User, Wallet

def check_wallet_enabled(view_func):
    def wrapped_view(request, *args, **kwargs):
        # Assuming you have an 'enabled' field in your model that indicates the object's status
        # Replace 'YourModel' with the name of your model and 'enabled' with the actual field name
        user = User.objects.filter(uuid=request.user_id, is_active=True).first()
        wallet = get_object_or_404(Wallet, owner=user)
        if not wallet.enabled:
            return Response({'error' : 'Wallet is not enabled. Please enable the wallet.'}, status=status.HTTP_400_BAD_REQUEST)

        return view_func(request, *args, **kwargs)

    return wrapped_view