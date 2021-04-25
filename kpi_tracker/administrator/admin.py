from django.contrib import admin
from .models import (
    SupplierQuantityFilesData,
    SupplierQuantityFiles,
    OutGoingQuantityFiles,
    OutGoingQuantityFilesData,
    OTDMFiles,
    OTDMFilesData,
    DINFiles,
    DINFilesData,
    NDVCTurnoverFiles,
    NDVCTurnoverFilesData,
    IndustrialEfficiencyFiles,
    IndustrialEfficiencyFilesData,
    NEEFiles,
    NEEFilesData,
)

# Register your models here.

admin.site.register(OutGoingQuantityFiles)
admin.site.register(OutGoingQuantityFilesData)
admin.site.register(SupplierQuantityFiles)
admin.site.register(SupplierQuantityFilesData)
admin.site.register(OTDMFiles)
admin.site.register(OTDMFilesData)
admin.site.register(DINFiles)
admin.site.register(DINFilesData)
admin.site.register(NDVCTurnoverFiles)
admin.site.register(NDVCTurnoverFilesData)
admin.site.register(IndustrialEfficiencyFiles)
admin.site.register(IndustrialEfficiencyFilesData)
admin.site.register(NEEFiles)
admin.site.register(NEEFilesData)
