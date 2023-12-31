from django.db import models
import uuid

# Create your models here.
class  User(models.Model):
    class Meta:
        db_table = 'customer_service'

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)
    is_active = models.BooleanField(default=True, null=False)


class Wallet(models.Model):
    class Meta:
        db_table = 'wallet'

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    balance = models.IntegerField(default=0, null=False)
    is_enabled = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Transactions(models.Model):
    class Meta:
        db_table = 'transactions'

    TRANSACTION_TYPES = [
        (1, "Credit"),
        (2, "Debit")
    ] 

    TRANSACTION_STATUSES = [
        (1, "Success"),
        (2, "Failed")
    ]
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.IntegerField(default=0, null=False)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES)
    status = models.IntegerField(choices=TRANSACTION_STATUSES)
    transaction_at = models.DateTimeField(auto_now_add=True)
    reference_id = models.UUIDField(editable=False, unique=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)