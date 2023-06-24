from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from safarbazi.residence.selectors import get_room, get_calendar_available_dates, get_checked_dates_sum
from safarbazi.residence.validators import valid_date

"""
    This function is used to check the prices of a room for a given date range.
    It takes the following parameters:
        - room: UUID of the room
        - checkin: Date of checkin
        - checkout: Date of checkout
        - adult_extra_count: Number of extra adults
        - child_extra_count: Number of extra children
        - baby_extra_count: Number of extra babies
    
    It returns a response with the following data:
        - total_amount__sum: Total amount for the given date range
        - adult_extra_amount__sum: Amount for extra adults
        - child_extra_amount__sum: Amount for extra children
        - baby_extra_amount__sum: Amount for extra babies
    
    It first validates the input data and checks if the room exists.
    Then it checks if the given date range is available for the room.
    If the date range is available, it calculates the total amount for the given date range.
    Finally, it returns the response with the calculated amount.
    
"""


class CheckPricesApi(APIView):
    class InputCheckSerializer(serializers.Serializer):
        room = serializers.UUIDField(required=True)
        checkin = serializers.DateField(validators=[
            valid_date
        ], required=True)
        checkout = serializers.DateField(validators=[
            valid_date
        ], required=True)
        adult_extra_count = serializers.IntegerField(required=True)
        child_extra_count = serializers.IntegerField(required=True)
        baby_extra_count = serializers.IntegerField(required=True)

    @extend_schema(request=InputCheckSerializer)
    def post(self, request):
        serializer = self.InputCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        checkin = serializer.validated_data.get('checkin')
        checkout = serializer.validated_data.get('checkout')
        adult_count = serializer.validated_data.get('adult_extra_count')
        child_count = serializer.validated_data.get('child_extra_count')
        baby_count = serializer.validated_data.get('baby_extra_count')

        room = get_room(room_id=serializer.validated_data.get("room"))
        available_dates = get_calendar_available_dates(room=room, checkin=checkin,
                                                       checkout=checkout)

        if room.max_guests_count < int(room.base_guests_count + adult_count + child_count + baby_count):
            return Response(data={'message': 'Total Guests are more that required max length'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not available_dates:
            return Response(data={'message': 'Dates not available for selected range'},
                            status=status.HTTP_404_NOT_FOUND)

        total_amount = get_checked_dates_sum(available_dates=available_dates,
                                             adult_count=adult_count,
                                             child_count=child_count,
                                             baby_count=baby_count)

        return Response(total_amount)
