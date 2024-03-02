from django.urls import path
# from .views import DivideAmountView
from . import views

urlpatterns = [
    path('incomecategories/<int:pk>/', views.IncomeCategoryDetailView.as_view()),
    path('incomecategories/', views.IncomeCategoryView.as_view()),
    path('incomes/', views.IncomeView.as_view()),
    path('incomes/<int:pk>/', views.IncomeDetailView.as_view()),

    path('expensecategories/<int:pk>/', views.ExpenseCategoryDetailView.as_view()),
    path('expensecategories/', views.ExpenseCategoryView.as_view()),
    path('expenses/', views.ExpenseView.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view()),

    path('assetcategories/<int:pk>/', views.AssetCategoryDetailView.as_view()),
    path('assetcategories/', views.AssetCategoryView.as_view()),
    path('assets/', views.AssetView.as_view()),
    path('assets/<int:pk>/', views.AssetDetailView.as_view()),
    
    path('liabilitycategories/<int:pk>/', views.LiabilityCategoryDetailView.as_view()),
    path('liabilitycategories/', views.LiabilityCategoryView.as_view()),
    path('liabilitys/', views.LiabilityView.as_view()),
    path('liabilitys/<int:pk>/', views.LiabilityDetailView.as_view()),

    path('totalincomes/', views.TotalIncomeView.as_view()),
    path('totalexpenses/', views.TotalExpenseView.as_view()),
    path('totalliabilitys/', views.TotalLiabilityView.as_view()),
    path('totalassets/', views.TotalAssetView.as_view()),

    path('balanceamount/', views.BalanceView.as_view()), #income-expense

    path('history/', views.HistoryView.as_view()),
    path('history/<int:entry_id>/', views.HistoryView.as_view(), name='history-detail'),

    path('targetwalletcreate/', views.TargetWalletCreateView.as_view()),
    path('targetwallet/<str:index>/', views.TargetWalletDetailView.as_view()),

    path('targets/', views.TargetListView.as_view()),
    path('targets/<int:pk>', views.TargetDetailView.as_view()),

]
