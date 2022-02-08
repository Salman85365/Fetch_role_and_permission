from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import serializers


class BaseAPIView(APIView):
    serializer_class = Serializer

    def get_serializer_context(self):
        return {'request': self.request, 'view': self}

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer(self, *a, **kw):
        serializer_class = self.get_serializer_class()
        kw['context'] = self.get_serializer_context()
        return serializer_class(*a, **kw)

def success_response(data):
    return {"status": "success", "data": data}

def validation_error_response(errors):
    return {"status": "error","errors": errors}


class IDSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)


class IDsSerializer(serializers.Serializer):
    ids = serializers.ListField(required=True, child=serializers.UUIDField(required=True))
