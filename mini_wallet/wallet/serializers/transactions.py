from rest_framework import serializers

from wallet.models import Transactions

class TransactionSerializer(serializers.Serializer):
    
    id = serializers.SerializerMethodField()
    transaction_by = serializers.SerializerMethodField()
    amount = serializers.IntegerField(required=True)
    transaction_type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    transaction_at = serializers.DateTimeField(required=True)
    reference_id = serializers.UUIDField(required=True)

    def get_id(self, obj):
        if obj:
            return obj.uuid
        raise serializers.ValidationError()

    def get_transaction_by(self, obj):
        if obj and obj.wallet and obj.wallet.owner:
            return obj.wallet.owner.uuid
        raise serializers.ValidationError()

    def get_status(self, obj):
        if obj:
            return obj.get_status_display()
        raise serializers.ValidationError()
    
    def get_transaction_type(self, obj):
        if obj:
            return obj.get_transaction_type_display()
        raise serializers.ValidationError()