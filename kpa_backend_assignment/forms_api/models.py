# forms_api/models.py

from django.db import models

class BmbcChecksheet(models.Model):
    adjusting_tube = models.CharField(max_length=100)
    cylinder_body = models.CharField(max_length=100)
    piston_trunnion = models.CharField(max_length=100)
    plunger_spring = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    axle_guide = models.CharField(max_length=100)
    bogie_frame_condition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolster_suspension_bracket = models.CharField(max_length=100)
    lower_spring_seat = models.CharField(max_length=100)

class BogieDetails(models.Model):
    bogie_no = models.CharField(max_length=50)
    date_of_ioh = models.DateField()
    deficit_components = models.CharField(max_length=255)
    incoming_div_and_date = models.CharField(max_length=100)
    maker_year_built = models.CharField(max_length=100)

class BogieChecksheetForm(models.Model):
    form_number = models.CharField(max_length=100)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bmbc_checksheet = models.OneToOneField(BmbcChecksheet, on_delete=models.CASCADE)
    bogie_checksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bogie_details = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)

class WheelSpecification(models.Model):
    wheel_type = models.CharField(max_length=100)
    diameter = models.FloatField()
    rim_thickness = models.FloatField()

    def __str__(self):
        return f"{self.wheel_type} - {self.diameter}mm"
