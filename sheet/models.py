from django.db import models
import datetime
from django.core.validators import (RegexValidator,
                                    MaxValueValidator,
                                    MinValueValidator)

# Create your models here.
ph_err_msg = 'Length has to be 10'


class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=200,
                            help_text="Enter product name")

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(primary_key=True, max_length=100,
                            help_text="Enter customer name")
    location = models.CharField(max_length="500",
                                help_text="Address/Location"),
    phone = models.CharField(validators=[RegexValidator(regex='^.{10}$',
                                                        message=ph_err_msg,
                                                        code='nomatch')],
                             max_length=10)
    description = models.CharField(max_length=500,
                                   help_text="Enter any note about customer",
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    Dozen = 'Dozen'
    Pieces = 'Dozen'
    ORDER_UNIT = (
        (Dozen, 'Dozen'),
        (Pieces, 'Pieces')
    )
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL,
                                 null=True)
    product = models.ForeignKey('Product',
                                on_delete=models.SET_NULL,
                                null=True)
    date = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(choices=ORDER_UNIT, max_length=15, default=Dozen)
    price = models.IntegerField(default=0)

    def __str__(self):
        return '[{0}] -> {1} {2} of {3} @ {4} INR'.format(self.customer,
                                                     self.quantity,
                                                     self.unit,
                                                     self.product,
                                                     self.price)


class Taxation(models.Model):
    Taxable = 'Taxable'
    Non_Taxable = 'Non_Taxable'
    TAXATION_OPTIONS = (
        (Taxable, 'Taxable'),
        (Non_Taxable, 'Non-Taxable')
    )

    type_of_order = models.CharField(max_length=15,
                                     choices=TAXATION_OPTIONS)
    tax_percentage = models.FloatField(default=0,
                                         validators=[MaxValueValidator(100),
                                                     MinValueValidator(0)])
    description = models.CharField(max_length=500,
                                   help_text="Enter any note about this entry",
                                   null=True,
                                   blank=True)

    def __str__(self):
        return '{0} @{1}%\n{2}'.format(self.type_of_order,
                                       self.tax_percentage,
                                       self.description)
