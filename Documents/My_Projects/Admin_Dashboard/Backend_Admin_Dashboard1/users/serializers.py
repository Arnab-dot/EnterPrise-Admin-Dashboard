from django.template.context_processors import request
from rest_framework import serializers
from .models import CustomUser, CustomUserManager, Organization


class RegisterOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["email","role","organization"] #takes the fields for the organization at the admin level
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')

        request = self.context.get('request')
        admin_user = getattr(request, 'user', None)

        if admin_user and admin_user.is_authenticated:
            # assign same organization as admin creating the user
            validated_data['organization'] = admin_user.organization
        else:
            # For first user, organization must be provided in request data
            # or create a default one
            from .models import Organization
            org = Organization.objects.create(name="Default Org", address="Default Address")
            validated_data['organization'] = org

        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields=["name","address"]

class ProfileSerializer(serializers.ModelSerializer):
    organization=OrganizationSerializer(read_only=True)
    class Meta:
        model=CustomUser
        fields=["email","role"]



