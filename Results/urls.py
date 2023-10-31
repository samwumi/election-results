from django.urls import path
from . import views


urlpatterns = [
    path('polling-unit/<int:polling_unit_uniqueid>/', views.view_polling_unit_results, name='polling_unit_results'),
    path('lga-total-result/<int:polling_unit_uniqueid>/', views.view_lga_total_results, name='view_lga_total_results'),
    
]


