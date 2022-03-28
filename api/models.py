from django.db import models
from django.contrib.auth.models import User


class Offer(models.Model):
    offer_choices = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('D', 'Declined')
    )
    # TODO: ensure offering and listings are different
    # item offered for a listing
    offering = models.ForeignKey('Listing', on_delete=models.CASCADE)
    offer_for = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='offerFor_listing')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    date_made = models.DateField(auto_created=True)
    status = models.CharField(choices=offer_choices, max_length=1)

    def __str__(self):
        return '{} from {}'.format(self.offering.name, self.owner.username)

class ExtraUserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_admin = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return 'Info for {}'.format(self.user.username)


class Listing(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=30, default='category')

    # enter similar items seperated by , e.g.: "Fruits, Vegetables, item"
    similar_items = models.TextField(max_length=300, default='item')

    # items location
    longitude = models.CharField(max_length=7, blank=True, null=True)
    latitude = models.CharField(max_length=7, blank=True, null=True)


    owner = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)

    image1 = models.TextField(blank=True, null=True)
    image2 = models.TextField(blank=True, null=True)
    image3 = models.TextField(blank=True, null=True)
    image4 = models.TextField(blank=True, null=True)

    offers = models.ManyToManyField('self', null=True, blank=True, symmetrical=False)

    featured = models.BooleanField(default=False)

    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
