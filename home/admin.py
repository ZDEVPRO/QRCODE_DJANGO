from django.contrib import admin
from home.models import Qrcode


class QrcodeAdmin(admin.ModelAdmin):
    list_display = ['text', 'type']


admin.site.register(Qrcode, QrcodeAdmin)
