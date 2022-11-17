from django.contrib import admin
from  second_app.models import User


# Register your models here.
# admin.site.register(User)

@admin.register(User)
class AdminMyForm(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id']