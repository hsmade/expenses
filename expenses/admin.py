from django.contrib import admin
from .models import *


class DepositInline(admin.TabularInline):
    model = Deposit
    extra = 0


class WithdrawalInline(admin.TabularInline):
    model = Withdrawal
    extra = 0


class MonthAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic info', {'fields': ['year', 'month']})
    ]
    inlines = [DepositInline, WithdrawalInline]

admin.site.register(Month, MonthAdmin)
# admin.site.register(Deposit)
# admin.site.register(Withdrawal)
admin.site.register(WithdrawalType)
admin.site.register(DepositType)
admin.site.register(Reservation)

