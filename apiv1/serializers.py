from rest_framework import serializers
from demo.models import Appartement, AppartementType


class AppartementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppartementType
        fields = ('title', )


class AppartementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Appartement
        fields = ('pk', 'uuid', 'title', 'active', 'created', 'modified',
                  'published', 'publish_date_start', 'publish_date_end',
                  'street_nr', 'postal_code', 'city', 'country',
                  'description', 'price', 'price_netto',
                  'available', 'rooms', 'floor', 'living_space', 'balconies', 'balconies_space',
                  'main_image', 'main_image_url',
                  'contact_name', 'contact_email', 'contact_phone',
        )