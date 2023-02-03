from rest_framework import serializers

available_websites = [
    ('AMAZON', 'AMAZON'),
    ('MYNTRA', 'MYNTRA'),
]

class PriceQuerySerializer(serializers.Serializer):
    url = serializers.URLField(max_length=1000, allow_blank=False)
    website = serializers.ChoiceField(
        choices=available_websites,
        allow_blank=False,
    )
