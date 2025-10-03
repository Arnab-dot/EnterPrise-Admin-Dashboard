from rest_framework import serializers
import clients
from clients.models import Clients, Invoice
from users.models import Organization, CustomUser

"""defining the serializers"""


class ClientSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="created_by.role", read_only=True)

    class Meta:
        model = Clients
        fields = ["id", "username", "user_address", "dob", "phone_no", "created_by", "created_at", "organization",
                  "role"]
        read_only_fields = ["created_by", "created_at", "organization"]
        extra_kwargs = {
            'dob': {'required': True}
        }


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ["client", "organization", "due_date", "status", "created_by", "created_at", "amount", "id"]
        read_only_fields = ["organization", "created_at", "created_by"]  # Removed "status" from read_only_fields
