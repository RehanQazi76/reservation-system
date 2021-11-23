from django.contrib import admin
from .models import Month, Name, Task,Date
# Register your models here.
admin.site.register(Task)
admin.site.register(Name)
admin.site.register(Date)
admin.site.register(Month)