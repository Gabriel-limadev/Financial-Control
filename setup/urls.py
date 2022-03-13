from django.contrib import admin
from django.urls import path, include
from finance.views import ExpensesViewSet, RevenuesViewSet, ExpensesMonth, RevenuesMonth, ResumeMonth
from rest_framework import routers

router = routers.DefaultRouter()
router.register('revenues',   RevenuesViewSet,   basename='Revenues')
router.register('expenses',   ExpensesViewSet,   basename='Expenses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # For month
    path('expenses/<int:year>/<int:month>/', ExpensesMonth.as_view()),
    path('revenues/<int:year>/<int:month>/', RevenuesMonth.as_view()),
    path('resume/<int:year>/<int:month>/', ResumeMonth.as_view())
]
        