from rest_framework import serializers

class AccountSerializer(serializers.Serializer):

    customer_xid = serializers.UUIDField(required=True)