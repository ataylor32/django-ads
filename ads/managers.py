import random

from ads.querysets import AdQuerySet
from django.db.models import Manager, Count


class AdManager(Manager):
    def get_queryset(self):
        return AdQuerySet(self.model)

    def category_ads(self, category):
        return self.get_queryset().category_ads(category)

    def public(self):
        return self.get_queryset().public()

    def zone_ads(self, zone):
        return self.get_queryset().zone_ads(zone)

    def random_ad(self, zone, category):
        ads = []
        for ad in self.zone_ads(zone).category_ads(category).public():
            ads += [ad] * ad.weight
        if not ads:
            return None
        return random.choice(ads)
