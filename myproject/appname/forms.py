from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from appname.models import User

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User