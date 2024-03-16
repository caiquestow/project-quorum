from quorum_data_app.views import process_legislators, process_bills
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Retrieve a list of legislators and their votes",
    responses={200: 'OK'},
    tags=['Legislators']
)
def legislator_info(request):
    legislators = process_legislators('dataset/legislators_(2).csv')
    return Response(legislators)

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Retrieve a list of bills and voting results",
    responses={200: 'OK'},
    tags=['Bills']
)
def bill_info(request):
    bills_data = process_bills('dataset/bills_(2).csv')
    return Response(bills_data)
