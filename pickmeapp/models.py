from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    per_day_rate = models.DecimalField(max_digits=10, decimal_places=2)
    seating_capacity = models.IntegerField()
    additional_km_rate = models.DecimalField(max_digits=10, decimal_places=2)
    allow_daily = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="vehicle_images/")

    def __str__(self):
        return f"Image for {self.vehicle.name}"





from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='package_images/', null=True, blank=True)  # New field for images

    def __str__(self):
        return self.name





from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/')
    review = models.TextField()

    def __str__(self):
        return self.name
