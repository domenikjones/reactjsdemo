# -*- coding: utf-8 -*-
import datetime
from filer.fields.image import FilerImageField
from pytz import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField, UUIDField

APPARTEMENT_COUNTRIES = (
    ('ch', _(u"Switzerland")),
    ('de', _(u"Germany")),
    ('us', _(u"United States of America")),
)


class BaseModel(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        abstract = True


class AppartementManager(models.Manager):
    def active(self):
        return super(AppartementManager, self).get_queryset().filter(active=True)

    def published(self, filters=None):
        if not filters:
            filters = {}
        filters['published'] = True
        return super(AppartementManager, self).get_queryset().filter(**filters).order_by('-publish_date_start')

    def visible(self):
        return super(AppartementManager, self).get_queryset().filter(published=True,
                                                                     active=True,
                                                                     publish_date_start__lte=datetime.datetime.now(),
                                                                     publish_date_end__gte=datetime.datetime.now(),
        )


class Appartement(BaseModel):
    # general
    title = models.CharField(_(u"Title"), max_length=45, )
    active = models.BooleanField(_(u"Active"), default=False, )

    # published
    published = models.BooleanField(_(u"Published"), default=False, )
    publish_date_start = models.DateTimeField(_(u"Start Date"), null=True, blank=True, )
    publish_date_end = models.DateTimeField(_(u"End Date"), null=True, blank=True, )

    objects = AppartementManager()

    # announcement data
    description = models.TextField(_(u"Description"), null=True, )

    # object data
    types = models.ManyToManyField("AppartementType", null=True, related_name="appartement_types")
    price = models.IntegerField(_(u"Price (per Month"), default=0, )
    price_netto = models.IntegerField(_(u"Price Netto (per Month"), default=0, )
    rooms = models.FloatField(_(u"Rooms"), default=0, )
    floor = models.SmallIntegerField(_(u"Floor"), default=1, )
    balconies = models.SmallIntegerField(_(u"Balconies"), default=0, )
    balconies_space = models.SmallIntegerField(_(u"Balconies Space"), default=0, )
    living_space = models.SmallIntegerField(_(u"Living Space"), default=0, )
    available = models.DateField(_(u"Available Date"), null=True, )

    # location
    street_nr = models.CharField(_(u"Street"), max_length=255, null=True, )
    postal_code = models.CharField(_(u"Postal Code"), max_length=45, null=True, )
    city = models.CharField(_(u"City"), max_length=255, null=True, )
    country = models.CharField(_(u"Country"), max_length=45, null=True, choices=APPARTEMENT_COUNTRIES, )

    # contact information
    contact_name = models.CharField(_(u"Contact Name"), null=True, max_length=255, )
    contact_email = models.CharField(_(u"Contact Email"), null=True, max_length=255, )
    contact_phone = models.CharField(_(u"Contact Phone"), null=True, max_length=255, )

    # media
    main_image = FilerImageField(null=True, blank=True, )
    main_image_url = models.URLField(_(u"Main Image URL"), null=True, blank=True, )

    def is_visible(self):
        """
        Returns True when the appartement is visible for listing
        :return:
        """
        # if self.published and self.publish_date_start >= datetime.datetime.utcnow() and self.publish_date_end <= datetime.datetime.utcnow():
        #     return True
        return False

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        app_label = "demo"
        verbose_name = _(u"Appartement")
        verbose_name_plural = _(u"Appartements")
        ordering = ('title', )


class AppartementType(BaseModel):
    title = models.CharField(_(u"Type"), max_length=255, )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        app_label = "demo"
        verbose_name = _(u"Appartement Type")
        verbose_name_plural = _(u"Appartement Types")
        ordering = ('title', )
