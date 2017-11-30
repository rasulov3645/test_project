from django.contrib import admin

from  .models import *

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subcriber._meta.fields]

    # exclude = ["email"]     # исключаем email.
    # fields = ["name"]    # то, есть что мы показываем

    # list_filter = ("name", )    # фильтируем по name в admin понели
    # list_filter = ["email", ]   # фильтируем по еmail1

    # input в котором можно вводить какой то значение и она будеть находить
    search_fields = ["name", "email"]


    # list_display = []
    # inlines = []
    # fields = ["email"]    # отображается только email.
    # exclude = ["email"]   # исключаем email.
    # list_filter = ()
    # search_fields = []

    class Meta:
        model = Subcriber



admin.site.register(Subcriber, SubscriberAdmin)


