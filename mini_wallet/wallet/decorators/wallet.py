from rest_framework.response import Response
from rest_framework import  status
from django.shortcuts import get_object_or_404

from wallet.models import User, Wallet

def check_wallet_enabled(wallet_status):
    def wallet_decorator(view_func):
        def wrapped_view(request, *args, **kwargs,):
            if wallet_status == 'disabled':
                is_enabled = False
            elif wallet_status == 'enabled':
                is_enabled = True
            else:
                is_enabled = None
            user_id = request.request.data.get('customer_xid', '')
            user = User.objects.filter(uuid=user_id, is_active=True).first()
            wallet = get_object_or_404(Wallet, owner=user)
            if wallet.is_enabled != is_enabled:
                return Response({'error' : f'Wallet is {"enabled" if wallet.is_enabled else "disabled"}!! Please {wallet_status} the Wallet.'}, status=status.HTTP_400_BAD_REQUEST)

            return view_func(request, user, wallet, *args, **kwargs)
        return wrapped_view
    return wallet_decorator