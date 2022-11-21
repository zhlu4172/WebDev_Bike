from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from django.utils.translation import gettext_lazy as _


# Create your forms here.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, help_text="Required add a valid email address.")

    class Meta:
        model = NewUser
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            NewUser.objects.get(email=email)
        except NewUser.DoesNotExist:
            return email
        raise forms.ValidationError(
            _("A user with that email already exists."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."))
        return password2


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

