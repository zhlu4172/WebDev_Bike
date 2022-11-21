from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.core.mail import send_mail


class CustomAccountManager(BaseUserManager):

    def create_user(self, email=None, password=None, username=None):
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_user(self, email, password, **extra_fields):
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password):

        user = self.create_user(email, password)

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class NewUser(AbstractUser, PermissionsMixin):
    # If we're not using username, just ignore unique constraint for username
    username = models.CharField(max_length=30, unique=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    image_location = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)

    is_admin = models.BooleanField(_("admin status"), default=False, help_text=_(
        "Designates whether the user can log into this admin site."),)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomAccountManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
