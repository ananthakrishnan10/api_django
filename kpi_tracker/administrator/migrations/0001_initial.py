# Generated by Django 3.2 on 2021-04-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DINFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="IndustrialEfficiencyFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="NDVCTurnoverFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="NEEFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="OTDMFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="OutGoingQuantityFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="SupplierQuantityFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="SupplierQuantityFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.supplierquantityfiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OutGoingQuantityFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("assy_production_ppm", models.CharField(max_length=100)),
                ("molding_production_ppm", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.outgoingquantityfiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OTDMFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.otdmfiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NEEFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.neefiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NDVCTurnoverFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.ndvcturnoverfiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndustrialEfficiencyFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("month_actual", models.CharField(max_length=100)),
                ("month_target", models.CharField(max_length=100)),
                ("ytd_actual", models.CharField(max_length=100)),
                ("ytd_target", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.industrialefficiencyfiles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DINFilesData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.CharField(max_length=100)),
                ("actual_ytd_din", models.CharField(max_length=100)),
                ("target_ytd_din", models.CharField(max_length=100)),
                ("actual_spot_din", models.CharField(max_length=100)),
                ("target_spot_din", models.CharField(max_length=100)),
                ("net_inventorys", models.CharField(max_length=100)),
                (
                    "file_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.dinfiles",
                    ),
                ),
            ],
        ),
    ]
