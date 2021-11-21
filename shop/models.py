from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.

STATE = (('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
         ('Andhra Pradesh', 'Andhra Pradesh'),
         ('Arunachal Pradesh', 'Arunachal Pradesh'),
         ('Assam', 'Assam'),
         ('Bihar', 'Bihar'),
         ('Chandigarh', 'Chandigarh'),
         ('Chattisgarh', 'Chattisgarh'),
         ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
         ('Daman and Diu', 'Daman and Diu'),
         ('Delhi', 'Delhi'),
         ('Goa', 'Goa'),
         ('Gujarat', 'Gujarat'),
         ('Haryana', 'Haryana'),
         ('Himachal Pradesh', 'Himachal Pradesh'),
         ('Jammu and Kashmir', 'Jammu and Kashmir'),
         ('Jharkhand', 'Jharkhand'),
         ('Karnataka', 'Karnataka'),
         ('Kerala', 'Kerala'),
         ('Lakshadweep', 'Lakshadweep'),
         ('Madhya Pradesh', 'Madhya Pradesh'),
         ('Maharashtra', 'Maharashtra'),
         ('Manipur', 'Manipur'),
         ('Meghalaya', 'Meghalaya'),
         ('Mizoram', 'Mizoram'),
         ('Nagaland', 'Nagaland'),
         ('Odisha', 'Odisha'),
         ('Puducherry', 'Puducherry'),
         ('Punjab', 'Punjab'),
         ('Rajasthan', 'Rajasthan'),
         ('Sikkim', 'Sikkim'),
         ('Tamil Nadu', 'Tamil Nadu'),
         ('Telangana', 'Telangana'),
         ('Tripura', 'Tripura'),
         ('Uttar Pradesh', 'Uttar Pradesh'),
         ('Uttarakhand', 'Uttarakhand'),
         ('West Bengal', 'West Bengal'),
         )


class Customerdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    Pincode = models.IntegerField()
    State = models.CharField(choices=STATE, max_length=100)

    def __str__(self):
        return str(self.id)


PRODUCT_CHOICES = (('KC', 'Kitchen Cookware'),
                   ('DEO', 'Deodrants'),
                   ('BM', 'Blended Masalas'))

STOCK_CHOICES = (('IS', 'In-Stock'), ('OS', 'Out of Stock'), ('LS',
                 'Less Products'))


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    category = models.CharField(choices=PRODUCT_CHOICES, max_length=4)
    stock_condition = models.CharField(choices=STOCK_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='images')
    stock_left = models.PositiveIntegerField()
    product_description = models.TextField(
        default='Description about the Product here')
    product_cutprice = models.FloatField(default=10)
    product_offers = models.TextField(
        max_length=1000, default='Offers about the Product here')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_indcost(self):
        return self.quantity * self.product.product_price


STATUS = (
    ('Order Placed', 'Order Placed'),
    ('Dispatched', 'Dispatched'),
    ('On The Way', 'On The Way'),
    ('Out for Delivery', 'Out For Delivery'),
    ('Delivered', 'Delivered'),
    ('Order Cancelled', 'Order Cancelled')
)


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customerdetails, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=100, choices=STATUS, default='Order Placed')

    @property
    def total_indcost(self):
        return self.quantity * self.product.product_price


RATING = (
    ('1-star', '1-star'),
    ('2-star', '2-star'),
    ('3-star', '3-star'),
    ('4-star', '4-star'),
    ('5-star', '5-star'),
)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=200)
    review_detail = models.TextField()
    rating = models.CharField(
        max_length=100, choices=RATING)
    reviewer_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product)
