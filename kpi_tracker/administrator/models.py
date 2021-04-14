from django.db import models

# Create your models here.


class File(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file


class FileData(models.Model):

    file_id = models.ForeignKey(File, on_delete=models.CASCADE, null=False)
    month = models.CharField(max_length=100, null=False)
    month_actual = models.CharField(max_length=100, null=False)
    month_target = models.CharField(max_length=100, null=False)
    ytd_actual = models.CharField(max_length=100, null=False)
    ytd_target = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.file_id
