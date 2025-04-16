from djongo import models  # Use djongo's models for MongoDB

class Product(models.Model):
    _id = models.ObjectIdField()  # MongoDB object ID
    name = models.CharField(max_length=100)  # Product name
    description = models.TextField()  # Product description
    price = models.FloatField()  # Product price
    category = models.CharField(max_length=50)  # Product category
    
    def __str__(self):
        return self.name  # Return the product name when the object is printed
