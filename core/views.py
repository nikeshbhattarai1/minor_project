# Create your views here.
from decimal import Decimal
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, DestroyAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db import transaction
from django.db.models import F 
from django.core.serializers import serialize
from . import models
from datetime import datetime

from django.http import JsonResponse
from django.contrib import messages


from . models import Income, IncomeCategory, Expense, ExpenseCategory, Asset,\
                    AssetCategory, Liability, LiabilityCategory, TargetWallet
from . serializers import IncomeCategorySerializer, IncomeSerializer,ExpenseSerializer,\
                            AssetSerializer, LiabilitySerializer, ExpenseCategorySerializer,\
                            AssetCategorySerializer, LiabilityCategorySerializer, TargetWalletSerializer


###########################################################################################################

class IncomeCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeCategory.objects.all()
    
    def get_serializer_class(self):
        return IncomeCategorySerializer



class IncomeCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return IncomeCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return IncomeCategorySerializer



class IncomeView(ListCreateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        # print("VIEW")
        return IncomeSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class IncomeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Income.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return IncomeSerializer
    
####################################################################################################################

class ExpenseCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseCategory.objects.all()
    
    def get_serializer_class(self):
        return ExpenseCategorySerializer



class ExpenseCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ExpenseCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return ExpenseCategorySerializer



class ExpenseView(ListCreateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        # print("VIEW")
        return ExpenseSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Expense.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return ExpenseSerializer
    
######################################################################################################################

class AssetCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AssetCategory.objects.all()
    
    def get_serializer_class(self):
        return AssetCategorySerializer



class AssetCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return AssetCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return AssetCategorySerializer



class AssetView(ListCreateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
         return Asset.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return AssetSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssetDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Asset.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return AssetSerializer
    
########################################################################################################################

class LiabilityCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LiabilityCategory.objects.all()
    
    def get_serializer_class(self):
        return LiabilityCategorySerializer



class LiabilityCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return LiabilityCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return LiabilityCategorySerializer



class LiabilityView(ListCreateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Liability.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return LiabilitySerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):    
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LiabilityDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Liability.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return LiabilitySerializer
    

##################################################################################################################

class TotalIncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount')) or 0
        return Response(total_income)
    
class TotalExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income_aggregated = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount'))
        total_income = total_income_aggregated['total_income'] if total_income_aggregated['total_income'] is not None else Decimal('0')
        
        total_expense_aggregated = Expense.objects.filter(user_id=self.request.user.id).aggregate(total_expense=Sum('expense_amount'))
        total_expense = total_expense_aggregated['total_expense'] if total_expense_aggregated['total_expense'] is not None else Decimal('0')
        
        expense_notification =''
        if total_income < total_expense:
            expense_notification = "Expense exceeded Income"
        elif total_expense > Decimal('100000'):
            expense_notification = "Expense More than Threshold"
            
        return Response({"total_expense": total_expense, "expense_notification":expense_notification})
    

class TotalAssetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_asset = Asset.objects.filter(user_id=self.request.user.id).aggregate(total_asset=Sum('asset_amount')) or 0
        return Response(total_asset)
    

class TotalLiabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_liability = Liability.objects.filter(user_id=self.request.user.id).aggregate(total_liability=Sum('liability_amount')) or 0
        return Response(total_liability)

##############################################################################################################################

class BalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount'))['total_income'] or 0
        total_expense = Expense.objects.filter(user_id=self.request.user.id).aggregate(total_expense=Sum('expense_amount'))['total_expense'] or 0
        total_liability = Liability.objects.filter(user_id=self.request.user.id).aggregate(total_liability=Sum('liability_amount'))['total_liability'] or 0
        total_asset = Asset.objects.filter(user_id=self.request.user.id).aggregate(total_asset=Sum('asset_amount'))['total_asset'] or 0
        balance_amount = total_income - total_expense

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "balance_amount": balance_amount,
            "total_assets": total_asset,
            "total_liabilities": total_liability,
        })

############################################################################################################
    
# class HistoryView(APIView):
#     permission_classes = [IsAuthenticated]

    

#     def get(self, request):
#         income_history = Income.objects.filter(user=request.user).values('id','income_amount', 'income_note', 'income_date',"income_category__category_name")
#         expense_history = Expense.objects.filter(user=request.user).values('id','expense_amount', 'expense_note', 'expense_date','expense_category__category_name')
#         liability_history = Liability.objects.filter(user=request.user).values('id','liability_amount', 'liability_note', 'liability_date','liability_category__category_name')
#         asset_history = Asset.objects.filter(user=request.user).values('id','asset_amount', 'asset_note', 'asset_date','asset_category__category_name')
#         combined_history = list(income_history) + list(expense_history) + list(liability_history) + list(asset_history)
#         combined_history_sorted = sorted(combined_history, key=lambda x: x.get('income_date', 
#                                          x.get('expense_date', 
#                                          x.get('liability_date', 
#                                          x.get('asset_date', datetime.min)))), reverse=True)
#         return Response(combined_history_sorted)

######################################################################################################################

class HistoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, entry_id=None):
        if entry_id is not None:
            try:
                income_data = Income.objects.filter(id=entry_id, user=request.user).values('id', 'income_amount', 'income_note', 'income_date', 'income_category__category_name')
                if income_data.exists():
                    return Response(income_data.first())
                else:
                    raise Http404("Income entry not found")
            except Income.DoesNotExist:
                try:
                    expense_data = Expense.objects.get(id=entry_id, user=request.user).values('id', 'expense_amount', 'expense_note', 'expense_date', 'expense_category__category_name')
                    if expense_data.exists():
                        return Response(expense_data.first())
                    else:
                        raise Http404("Expense entry not found")
                except Expense.DoesNotExist:
                    try:
                        liability_data = Liability.objects.get(id=entry_id, user=request.user).values('id', 'liability_amount', 'liability_note', 'liability_date', 'liability_category__category_name')
                        if liability_data.exists():
                            return Response(liability_data.first())
                        else:
                            raise Http404("Liability entry not found")
                    except Liability.DoesNotExist:
                        try:
                            asset_data = Asset.objects.get(id=entry_id, user=request.user).values('id', 'asset_amount', 'asset_note', 'asset_date', 'asset_category__category_name')
                            if asset_data.exists():
                                return Response(asset_data.first())
                            else:
                                raise Http404("Asset entry not found")
                        except Asset.DoesNotExist:
                            raise Http404("History entry not found")

        else:
            income_history = Income.objects.filter(user=request.user).values('id', 'income_amount', 'income_note', 'income_date', 'income_category__category_name')
            expense_history = Expense.objects.filter(user=request.user).values('id', 'expense_amount', 'expense_note', 'expense_date', 'expense_category__category_name')
            liability_history = Liability.objects.filter(user=request.user).values('id', 'liability_amount', 'liability_note', 'liability_date', 'liability_category__category_name')
            asset_history = Asset.objects.filter(user=request.user).values('id', 'asset_amount', 'asset_note', 'asset_date', 'asset_category__category_name')

            combined_history = list(income_history) + list(expense_history) + list(liability_history) + list(asset_history)
            
            combined_history_sorted = sorted(combined_history, key=lambda x: x.get('income_date', 
                                            x.get('expense_date', 
                                            x.get('liability_date', 
                                            x.get('asset_date', datetime.min)))), reverse=True)

            return Response(combined_history_sorted)


    def delete(self, request, entry_id):
        try:
            with transaction.atomic():
                income_entry = Income.objects.get(id=entry_id, user=request.user)
                income_entry.delete()
                return Response({'detail': 'Income entry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Income.DoesNotExist:
            try:
                with transaction.atomic():
                    expense_entry = Expense.objects.get(id=entry_id, user=request.user)
                    expense_entry.delete()
                    return Response({'detail': 'Expense entry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Expense.DoesNotExist:
                try:
                    with transaction.atomic():
                        liability_entry = Liability.objects.get(id=entry_id, user=request.user)
                        liability_entry.delete()
                        return Response({'detail': 'Liability entry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                except Liability.DoesNotExist:
                    try:
                        with transaction.atomic():
                            asset_entry = Asset.objects.get(id=entry_id, user=request.user)
                            asset_entry.delete()
                            return Response({'detail': 'Asset entry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                    except Asset.DoesNotExist:
                        raise Http404("History entry not found")

##################################################################################################################################


