from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Order, Department, Course
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none(), required=False)

    class Meta:
        model = Order
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'department', 'course', 'purpose', 'materials_provide']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset

        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
