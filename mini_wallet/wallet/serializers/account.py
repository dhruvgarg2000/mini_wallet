from rest_framework import serializers

from wallet.models import Wallet

class AccountSerializer(serializers.Serializer):

    customer_xid = serializers.UUIDField(required=True)