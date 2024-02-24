from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator # input validation

# Create your models here.

class User(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True, null=True)


class IncomeCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'


class Income(models.Model):
    income_note = models.CharField(max_length  = 255)
    income_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    income_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    income_category = models.ForeignKey(IncomeCategory, on_delete = models.PROTECT)


class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'
    

class Expense(models.Model):
    expense_note = models.CharField(max_length  = 255)
    expense_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    expense_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete = models.PROTECT)


class AssetCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'


class Asset(models.Model):
    asset_note = models.CharField(max_length  = 255)
    asset_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    asset_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    asset_category = models.ForeignKey(AssetCategory, on_delete = models.PROTECT)


class LiabilityCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'


class Liability(models.Model):
    liability_note = models.CharField(max_length  = 255)
    liability_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    liability_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    liability_category = models.ForeignKey(LiabilityCategory, on_delete = models.PROTECT)
    
###############################################################################################
# class Target(models.Model):
#     target_name = models.CharField(max_length = 255)
#     target_set_date = models.DateField(auto_now=True)
#     target_completion_date = models.DateField(auto_now=False)
#     completed = 'COMP'
#     incomplete = 'INCP'
#     target_choices = [(completed, 'completed'),
#                       (incomplete, 'incomplete')]
#     target_status  = models.CharField(max_length =4, choices = target_choices, default = incomplete)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)

#     def __str__(self):
#         return f'{self.target_name}'


# class TargetWallet(models.Model):
#     added_date = models.DateTimeField()
#     added_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
#     target = models.ForeignKey(Target, on_delete = models.CASCADE)

#########################################################################################################################

class TargetWallet(models.Model):
    added_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(1)])
    # target = models.ForeignKey(Target, on_delete=models.CASCADE)

    def add_amount(self, amount):
        self.total_amount += amount
        self.save()

    def __str__(self):
        return f"TargetWallet - Total Amount: {self.total_amount}"


class Target(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    target_name = models.CharField(max_length = 255)
    target_set_date = models.DateField(auto_now=True)
    target_completion_date = models.DateField(auto_now=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    amount_needed = models.DecimalField(max_digits=10, decimal_places=2)
    target_wallet = models.ForeignKey(TargetWallet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)