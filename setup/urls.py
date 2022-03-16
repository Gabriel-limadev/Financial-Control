from django.contrib import admin
from django.urls import path, include
from finance.views import ExpenseList, ExpenseDetail, ExpensesMonth, RevenueList, RevenueDetail, RevenuesMonth, ResumeMonth

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/revenues/', RevenueList.as_view()),  
    path('api/revenues/<int:pk>/', RevenueDetail.as_view()),

    path('api/expenses/', ExpenseList.as_view()),  
    path('api/expenses/<int:pk>/', ExpenseDetail.as_view()),


    path('api/expenses/<int:year>/<int:month>/', ExpensesMonth.as_view()),
    path('api/revenues/<int:year>/<int:month>/', RevenuesMonth.as_view()),
    path('api/resume/<int:year>/<int:month>/', ResumeMonth.as_view())
]
        