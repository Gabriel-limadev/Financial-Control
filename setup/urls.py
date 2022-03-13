from django.contrib import admin
from django.urls import path, include
from finance.views import ExpensesViewSet, RevenuesViewSet, ExpensesMonth, RevenuesMonth, ResumeMonth
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('revenues',   RevenuesViewSet,   basename='Revenues')
router.register('expenses',   ExpensesViewSet,   basename='Expenses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', include(router.urls)),
    path('expenses/<int:year>/<int:month>/', ExpensesMonth.as_view()),
    path('revenues/<int:year>/<int:month>/', RevenuesMonth.as_view()),
    path('resume/<int:year>/<int:month>/', ResumeMonth.as_view())
]
        