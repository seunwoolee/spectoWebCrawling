from django.contrib import admin
from .models import *


@admin.register(ProbesGroup)
class ProbesGroupAdmin(admin.ModelAdmin):
    list_display = ['DateTime', 'Internal_average_temperature', 'Internal_humidity', 'External_temperature',
                    'External_humidity', 'Pressure', 'Fan_temperature_1', 'Fan_temperature_2', 'Fan_temperature_3',
                    'Fan_temperature_4', 'Fan_temperature_5', 'Fan_temperature_6', 'Window_temperature_1',
                    'Internal_Temperature_Minimum_Daily', 'Internal_Temperature_Average_Daily',
                    'Internal_Temperature_Maximum_Daily', 'Internal_Humidity_Minimum_Daily',
                    'Internal_Humidity_Average_Daily', 'Internal_Humidity_Maximum_Daily',
                    'External_Temperature_Minimum_Daily', 'External_Temperature_Average_Daily',
                    'External_Temperature_Maximum_Daily', 'External_Humidity_Minimum_Daily',
                    'External_Humidity_Average_Daily', 'External_Humidity_Maximum_Daily']
    model = ProbesGroup


admin.site.register(ControllerGroup)
admin.site.register(CycleDataGroup)
admin.site.register(BirdsGroup)
# admin.site.register(ProbesGroup)
admin.site.register(FanGroup)
admin.site.register(CoolingGroup)
admin.site.register(WindowsGroup)
admin.site.register(AirUnit1Group)
admin.site.register(FoodGroup)
admin.site.register(ChartsGroup)
admin.site.register(CoilsGroup)
admin.site.register(SilosGroup)
admin.site.register(WaterGroup)
admin.site.register(EggsCollectionGroup)
admin.site.register(Egg)
