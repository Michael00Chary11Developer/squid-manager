import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlockedSite
from .serializers import BlockedSiteSerializer

class BlockedSiteList(APIView):
    def get(self, request):
        sites = BlockedSite.objects.all()
        serializer = BlockedSiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlockedSiteSerializer(data=request.data)
        if serializer.is_valid():
            site = serializer.save()

 
            self.add_to_squid_manager(site.url)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_to_squid_manager(self, site_url):

        api_url = "http://squid-manager-api-url/block_site"  
        data = {"url": site_url}

        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print(f"Site {site_url} blocked successfully in Squid Manager.")
        else:
            print(f"Failed to block site {site_url} in Squid Manager.")

class UnblockSite(APIView):
    def delete(self, request, site_id):
        try:
            site = BlockedSite.objects.get(id=site_id)
            site.delete()

            self.remove_from_squid_manager(site.url)

            return Response({"message": "Site unblocked successfully."}, status=status.HTTP_200_OK)
        except BlockedSite.DoesNotExist:
            return Response({"error": "Site not found."}, status=status.HTTP_404_NOT_FOUND)

    def remove_from_squid_manager(self, site_url):
     
        api_url = "http://squid-manager-api-url/unblock_site"  
        data = {"url": site_url}

        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print(f"Site {site_url} unblocked successfully in Squid Manager.")
        else:
            print(f"Failed to unblock site {site_url} in Squid Manager.")
