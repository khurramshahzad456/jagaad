from rest_framework import status
from django.db.models import Count, Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StatsMessage
from .serializers import StatsMessageSerializer


@api_view(['POST'])
def create_stats_message(request):
    try:
        serializer = StatsMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_stats_information(request):
    try:
        # Perform the required database queries to retrieve the statistical information
        stats = StatsMessage.objects.values('customerId', 'type').annotate(
            total_messages=Count('customerId'),
            total_amount=Sum('amount')
        )

        # Prepare the response data
        response_data = []
        for stat in stats:
            data = {
                'customerId': stat['customerId'],
                'type': stat['type'],
                'totalMessages': stat['total_messages'],
                'totalAmount': str(stat['total_amount']),
            }
            response_data.append(data)

        return Response(response_data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
