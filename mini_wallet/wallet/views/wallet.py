from rest_framework.response import Response
from rest_framework import  status, viewsets
from rest_framework.decorators import action
from authentication.handlers.authentication import generate_jwt_token
from wallet.decorators.wallet import check_wallet_enabled
from wallet.models import User, Wallet
from wallet.serializers.account import AccountSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime

class AccountViewSet(viewsets.ViewSet):

    def create(self, request):
        '''Create the account for the user'''
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_id = serializer.data.get('customer_xid')
            user = get_object_or_404(User, uuid=user_id)
            try:
                Wallet.objects.get(owner=user)
                return Response({"message" : "Account is already created!!"})
            except Wallet.DoesNotExist:
                if user.is_active:
                    Wallet.objects.create(owner=user)
                    token = generate_jwt_token(user_id)
                    return Response({
                                "data": {
                                    "token": token
                                },
                                "status": "success"
                            }, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message" : "User is inactive"})


class WalletViewSet(viewsets.ViewSet):

    @check_wallet_enabled('disabled')
    def create(self, request, user, wallet):
        '''Enable the wallet'''
        wallet.is_enabled = True
        wallet.enabled_at = datetime.now()
        wallet.save()

        return Response({
            "status": "success",
            "data": {
                "wallet": {
                "id": wallet.uuid,
                "owned_by": user.uuid,
                "status": "enabled" if wallet.is_enabled else "disabled",
                "enabled_at": wallet.updated_at,
                "balance": wallet.balance
                }
            }
        }, status=status.HTTP_201_CREATED)


    @check_wallet_enabled('enabled')
    def partial_update(self, request, user, wallet):
        '''Disable the wallet'''
        wallet.is_enabled = False
        wallet.enabled_at = datetime.now()
        wallet.save()

        return Response({
            "status": "success",
            "data": {
                "wallet": {
                "id": wallet.uuid,
                "owned_by": user.uuid,
                "status": "enabled" if wallet.is_enabled else "disabled",
                "disabled_at": wallet.updated_at,
                "balance": wallet.balance
                }
            }
        })


    @check_wallet_enabled('enabled')
    def list(self, request, user, wallet):
        '''Get information of the wallet'''
        pass


    @check_wallet_enabled('enabled')
    @action(detail=False, methods=["get"])
    def transactions(self, request, user, wallet):
        '''Get all the transactions of the wallet'''
        pass


    @check_wallet_enabled('enabled')
    @action(detail=False, methods=['post'])
    def deposits(self, request, user, wallet):
        '''Deposit the virtual money in the wallet'''
        pass


    @check_wallet_enabled('enabled')
    @action(detail=False, methods=['post'])
    def withdrawals(self, request, user, wallet):
        '''Withdrawal the virtual money in the wallet'''
        pass


# 1. Authentication middleware 
# 2. Decorator which checks whether the account is created or not
# 3. Decorator which checks wallet is enabled or not
# 4. Write the APIs