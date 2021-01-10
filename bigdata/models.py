# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grado = models.IntegerField(db_column='Grado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alumno'


class Grado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grado'


class Materia(models.Model):
    idmateria = models.IntegerField(db_column='idMateria', primary_key=True)  # Field name made lowercase.
    idgrado = models.IntegerField(db_column='idGrado')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materia'
        unique_together = (('idmateria', 'idgrado'),)


class SubTarea(models.Model):
    idsub_tarea = models.IntegerField(db_column='idSub_Tarea', primary_key=True)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='idUsuario')  # Field name made lowercase.
    idtarea = models.IntegerField(db_column='idTarea')  # Field name made lowercase.
    subcomentario = models.CharField(db_column='SubComentario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    terminada = models.TextField(db_column='Terminada', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tiempo = models.TimeField(db_column='Tiempo', blank=True, null=True)  # Field name made lowercase.
    fecsub = models.DateField(db_column='FecSub', blank=True, null=True)  # Field name made lowercase.
    fecfinsub = models.DateTimeField(db_column='FecFinSub', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_tarea'
        unique_together = (('idsub_tarea', 'idusuario', 'idtarea'),)


class Tarea(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(db_column='Titulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarea'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioTarea(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    idtarea = models.IntegerField(db_column='idTarea')  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pendiente = models.TextField(db_column='Pendiente', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_tarea'
        unique_together = (('idusuario', 'idtarea'),)
