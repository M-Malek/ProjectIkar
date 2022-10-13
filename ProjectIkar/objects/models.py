from django.db import models


# Create your models here.
# Main object:
class Object(models.Model):
    object_name = models.CharField(max_length=300)
    # Object types:
    wind_farm = 'WF'
    photovoltaic_farm = 'PV'
    object_list = [(wind_farm, 'Wind Farm'), (photovoltaic_farm, 'Photovoltaic Power Plant')]
    object_type = models.CharField(max_length=2, choices=object_list, default=wind_farm)


# Object location
class Location(models.Model):
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    object_city = models.CharField(max_length=300)
    object_voivodeship = models.CharField(max_length=350)
    object_cords = models.CharField(max_length=100)


# Device types
class PhotovoltaicPanel(models.Model):
    panel_producer = models.CharField(max_length=300)


# Inverter data
class Inverter(models.Model):
    pass


# Wind turbine data
class WindTurbine(models.Model):
    pass


# Object devices:
class Devices:
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    object_inverter = models.ForeignKey(Inverter, on_delete=models.CASCADE)
    object_photo = models.ForeignKey(PhotovoltaicPanel, on_delete=models.CASCADE)


# # Connection condition given by electric grid operator
# class ConnectionConditions(models.Model):
#     pass
