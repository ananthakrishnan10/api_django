from django.db import models

# Create your models here.


class OutGoingQuantityFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class OutGoingQuantityFilesData(models.Model):

    file_id = models.ForeignKey(
        OutGoingQuantityFiles, on_delete=models.CASCADE, null=False
    )
    month = models.CharField(max_length=100, null=False)
    assy_production_ppm = models.CharField(max_length=100, null=False)
    molding_production_ppm = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class SupplierQuantityFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class SupplierQuantityFilesData(models.Model):

    file_id = models.ForeignKey(
        SupplierQuantityFiles, on_delete=models.CASCADE, null=False
    )
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class OTDMFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class OTDMFilesData(models.Model):

    file_id = models.ForeignKey(OTDMFiles, on_delete=models.CASCADE, null=False)
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class DINFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class DINFilesData(models.Model):

    file_id = models.ForeignKey(DINFiles, on_delete=models.CASCADE, null=False)
    month = models.CharField(max_length=100, null=False)
    actual_ytd_din = models.CharField(max_length=100, null=False)
    target_ytd_din = models.CharField(max_length=100, null=False)
    actual_spot_din = models.CharField(max_length=100, null=False)
    target_spot_din = models.CharField(max_length=100, null=False)
    net_inventorys = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class NDVCTurnoverFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class NDVCTurnoverFilesData(models.Model):

    file_id = models.ForeignKey(NDVCTurnoverFiles, on_delete=models.CASCADE, null=False)
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class IndustrialEfficiencyFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class IndustrialEfficiencyFilesData(models.Model):

    file_id = models.ForeignKey(
        IndustrialEfficiencyFiles, on_delete=models.CASCADE, null=False
    )
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)


class NEEFiles(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class NEEFilesData(models.Model):

    file_id = models.ForeignKey(NEEFiles, on_delete=models.CASCADE, null=False)
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)
