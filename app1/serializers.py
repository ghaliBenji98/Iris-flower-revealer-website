from rest_framework import serializers
from . models import flowerDim

class FlowerSerializers(serializers.ModelSerializer):
	class Meta:
		model=flowerDim
		fields='__all__'
