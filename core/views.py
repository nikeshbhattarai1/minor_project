# Create your views here.
from decimal import Decimal
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db import transaction
from django.core.serializers import serialize

from datetime import datetime

from . models import Income, IncomeCategory, Expense, ExpenseCategory, Asset,\
                    AssetCategory, Liability, LiabilityCategory
from . serializers import IncomeCategorySerializer, IncomeSerializer,ExpenseSerializer,\
                            AssetSerializer, LiabilitySerializer, ExpenseCategorySerializer,\
                            AssetCategorySerializer, LiabilityCategorySerializer

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



class IncomeView(ListCreateAPIView):
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



class ExpenseView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        print("VIEW")
        return ExpenseSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

    # def get_queryset(self):
    #     return Expense.objects.filter(user_id=self.request.user.id)
    
    # def get_serializer_class(self):
    #     return ExpenseSerializer
    


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



class AssetView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
         return Asset.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        # print("VIEW")
        return AssetSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


    # def get_queryset(self):
    #     return Asset.objects.filter(user_id=self.request.user.id)
    
    # def get_serializer_class(self):
    #     return AssetSerializer

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



class LiabilityView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Liability.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        # print("VIEW")
        return LiabilitySerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


    # def get_queryset(self):
    #     return Liability.objects.filter(user_id=self.request.user.id)
    
    # def get_serializer_class(self):
    #     return LiabilitySerializer
    


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
        return Response({"balance_amount":total_income-total_expense})
    

############################################################################################################
    
# class HistoryView(APIView, DeleteModelMixins):
#     permission_classes = [IsAuthenticated]

    

#     def get(self, request):
#         income_history = Income.objects.filter(user=request.user).values('id','income_amount', 'income_note', 'income_date',"income_category__category_name")
#         expense_history = Expense.objects.filter(user=request.user).values('expense_amount', 'expense_note', 'expense_date','expense_category__category_name')
#         liability_history = Liability.objects.filter(user=request.user).values('liability_amount', 'liability_note', 'liability_date','liability_category__category_name')
#         asset_history = Asset.objects.filter(user=request.user).values('asset_amount', 'asset_note', 'asset_date','asset_category__category_name')
#         combined_history = list(income_history) + list(expense_history) + list(liability_history) + list(asset_history)
#         combined_history_sorted = sorted(combined_history, key=lambda x: x.get('income_date', 
#                                          x.get('expense_date', 
#                                          x.get('liability_date', 
#                                          x.get('asset_date', datetime.min)))), reverse=True)
#         return Response(combined_history_sorted)





class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, entry_id=None):
        if entry_id is not None:
            # If an entry_id is provided, treat it as a request for a specific history entry
            try:
                income_entry = Income.objects.get(id=entry_id, user=request.user)
                serializer = IncomeSerializer(income_entry)
                return Response(serializer.data)
            except Income.DoesNotExist:
                try:
                    expense_entry = Expense.objects.get(id=entry_id, user=request.user)
                    serializer = ExpenseSerializer(expense_entry)
                    return Response(serializer.data)
                except Expense.DoesNotExist:
                    try:
                        liability_entry = Liability.objects.get(id=entry_id, user=request.user)
                        serializer = LiabilitySerializer(liability_entry)
                        return Response(serializer.data)
                    except Liability.DoesNotExist:
                        try:
                            asset_entry = Asset.objects.get(id=entry_id, user=request.user)
                            serializer = AssetSerializer(asset_entry)
                            return Response(serializer.data)
                        except Asset.DoesNotExist:
                            raise Http404("History entry not found")
        
        else:
            # If no entry_id is provided, return the entire financial history
            income_history = Income.objects.filter(user=request.user)
            expense_history = Expense.objects.filter(user=request.user)
            liability_history = Liability.objects.filter(user=request.user)
            asset_history = Asset.objects.filter(user=request.user)

            combined_history = list(income_history) + list(expense_history) + list(liability_history) + list(asset_history)
            
            combined_history_serialized = []

            for entry in combined_history:
                if isinstance(entry, Income):
                    serializer = IncomeSerializer(entry)
                elif isinstance(entry, Expense):
                    serializer = ExpenseSerializer(entry)
                elif isinstance(entry, Liability):
                    serializer = LiabilitySerializer(entry)
                elif isinstance(entry, Asset):
                    serializer = AssetSerializer(entry)

                combined_history_serialized.append(serializer.data)

            combined_history_sorted = sorted(combined_history_serialized, key=lambda x: x.get('income_date', 
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
