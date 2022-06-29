from rest_framework import serializers
from .models import EmployeeUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ["id", "name", "email", "mob", "role"]

class RegisterEmployeeSerializer(serializers.ModelSerializer):

        model = EmployeeUser
        email = serializers.CharField( required=True)
        password = serializers.CharField(write_only=True,required=True)
        class Meta:
            model = EmployeeUser
            fields = ('id', 'email','name','mob' ,'password', 'role' )
        def create(self,validated_data):
            user = EmployeeUser.objects.create(id = validated_data['id'], email = validated_data['email'], mob= validated_data['mob'], role = validated_data['role'])
            user.set_password(validated_data['password'])
            user.save()
            return user

class LoginEmployeeSerializer(serializers.ModelSerializer):
    model = EmployeeUser
    email = serializers.CharField(required=True)
    password = serializers.CharField(max_length=200)
    role = serializers.CharField(max_length=200)
    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        role = data['role']
        if user is None:
            raise serializers.ValidationError("Invalid Credentials")
        else:
            data = {
                'message':'Login Successful',
                'email':user.email,
                'role': user.role
            }

            return data

class RegisterEmployee(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ('id','email', 'name', 'mob',  'role')

    def create(self,validated_data):
        if validated_data['role'] == 'superuser' or validated_data['role'] =='manager':
            self.fail('bad_request')
        else:
            password =