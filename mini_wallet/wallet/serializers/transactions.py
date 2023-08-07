from rest_framework import serializers

from wallet.models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transactions
        fields = '__all__'