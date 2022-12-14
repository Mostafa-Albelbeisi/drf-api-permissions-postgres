from rest_framework import serializers

from .models import Fone, Circuits


class FoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fone
        fields = [
            "carName",
            "carModel",
            "carFactory",
            "driver",
            "ratingDriver",
            "trophyDriver",
            "founder",
        ]

        # fields = "__all__"


class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuits
        fields = "__all__"
