from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from .models import IncomeCategory, Income, Expense, Asset, Liability, ExpenseCategory, AssetCategory, LiabilityCategory, Target, TargetWallet



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name','phone_no']



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name','phone_no']

######################################################################################################################

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id', 'category_name']


class IncomeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    # income_category_id = serializers.IntegerField()
    class Meta:
        model = Income
        fields = ['id','user_id','income_note', 'income_amount', 'income_date', 'income_category']

    def create(self,validated_data):
        # print('here')
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        # print(validated_data)
        Income_instance=Income.objects.create(**validated_data)
        print(Income_instance)
        return Income_instance

##############################################################################################################

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'category_name']


class ExpenseSerializer(serializers.ModelSerializer):
    user_id =  serializers.IntegerField(read_only = True)
    # expense_category_id = serializers.IntegerField()
    class Meta:
        model = Expense
        fields = ['id','user_id', 'expense_note', 'expense_amount', 'expense_date','expense_category'] # 'expense_category_id',

    def create(self,validated_data):
        print('here')
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        # print(validated_data)
        Expense_instance=Expense.objects.create(**validated_data)
        print(Expense_instance)
        return Expense_instance


#################################################################################################################

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = ['id', 'category_name']



class AssetSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField(read_only = True)
    # asset_category_id = serializers.IntegerField()
    class Meta:
        model = Asset
        fields = ['id','user_id','asset_note', 'asset_amount', 'asset_date', 'asset_category'] # ',

    def create(self,validated_data):
        # print('here')
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        # print(validated_data)
        Asset_instance  =Asset.objects.create(**validated_data)
        print(Asset_instance )
        return Asset_instance 

###################################################################################################################################3

class LiabilityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LiabilityCategory
        fields = ['id', 'category_name']



class LiabilitySerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField(read_only=True)
    # liability_category_id = serializers.IntegerField()
    class Meta:
        model = Liability
        fields = ['id' , 'user_id','liability_note', 'liability_amount', 'liability_date','liability_category'] # 'liability_category_id'


    def create(self,validated_data):
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        Liability_instance  =Liability.objects.create(**validated_data)
        print(Liability_instance )
        return Liability_instance 
    

################################################################################################################
class TargetWalletSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = TargetWallet
        fields = ['id', 'amount', 'user_id']

    def create(self,validated_data):
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        TargetWallet_instance  =TargetWallet.objects.create(**validated_data)
        print(TargetWallet_instance )
        return TargetWallet_instance 


class TargetSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Target
        fields = ['id', 'user_id','target_name', 'current_amount', 'target_amount', 'target_add_date', 'target_deadline', 'target_status', 'target_priority']

    def create(self,validated_data):
        user_id = self.context.get('user_id')
        validated_data['user_id'] = user_id
        Target_instance  =Target.objects.create(**validated_data)
        print(Target_instance )
        return Target_instance 