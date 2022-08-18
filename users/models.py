from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from .manager import UserManager



class CoreUser(AbstractBaseUser, PermissionsMixin):
    """ The main user object """
    class Meta :
        verbose_name = "Core User"
        verbose_name_plural = "Core Users"
    
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    groups = models.ForeignKey(
                        Group,
                        on_delete=models.SET_NULL,
                        verbose_name=_("groups"),
                        blank=True,
                        null=True,
                        help_text=_(
                            "The groups this user belongs to. A user will get all permissions "
                            "granted to each of their groups."
                        ),
                        related_name="user_group",
                        related_query_name="user_groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_set_permission",
        related_query_name="user_permissions",
    )
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

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

    def __str__(self) :
        return f"CoreUser {self.email} #{self.id}"

class StaffUser(CoreUser):
    ''' This user is allowed to access the admin panel '''
    class Meta :
        verbose_name = "Staff User"
        verbose_name_plural = "Staff Users"
    
    token = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self) :
        return f"Staff  {self.email}"
    
    def save(self, *args, **kwargs):
        self.is_staff = True
        return super(StaffUser, self).save(*args, **kwargs)

