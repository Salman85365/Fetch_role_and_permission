from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import uuid
class User(AbstractUser):
    ADMIN = 'Admin'
    MEMBER = 'Member'
    CUSTOMER = "Customer"
    USER_TYPE_CHOICES = (
        (ADMIN, 'ADMIN'),
        (MEMBER, 'Member'),
        (CUSTOMER, 'Customer'),
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    password = models.CharField(_('password'), max_length=128,blank=True,null=True)

    dob = models.DateField(null=True,blank=True)
    role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=CUSTOMER)
    is_active = models.BooleanField(default=True)
    email = models.EmailField()
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.id)