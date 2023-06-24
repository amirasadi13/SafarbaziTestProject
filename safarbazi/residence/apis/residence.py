from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from safarbazi.residence.models import Residence
from safarbazi.residence.services import create_residence


class ResidenceApi(APIView, LimitOffsetPagination):

    class InputResidenceSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=100, required=True)

    class OutPutResidenceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Residence
            fields = '__all__'

    @extend_schema(request=InputResidenceSerializer, responses=OutPutResidenceSerializer)
    def post(self, request):
        serializer = self.InputResidenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            residence = create_residence(title=serializer.validated_data.get("title"))
        except Exception as ex:
            return Response(data={'message': f"Database Error {ex}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.OutPutResidenceSerializer(residence, context={"request": request}).data)
