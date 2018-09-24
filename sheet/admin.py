from django.contrib import admin
from sheet.models import (Product,
                          Customer,
                          Taxation,
                          Order)

# Register your models here.
# admin.site.register(MyModelName)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Taxation)
admin.site.register(Order)
