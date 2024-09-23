# user_app/views.py

from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from profile_app.models import UserDetails
from .serializers import UserDetailsSerializer
from global_messages import ERROR_MESSAGES as GLOBAL_ERROR_MESSAGES

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        response_data = {'status': 'error'}

        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 50))
        search_term = request.GET.get('searchTerm', '')

        # Fetch UserDetails with related User and CustomGroup
        user_details = UserDetails.objects.select_related('user').prefetch_related('user__groups')

        if search_term:
            q_objects = Q(
                user__username__icontains=search_term
            ) | Q(
                current_city__icontains=search_term
            ) | Q(
                permanent_city__icontains=search_term
            ) | Q(
                college__name__icontains=search_term
            ) | Q(
                organization__name__icontains=search_term
            )
            user_details = user_details.filter(q_objects)

        try:
            user_details = user_details.order_by('-created_at')[offset:offset + limit]
        except Exception as e:
            response_data.update({
                'status': 'error',
                'message': GLOBAL_ERROR_MESSAGES['data_fetch_error'],
                'error_code': 'BAD_REQUEST',
                'details': str(e)
            })
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        if user_details:
            serialized_data = UserDetailsSerializer(user_details, many=True).data
            response_data.update({
                'status': 'success',
                'data': serialized_data,
                'message': 'User details fetched successfully.'
            })
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data.update({
                'status': 'error',
                'message': 'No users found.',
                'error_code': 'RESOURCE_NOT_FOUND'
            })
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
