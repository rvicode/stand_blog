from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'first_name', 'last_name', )


class CustomUserChangForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'first_name', 'last_name', )

