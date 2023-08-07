from rest_framework import serializers


class AccountSerializer(serializers.Serializer):

    customer_xid = serializers.UUIDField(required=True)


class EnableWalletSerializer(serializers.Serializer):

    id = serializers.SerializerMethodField()
    owned_by = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    enabled_at = serializers.SerializerMethodField()
    balance = serializers.IntegerField(required=True)

    def get_id(self, obj):
        if obj:
            return obj.uuid
        raise serializers.ValidationError()

    def get_owned_by(self, obj):
        if obj and obj.owner.uuid:
            return obj.owner.uuid
        raise serializers.ValidationError()

    def get_status(self, obj):
        if obj:
            return "enabled" if obj.is_enabled else "disabled"
        raise serializers.ValidationError()
        
    def get_enabled_at(self, obj):
        if obj:
            return obj.updated_at
        raise serializers.ValidationError()
        

class DisableWalletSerializer(serializers.Serializer):

    id = serializers.SerializerMethodField()
    owned_by = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    disabled_at = serializers.SerializerMethodField()
    balance = serializers.IntegerField(required=True)

    def get_id(self, obj):
        if obj:
            return obj.uuid
        raise serializers.ValidationError()

    def get_owned_by(self, obj):
        if obj and obj.owner.uuid:
            return obj.owner.uuid
        raise serializers.ValidationError()

    def get_status(self, obj):
        if obj:
            return "enabled" if obj.is_enabled else "disabled"
        raise serializers.ValidationError()
        
    def get_disabled_at(self, obj):
        if obj:
            return obj.updated_at
        raise serializers.ValidationError()
        

class DepositWithdrawalTransactionSerializer(serializers.Serializer):

    amount = serializers.IntegerField(required=True)
    reference_id = serializers.UUIDField(required=True)


class DepositTransactionSerializer(serializers.Serializer):

    id = serializers.SerializerMethodField()
    deposited_by = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    deposited_at = serializers.SerializerMethodField()
    amount = serializers.IntegerField(required=True)
    reference_id = serializers.UUIDField(required=True)

    def get_id(self, obj):
        if obj:
            return obj.uuid
        raise serializers.ValidationError()

    def get_deposited_by(self, obj):
        if obj and obj.wallet and obj.wallet.owner:
            return obj.wallet.owner.uuid
        raise serializers.ValidationError()

    def get_status(self, obj):
        if obj:
            return obj.get_status_display()
        raise serializers.ValidationError()
        
    def get_deposited_at(self, obj):
        if obj:
            return obj.transaction_at
        raise serializers.ValidationError()


class WithdrawalTransactionSerializer(serializers.Serializer):

    id = serializers.SerializerMethodField()
    withdrawn_by = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    withdrawn_at = serializers.SerializerMethodField()
    amount = serializers.IntegerField(required=True)
    reference_id = serializers.UUIDField(required=True)

    def get_id(self, obj):
        if obj:
            return obj.uuid
        raise serializers.ValidationError()

    def get_withdrawn_by(self, obj):
        if obj and obj.wallet and obj.wallet.owner:
            return obj.wallet.owner.uuid
        raise serializers.ValidationError()

    def get_status(self, obj):
        if obj:
            return obj.get_status_display()
        raise serializers.ValidationError()
        
    def get_withdrawn_at(self, obj):
        if obj:
            return obj.transaction_at
        raise serializers.ValidationError()