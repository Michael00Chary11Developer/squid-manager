from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccess, BlockedSite
from .serializers import UserAccessSerializer


class BlockSiteForUser(APIView):
    def post(self, request, user_id):
        try:
   
            user_access = UserAccess.objects.get(user_id=user_id)
            blocked_sites = request.data.get('blocked_sites_ids', [])

            user_access.blocked_sites.clear()

            for site_id in blocked_sites:
                site = BlockedSite.objects.get(id=site_id)
                user_access.blocked_sites.add(site)

            user_access.save()
            return Response({"message": "User sites updated successfully."}, status=status.HTTP_200_OK)

        except UserAccess.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)



class UserAccessDetail(APIView):
    def get(self, request, user_id):
        try:
            user_access = UserAccess.objects.get(user_id=user_id)
            serializer = UserAccessSerializer(user_access)
            return Response(serializer.data)

        except UserAccess.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
