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
    item = models.ForeignKey('Listing', on_delete=models.CASCADE)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='offering_listing')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    date_made = models.DateField(auto_created=True)
    status = models.CharField(choices=offer_choices, max_length=1)

    def __str__(self):
        return '{} from {}'.format(self.item.name, self.owner.username)


class Listing(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='listings/', null=True, blank=True)

    offers = models.ManyToManyField(Offer, null=True, blank=True)

    def __str__(self):
        return self.name
