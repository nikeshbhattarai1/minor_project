from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.urls import reverse
from django.utils.html import urlencode, format_html
from django.db.models.aggregates import Count
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'income_list','expense_list', 'asset_list', 'liability_list', 'target_list']

    def income_list(self, user):
        url = reverse('admin:core_income_changelist')+ '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href = "{}">{}</a>', url, user.income_list) #display with link 
    
    def expense_list(self, user):
        url = reverse('admin:core_expense_changelist')+ '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href = "{}">{}</a>', url, user.expense_list) #display with link 
    
    def asset_list(self, user):
        url = reverse('admin:core_asset_changelist')+ '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href = "{}">{}</a>', url, user.asset_list) #display with link 
    
    def liability_list(self, user):
        url = reverse('admin:core_liability_changelist')+ '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href = "{}">{}</a>', url, user.liability_list) #display with link 
    
    def target_list(self, user):
        url = reverse('admin:core_target_changelist')+ '?' + urlencode({'user__id': str(user.id)})
        return format_html('<a href = "{}">{}</a>', url, user.target_list) #display with link 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            income_list = Count('income', distinct=True),
            expense_list  = Count('expense', distinct=True),
            asset_list = Count('asset', distinct=True),
            liability_list = Count('liability', distinct=True),
            target_list = Count('target', distinct=True)
        )
    

@admin.register(models.IncomeCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','category_name', 'income_list']
    
    def income_list(self, incomecategory):
        url = reverse('admin:core_income_changelist')+ '?' + urlencode({'income_category__id': str(incomecategory.id)})
        return format_html('<a href = "{}">{}</a>', url, incomecategory.income_list) #display with link 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            income_list = Count('income', distinct=True)
        )
    

@admin.register(models.Income)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'income_note', 'income_amount', 'income_date']
    list_filter = ['user', 'income_category']

    def user(self, obj):
        return obj.user.username if obj.user else ''
    

@admin.register(models.ExpenseCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','category_name', 'category_list']

    def category_list(self, expense_category):
        url = reverse('admin:core_expense_changelist')+ '?' + urlencode({'expense_category__id': str(expense_category.id)})
        return format_html('<a href = "{}">{}</a>', url, expense_category.category_list) #display with link 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            category_list = Count('expense', distinct=True)
        )


@admin.register(models.Expense)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'expense_note', 'expense_amount', 'expense_date']
    list_filter = ['user', 'expense_category']

    def user(self, obj):
        return obj.user.username if obj.user else ''

@admin.register(models.AssetCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','category_name', 'category_list']

    def category_list(self, asset_category):
        url = reverse('admin:core_asset_changelist')+ '?' + urlencode({'asset_category__id': str(asset_category.id)})
        return format_html('<a href = "{}">{}</a>', url, asset_category.category_list) #display with link 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            category_list = Count('asset', distinct=True)
        )


@admin.register(models.Asset)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'asset_note', 'asset_amount', 'asset_date']
    list_filter = ['user', 'asset_category']

    def user(self, obj):
        return obj.user.username if obj.user else ''


@admin.register(models.LiabilityCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_list']

    def category_list(self, liability_category):
        url = reverse('admin:core_liability_changelist')+ '?' + urlencode({'liability_category__id': str(liability_category.id)})
        return format_html('<a href = "{}">{}</a>', url, liability_category.category_list) #display with link 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            category_list = Count('liability', distinct=True)
        )


@admin.register(models.Liability)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'liability_note', 'liability_amount', 'liability_date']
    list_filter = ['user', 'liability_category']

    def user(self, obj):
        return obj.user.username if obj.user else ''


# @admin.register(models.Target)
# class TargetAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'target_name', 'priority', 'target_set_date', 'target_completion_date', 'target_wallet_count']
#     list_filter = ['user']

#     def target_wallet_count(self, obj):
#         return obj.target_wallet_count  # This assumes you have annotated it in the queryset

#     target_wallet_count.short_description = 'Target Wallet Count'  # Custom column name

#     def user(self, obj):
#         return obj.user.username if obj.user else ''

# @admin.register(models.TargetWallet)
# class TargetWalletAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'target', 'added_date', 'total_amount']
#     list_filter = ['target']

#     def target(self, obj):
#         return obj.target.target_name if obj.target else ''

#     def user(self, obj):
#         return obj.target.user.username if obj.target and obj.target.user else ''
    
# @admin.register(models.TargetWallet)
# class TargetWalletAdmin(admin.ModelAdmin):
#     list_display = ['id', 'added_date', 'total_amount']
#     search_fields = ['id'] 

# @admin.register(models.Target)
# class TargetAdmin(admin.ModelAdmin):
#     list_display = ['id', 'target_name', 'priority', 'target_set_date', 'target_completion_date', 'amount_needed', 'user']
#     search_fields = ['id', 'target_name', 'user__username']  
#     list_filter = ['priority', 'user']

#     def target_wallet_total_amount(self, obj):
#         return obj.target_wallet.total_amount if obj.target_wallet else None

#     target_wallet_total_amount.short_description = 'Target Wallet Total Amount' 

#     def user_username(self, obj):
#         return obj.user.username if obj.user else None

#     user_username.short_description = 'User' 
    

@admin.register(models.Target)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'target_name', 'current_amount', 'target_amount', 'target_add_date', 'target_deadline', 'target_status', 'target_priority']
    list_filter = ['user']

    def user(self, obj):
        return obj.user.username if obj.user else ''


@admin.register(models.TargetWallet)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount']
    list_filter = ['user']
    
    def user(self,obj):
        return obj.target.user.username if obj.target.user else ''