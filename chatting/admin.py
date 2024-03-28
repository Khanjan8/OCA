from django.contrib import admin
from chatting.models import user,message,images,report,request,pin,block,feedback,admin2

admin.site.register(user)
admin.site.register(message)
admin.site.register(images)
admin.site.register(report)
admin.site.register(request)
admin.site.register(pin)
admin.site.register(block)
admin.site.register(feedback)
admin.site.register(admin2)
