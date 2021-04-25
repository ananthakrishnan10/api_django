"""etp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    UserCreateList,
    UserDetail,
    SupplierQuantityView,
    SupplierQuantityDataList,
    OutGoingQuantityView,
    OutGoingQuantityDataList,
    OTDMView,
    OTDMDataList,
    DINView,
    DINDataList,
    NDVCTurnoverView,
    NDVCTurnoverDataList,
    IndustrialEfficiencyView,
    IndustrialEfficiencyDataList,
    NEEView,
    NEEDataList,
)

urlpatterns = [
    path("user/", UserCreateList.as_view()),
    path("user/<int:pk>/", UserDetail.as_view()),
    path("OGQ_file_upload/", OutGoingQuantityView.as_view()),
    path("OGQ_quantity_file_data/", OutGoingQuantityDataList.as_view()),
    path("supplier_quantity_file_upload/", SupplierQuantityView.as_view()),
    path("supplier_quantity_file_data/", SupplierQuantityDataList.as_view()),
    path("OTDM_file_upload/", OTDMView.as_view()),
    path("OTDM_file_data/", OTDMDataList.as_view()),
    path("DIN_file_upload/", DINView.as_view()),
    path("DIN_file_data/", DINDataList.as_view()),
    path("NDVCTurnover_file_upload/", NDVCTurnoverView.as_view()),
    path("NDVCTurnover_file_data/", NDVCTurnoverDataList.as_view()),
    path("IndustrialEfficiency_file_upload/", IndustrialEfficiencyView.as_view()),
    path("IndustrialEfficiency_file_data/", IndustrialEfficiencyDataList.as_view()),
    path("NEE_file_upload/", NEEView.as_view()),
    path("NEE_file_data/", NEEDataList.as_view()),
]
