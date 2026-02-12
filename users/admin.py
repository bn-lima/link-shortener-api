from django.contrib import admin
from .models import Account, ResetToken

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']
    search_fields = ['email', 'username']

@admin.register(ResetToken)
class ResetTokenAdmin(admin.ModelAdmin):
    list_display = ["user", "active", "key", "expiration"]
    readonly_fields = ["user", "active", "key", "expiration"]