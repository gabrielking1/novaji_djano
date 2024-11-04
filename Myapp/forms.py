from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

# Create your forms here.

class RegForm(UserCreationForm):

    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField()
        
    

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','phone_number', 'password1' ,'password2' )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user