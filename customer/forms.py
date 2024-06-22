from django import forms
from customer.models import Customer, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class LoginForm(forms.Form):
    # username = forms.CharField()
    phone_number = forms.CharField()
    password = forms.CharField()

    #  the difference between get and filter
    """ get() returns DoesNotExists when nothing is found,
        filter() returns None when nothing is found"""
    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(f'{phone_number} does not exist.')
        return phone_number

    # def clean_email(self):
    #     email = self.data.get('email')
    #     if not User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email does not exist')
    #     return email

    def clean_password(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{phone_number} does not exists')
        return password
