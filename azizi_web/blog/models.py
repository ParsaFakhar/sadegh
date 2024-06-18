from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError
from django.utils.html import escape


# Fetch the superuser with a specific username
def get_default_user_id():
    try:
        default_user = User.objects.get(username='default_user')
        return default_user.id
    except User.DoesNotExist:
        raise ValueError("No superuser found with the specified username.")
    except User.MultipleObjectsReturned:
        raise ValueError("Multiple superusers found with the specified username. Please ensure usernames are unique.")


def get_default_choice_id():
    # Return a valid primary key for the Choice model
    return 1


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(_(self.name))


class Post(models.Model):
    header = models.CharField(max_length=50)

    def clean(self):
        super().clean()
        # Sanitize the file name
        self.image.name = re.sub(r'[^\w\s-]', '', self.image.name).strip().lower()
        self.image.name = re.sub(r'[-\s]+', '-', self.image.name)
        self.text = escape(self.text)
        # Validate the URL
        if not self.image.url.startswith('/img/'):
            raise ValidationError(_('Invalid image URL from models.py'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    image = models.ImageField(upload_to='img')
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_default_user_id)
    model = models.ForeignKey(Choice, on_delete=models.SET_DEFAULT, default=get_default_choice_id)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
