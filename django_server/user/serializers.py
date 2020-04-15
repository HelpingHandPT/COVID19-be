from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import MyUser

# inherit from ModelSerializer (generates automaticallyvalidators for the serializer based on the model)
# It will automatically generate a set of fields based on the model.
# It will automatically generate validators for the serializer, such as unique_together validators.
# It includes simple default implementations of .create() and .update().
# Read more about it here: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True, # make sure email is provided
            validators=[UniqueValidator(queryset=MyUser.objects.all())] # make sure email is unique
            )
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())],
            min_length=5,
            max_length=20
            )
    password = serializers.CharField(
            write_only=True,
            required=True,
            max_length=256
            )
    first_name = serializers.CharField(
            required=True,
            max_length=25
            )
    last_name = serializers.CharField(
            required=True,
            max_length=25
            )

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'], validated_data['username'], validated_data['password'],
        validated_data['first_name'], validated_data['last_name'])
        return user


    class Meta:
        model = MyUser
        fields = ('user_id', 'email', 'username', 'password', 'first_name', 'last_name')