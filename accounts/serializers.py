from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from carts.models import Cart


from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    def get_address(self, obj: Account):
        try:
            address_obj = obj.address
            return {
                "id": address_obj.id,
                "city": address_obj.city,
                "street": address_obj.street,
                "number": address_obj.number,
                "zip_code": address_obj.zip_code,
            }
        except Address.DoesNotExist:
            return None

    def create(self, validated_data: dict) -> Account:
        user = Account.objects.create_user(**validated_data)
        Cart.objects.create(user=user)

        return user

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "address",
            "cart",
        ]
        read_only_fields = ["is_superuser", "cart"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                    )
                ]
            },
        }
