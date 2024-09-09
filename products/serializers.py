from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)
        # validated_data['author'] = self.context['request'].user
        # return super().create(validated_data)