from rest_framework import serializers
from .models import BlockedSite, UserAccess


class BlockedSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedSite
        fields = ['url', 'created_at']
        
class UserAccessSerializer(serializers.ModelSerializer):
    blocked_sites = BlockedSiteSerializer(many=True, read_only=True) 
    blocked_sites_ids = serializers.PrimaryKeyRelatedField(queryset=BlockedSite.objects.all(), many=True, write_only=True)  # سایت‌های مسدود شده برای ایجاد یا ویرایش

    class Meta:
        model = UserAccess
        fields = ['user_id', 'blocked_sites', 'blocked_sites_ids', 'created_at']

    def update(self, instance, validated_data):
        blocked_sites_data = validated_data.pop('blocked_sites_ids', [])

        instance.blocked_sites.clear()


        for site_id in blocked_sites_data:
            site = BlockedSite.objects.get(id=site_id)
            instance.blocked_sites.add(site)

        instance.save()
        return instance
      
