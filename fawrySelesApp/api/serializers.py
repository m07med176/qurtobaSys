from rest_framework import serializers
from fawrySelesApp.models import RassedProtal,TransactionsPortal
class S_RassedProtal(serializers.ModelSerializer):
    class Meta:
        model = RassedProtal
        fields = '__all__'


class S_TransactionsPortal(serializers.ModelSerializer):
    class Meta:
        model = TransactionsPortal
        fields = '__all__'
