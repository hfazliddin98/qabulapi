from rest_framework import serializers
from .models import BakalavrHujat, BakalavrBolim, BakalavrTolov, BakalavrMalumot
from .models import MagistrHujat, MagistrBolim, MagistrTolov, MagistrMalumot
from .models import PhdHujat, PhdBolim, PhdTolov, PhdMalumot
from .models import DscHujat, DscBolim, DscTolov, DscMalumot




        
class BakalavrHujatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakalavrHujat
        fields = '__all__'


class BakalavrBolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakalavrBolim
        fields = '__all__'


class BakalavrTolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakalavrTolov
        fields = '__all__'


class BakalavrMalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakalavrMalumot
        fields = '__all__'





        
class MagistrHujatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagistrHujat
        fields = '__all__'


class MagistrBolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagistrBolim
        fields = '__all__'


class MagistrTolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagistrTolov
        fields = '__all__'


class MagistrMalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagistrMalumot
        fields = '__all__'





        
class PhdHujatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdHujat
        fields = '__all__'


class PhdBolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdBolim
        fields = '__all__'


class PhdTolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdTolov
        fields = '__all__'


class PhdMalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdMalumot
        fields = '__all__'





        
class DscHujatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DscHujat
        fields = '__all__'


class DscBolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = DscBolim
        fields = '__all__'


class DscTolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = DscTolov
        fields = '__all__'


class DscMalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DscMalumot
        fields = '__all__'




