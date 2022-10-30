from django.db import models

# Create your models here.
class Cuenca(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    nombre = models.TextField(unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuenca'


class Metodo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    nombre = models.TextField(unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metodo'


class Pesca(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)  # Field name made lowercase.
    idCuenca = models.ForeignKey(Cuenca, models.DO_NOTHING, db_column='idCuenca')  # Field name made lowercase.
    idMetodo = models.ForeignKey(Metodo, models.DO_NOTHING, db_column='idMetodo')  # Field name made lowercase.
    fecha = models.TextField(db_column='fecha')  # Field name made lowercase.
    peso = models.TextField(db_column='peso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pesca'