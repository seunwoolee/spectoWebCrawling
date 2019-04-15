from django.db import models


class ControllerGroup(models.Model):
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)

    def __str__(self):
        return "{}{}".format(self.Date, self.Time)


class CycleDataGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Present_heads_group_1 = models.CharField(max_length=100)
    Life_Days = models.CharField(max_length=100)
    Set_m3hkg = models.CharField(max_length=100)

    def __str__(self):
        return "{}_Present_heads_group_1: {}_Life_Days: {}"\
            .format(self.DateTime, self.Present_heads_group_1, self.Life_Days)


class BirdsGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Present_heads_group_1 = models.CharField(max_length=100)
    Total_removed_heads_group_1 = models.CharField(max_length=100)
    Total_added_heads_group_1 = models.CharField(max_length=100)
    Total_dead_heads_group_1 = models.CharField(max_length=100)

    def __str__(self):
        return "{}_Present_heads_group_1: {}_Life_Days: {}"\
            .format(self.DateTime, self.Present_heads_group_1, self.Total_dead_heads_group_1)


class ProbesGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=100)
    Internal_humidity = models.CharField(max_length=100)
    External_temperature = models.CharField(max_length=100)
    External_humidity = models.CharField(max_length=100)
    Pressure = models.CharField(max_length=100)
    Fan_temperature_1 = models.CharField(max_length=100)
    Fan_temperature_2 = models.CharField(max_length=100)
    Fan_temperature_3 = models.CharField(max_length=100)
    Fan_temperature_4 = models.CharField(max_length=100)
    Fan_temperature_5 = models.CharField(max_length=100)
    Fan_temperature_6 = models.CharField(max_length=100)
    Window_temperature_1 = models.CharField(max_length=100)
    Internal_Temperature_Minimum_Daily = models.CharField(max_length=100)
    Internal_Temperature_Average_Daily = models.CharField(max_length=100)
    Internal_Temperature_Maximum_Daily = models.CharField(max_length=100)
    Internal_Humidity_Minimum_Daily = models.CharField(max_length=100)
    Internal_Humidity_Average_Daily = models.CharField(max_length=100)
    Internal_Humidity_Maximum_Daily = models.CharField(max_length=100)
    External_Temperature_Minimum_Daily = models.CharField(max_length=100)
    External_Temperature_Average_Daily = models.CharField(max_length=100)
    External_Temperature_Maximum_Daily = models.CharField(max_length=100)
    External_Humidity_Minimum_Daily = models.CharField(max_length=100)
    External_Humidity_Average_Daily = models.CharField(max_length=100)
    External_Humidity_Maximum_Daily = models.CharField(max_length=100)


class FanGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=100)
    External_temperature = models.CharField(max_length=100)
    Internal_humidity = models.CharField(max_length=100)
    External_humidity = models.CharField(max_length=100)
    Fan_Step = models.CharField(max_length=100)
    Internal_temperature = models.CharField(max_length=100)
    Set_Fan = models.CharField(max_length=100)
    change_set_minimum_fan_external = models.CharField(max_length=100)
    change_set_fan_night = models.CharField(max_length=100)
    change_set_fan_humidity = models.CharField(max_length=100)
    Air_total_farm = models.CharField(max_length=100)
    Air_supplied = models.CharField(max_length=100)
    Air_Unit_1 = models.CharField(max_length=100)
    Delivered_percentage = models.CharField(max_length=100)
    Ventilation_minimum_calculated = models.CharField(max_length=100)
    Set_m3hkg = models.CharField(max_length=100)
    Set_minimum_fan = models.CharField(max_length=100)
    Block_maximum_fan = models.CharField(max_length=100)
    Block_Max_external_fan = models.CharField(max_length=100)
    Block_max_step_external_temp = models.CharField(max_length=100)
    Block_minimum_fan = models.CharField(max_length=100)
    Block_forcing_refresh = models.CharField(max_length=100)
    Block_refresh_for_humidity = models.CharField(max_length=100)
    Block_rotation_fan = models.CharField(max_length=100)
    Block_rotation_replacements = models.CharField(max_length=100)
    Fan_Stop_for_heating_On = models.CharField(max_length=100)
    Correction_factor = models.CharField(max_length=100)
    Air_minimum = models.CharField(max_length=100)
    Air_renew = models.CharField(max_length=100)
    Air_theoretical_supplied = models.CharField(max_length=100)


class CoolingGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=100)
    Internal_humidity = models.CharField(max_length=100)
    Cooling_satus_1 = models.CharField(max_length=100)
    Set_Cooling_1 = models.CharField(max_length=100)
    Block_max_humidity_cooling_1 = models.CharField(max_length=100)


class WindowsGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Internal_average_temperature = models.CharField(max_length=100)
    Internal_humidity = models.CharField(max_length=100)
    External_temperature = models.CharField(max_length=100)
    External_humidity = models.CharField(max_length=100)
    Pressure = models.CharField(max_length=100)
    Set_pressure = models.CharField(max_length=100)
    change_set_pressure_for_external_temperature = models.CharField(max_length=100)
    Window_temperature_1 = models.CharField(max_length=100)
    Set_Window_1 = models.CharField(max_length=100)
    Window_lap_position_1 = models.CharField(max_length=100)
    Window_Potentiometer_1 = models.CharField(max_length=100)
    Window_Potentiometer_2 = models.CharField(max_length=100)
    Window_position_2 = models.CharField(max_length=100)
    Set_depression_meter_Window_3 = models.CharField(max_length=100)
    Block_action_window_open = models.CharField(max_length=100)
    Block_action_window_closed = models.CharField(max_length=100)
    Block_Summer_Window = models.CharField(max_length=100)
    Block_Winter_Window = models.CharField(max_length=100)
    Block_Window_open_for_cooling = models.CharField(max_length=100)
    Block_Window_closed_for_cooling = models.CharField(max_length=100)
    Block_min_open_windows_depression_meter = models.CharField(max_length=100)
    Pressure_set_variation_for_external_temp_Block = models.CharField(max_length=100)


class AirUnit1Group(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Dew_temperature = models.CharField(max_length=100)
    Air_Unit_1 = models.CharField(max_length=100)
    Run_time_turbine_U1 = models.CharField(max_length=100)


class FoodGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Total_food_delivered = models.CharField(max_length=100)
    Todays_feed_distributed = models.CharField(max_length=100)
    Food_head = models.CharField(max_length=100)


class ChartsGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Status_Trolleys_Group_1 = models.CharField(max_length=100)
    Run_number_group_1 = models.CharField(max_length=100)
    Cargo_number_group_1 = models.CharField(max_length=100)


class CoilsGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Status_Coil_1 = models.CharField(max_length=100)
    Block_Coil_1 = models.CharField(max_length=100)


class SilosGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Total_weight_silos = models.CharField(max_length=100)
    Weight_Silo_1 = models.CharField(max_length=100)
    Status_Silo_1 = models.CharField(max_length=100)
    Load_Today_Silo_1 = models.CharField(max_length=100)
    Distributed_Today_Silo_1 = models.CharField(max_length=100)
    Silo_1_Level_1 = models.CharField(max_length=100)
    Silo_1_Level_2 = models.CharField(max_length=100)
    Weight_Silo_2 = models.CharField(max_length=100)
    Status_Silo_2 = models.CharField(max_length=100)
    Load_Today_Silo_2 = models.CharField(max_length=100)
    Distributed_Today_Silo_2 = models.CharField(max_length=100)
    Weight_Silo_3 = models.CharField(max_length=100)
    Status_Silo_3 = models.CharField(max_length=100)
    Load_Today_Silo_3 = models.CharField(max_length=100)
    Distributed_Today_Silo_3 = models.CharField(max_length=100)


class WaterGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Total_water_distributed = models.CharField(max_length=100)
    Todays_water_distributed = models.CharField(max_length=100)
    Water_head = models.CharField(max_length=100)
    Block_water_counter = models.CharField(max_length=100)


class EggsCollectionGroup(models.Model):
    DateTime = models.ForeignKey(ControllerGroup, on_delete=models.CASCADE)
    Meters_remaining_group_1 = models.CharField(max_length=100)
    Percentage_collection_group_1 = models.CharField(max_length=100)
    Collection_end_time_group_1 = models.CharField(max_length=100)
    Collection_on_time_group_1 = models.CharField(max_length=100)
    Collection_off_time_group_1 = models.CharField(max_length=100)
