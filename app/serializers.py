from rest_framework.serializers import ModelSerializer
from app.models import MyModel

class ModelSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["field1","field2"]