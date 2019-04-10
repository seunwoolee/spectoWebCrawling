from django.db import models


class ControllerGroup(models.Model):
    Date = models.CharField(max_length=30)
    Time = models.CharField(max_length=30)


class CycleDataGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Present_heads_group_1 = models.CharField(max_length=30)
    Life_Days = models.CharField(max_length=30)


class BirdsGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Present_heads_group_1 = models.CharField(max_length=30)
    Total_removed_heads_group_1 = models.CharField(max_length=30)
    Total_added_heads_group_1 = models.CharField(max_length=30)
    Total_dead_heads_group_1 = models.CharField(max_length=30)


class ProbesGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=30)
    Internal_humidity = models.CharField(max_length=30)
    External_temperature = models.CharField(max_length=30)
    External_humidity = models.CharField(max_length=30)
    Pressure = models.CharField(max_length=30)
    Fan_temperature_1 = models.CharField(max_length=30)
    Fan_temperature_2 = models.CharField(max_length=30)
    Fan_temperature_3 = models.CharField(max_length=30)
    Fan_temperature_4 = models.CharField(max_length=30)
    Fan_temperature_5 = models.CharField(max_length=30)
    Fan_temperature_6 = models.CharField(max_length=30)
    Window_temperature_1 = models.CharField(max_length=30)
    Internal_Temperature_Minimum_Daily = models.CharField(max_length=30)
    Internal_Temperature_Average_Daily = models.CharField(max_length=30)
    Internal_Temperature_Maximum_Daily = models.CharField(max_length=30)
    Internal_Humidity_Minimum_Daily = models.CharField(max_length=30)
    Internal_Humidity_Average_Daily = models.CharField(max_length=30)
    Internal_Humidity_Maximum_Daily = models.CharField(max_length=30)
    External_Temperature_Minimum_Daily = models.CharField(max_length=30)
    External_Temperature_Average_Daily = models.CharField(max_length=30)
    External_Temperature_Maximum_Daily = models.CharField(max_length=30)
    External_Humidity_Minimum_Daily = models.CharField(max_length=30)
    External_Humidity_Average_Daily = models.CharField(max_length=30)
    External_Humidity_Maximum_Daily = models.CharField(max_length=30)


class FanGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=30)
    Internal_humidity = models.CharField(max_length=30)
    External_temperature = models.CharField(max_length=30)
    External_humidity = models.CharField(max_length=30)
    Fan_Step = models.CharField(max_length=30)
    Internal_temperature = models.CharField(max_length=30)
    Set_Fan = models.CharField(max_length=30)
    change_set_minimum_fan = models.CharField(max_length=30)
    change_set_fan_night = models.CharField(max_length=30)
    change_set_fan_humidity = models.CharField(max_length=30)
    Air_total_farm = models.CharField(max_length=30)
    Air_supplied = models.CharField(max_length=30)
    Air_Unit_1 = models.CharField(max_length=30)
    Delivered_percentage = models.CharField(max_length=30)


class CoolingGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=30)
    Internal_humidity = models.CharField(max_length=30)
    Cooling_satus_1 = models.CharField(max_length=30)
    Set_Cooling_1 = models.CharField(max_length=30)
    Block_max_humidity_cooling_1 = models.CharField(max_length=30)


class FoodGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Total_food_delivered = models.CharField(max_length=30)
    Today_feed_distributed = models.CharField(max_length=30)
    Food_head = models.CharField(max_length=30)


class WaterGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Total_water_distributed = models.CharField(max_length=30)
    Today_water_distributed = models.CharField(max_length=30)
    Water_head = models.CharField(max_length=30)
    Block_water_counter = models.CharField(max_length=30)


