import findspark
import sys
import math
import csv
import json
import pandas as pd
import numpy as np
from django.shortcuts import render,HttpResponse
from django.http import request
from random import random
from operator import add
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType
from .models import TkCabezal,TkRenglones
from shutil import rmtree
from os import mkdir


# Create your views here.
def inicio(request):
    data.show()
    return HttpResponse('Hasta aca todo bien')

def consulta(request):
    
    try:    
        rmtree("D:/Spark/archivos/")#con esto elimino la carpeta con todos los archivos
        print("Elimina carpeta")
    except: 
        print("E")
   
    mkdir("D:/Spark/archivos/")#Vuelvo a crear la carpeta
    try:

        df=pd.DataFrame.from_records(TkCabezal.objects.all().values_list("terminal","ticket","tipo","rollo","caja","cajero","fecha","total"),columns=["Terminal","Ticket","Tipo","Rollo","Caja","Cajero","Fecha","Total"])
        print("Empezo a escribir cabezal a csv")
        df.to_csv("D:/Spark/archivos/tkcabezal.csv",sep=";")#Escribo los csv con separacion por punto y coma
        print("Escribió TkCabezal.CSV")
        dfd=pd.DataFrame.from_records(TkRenglones.objects.all().values_list("terminal","ticket","renglon","idmercaderia","codigo","descripcion","cantidad","preventa","prereal"),columns=["Terminal","Ticket","Renglon","Mercaderia","Codigo","Descripcion","Cantidad","PreVenta","PreReal"])
        dfd.to_csv("D:/Spark/archivos/tkdetalle.csv",sep=";")
        print("Escribió TKRenglones.CSV")
    except:
        print('Error en la Importacion')     
    """
    c = csv.writer(open("D:/Spark/archivos/tkcabezal.csv","w")) 
    cd = csv.writer(open("D:/Spark/archivos/tkdetalle.csv","w"))
    #cda = csv.writer(open("D:/Spark/cfe_detalle_ad.csv","w"))
    c.writerow(["Terminal;Ticket;Tipo;Rollo;Caja;Cajero;Fecha;Total;IvaMin;IvaBas;Estado;Motivo"])
    cd.writerow(["Terminal;Ticket;Renglon;Codigo;Descripcion;Moneda;Cant;Importe;Tasa IVA"])
    print("Empezo a escribir")
    for rows in TkRenglones.objects.all(): 
        cd.writerow([str(rows.terminal)+";"+str(rows.ticket)+";"+str(rows.renglon)+";"\
                    +str(rows.codigo)+";"+str(rows.descripcion)+";"+str(rows.idmoneda)+";"\
                    +str(rows.cantidad)+";"+str(rows.importe)+";"+str(rows.taiva)])

    print("Escribió TKRenglones.CSV")

    for row in TkCabezal.objects.all():
        c.writerow([str(row.terminal)+";"+str(row.ticket)+";"+str(row.tipo)+";"\
                    +str(row.rollo)+";"+str(row.caja)+";"+str(row.cajero)+";"\
                    +str(row.fecha)+";"+str(row.total)+";"+str(row.ivamin)+";"\
                    +str(row.ivabas)+";"+str(row.estado)+";"+str(row.motivo)])
        
    print("Escribió TkCabezal.CSV")
    """
    
    findspark.init()
    from pyspark import SparkConf
    #la siguiente linea es la sesion de spark con su configuracion
    spark = SparkSession\
            .builder\
            .appName("Consultas")\
            .master("local[*]")\
            .config("spark.executor.heartbeatInterval",30000)\
            .config("spark.default.parallelism",4)\
            .enableHiveSupport()\
            .getOrCreate() 
            #en las lineas anteriores le paso el intervalo a esperar en milisegundos y los procesadores que quiero que use

    #a continuacion traigo los datos de los csv y los transformo a archivos parquet.
    df = spark.read.option("header","true").option("delimiter",";").option("infierSchema","true").csv("D:/Spark/archivos/tkcabezal.csv")
    dfd = spark.read.option("header","true").option("delimiter",";").option("infierSchema","true").csv("D:/Spark/archivos/tkdetalle.csv")
    df.write.parquet("D:/Spark/archivos/input-parquet-cabezal")
    dfd.write.parquet("D:/Spark/archivos/input-parquet-detalle")
    return principal(request)	   

def mostrar(request):
    global list_cabezal
    global list_detalle 
    serie = ""
    numero = ""
    findspark.init('D:\Spark\spark-2.4.7-bin-hadoop2.7')
    #findspark.add_packages('org.db.mysql:mysql-connector-java-5.1.49.jar')
    from pyspark import SparkConf
    spark = SparkSession\
        .builder\
        .appName("PythonMostrar")\
        .getOrCreate()
    data = spark.read.option("header","true").option("delimiter",";").option("infierSchema","true").parquet("D:/Spark/archivos/input-parquet-cabezal")
    datadf=spark.read.option("header","true").option("delimiter",";").option("infierSchema","true").parquet("D:/Spark/archivos/input-parquet-detalle")
    #lista=data.select("Tipo","Serie","Numero","Fecha","Info").where(data["Numero"].rlike("123")).collect()
    if request.is_ajax():
        dato = request.POST.get("info")
        tipo = request.POST.get("tipo")
        serie = dato[0:2]
        numero = dato[2:len(dato)].strip() 
        print(serie+"  "+numero)
        if tipo=="detalle": 
            lista=datadf.select("*").filter(datadf["Terminal"]==serie).filter(datadf["Ticket"]==numero).collect()
            mensaje='<table class="table table-responsive"><thead><tr>'\
                    '<th scope="col">Renglon</th><th scope="col">Mercaderia</th><th scope="col">Codigo</th>'\
                    '<th scope="col">Descripcion</th><th scope="col">Cantidad</th>'\
                    '<th scope="col">Precio Venta</th><th scope="col">Precio Real</th></tr></thead><tbody><tr>'
                    
            for li in lista:
                mensaje+='<td>'+str(li.Renglon)+'</td><td>'+str(li.Mercaderia)+'</td><td>'+str(li.Codigo)+'</td>'\
                         '<td>'+str(li.Descripcion)+'</td><td>'+str(li.Cantidad)+'</td><td>'+str(li.PreVenta)+'</td>'\
                         '<td>'+str(li.PreReal)+'</td></tr>'\

            mensaje+='</tbody></table>'

            lista=json.dumps(mensaje)
            return HttpResponse(lista,content_type='application/json')              
        else:
              
            lista=data.select("*").filter(data["Terminal"]==serie).filter(data["Ticket"].rlike(numero)).collect()
            mensaje='<table class="table table-responsive"><thead><tr>'\
                    '<th scope="col">Terminal</th><th scope="col">Ticket</th><th scope="col">Tipo</th>'\
                    '<th scope="col">Rollo</th><th scope="col">Caja</th><th scope="col">Cajero</th>'\
                    '<th scope="col">Fecha</th><th scope="col">Total</th></tr></thead><tbody><tr>' 
            for li in lista:   
                mensaje+='<td id="tipocfe" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Terminal)+'</td> <td id="numero" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Ticket)+'</td>'\
                         '<td id="tipocfe" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Tipo)+'</td> <td id="numero" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Rollo)+'</td>'\
                         '<td id="fecha" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Caja)+'</td> <td id="info" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Cajero)+'</td>'\
                         '<td id="fecha" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Fecha)+'</td> <td id="info" onclick="return buscar_detalle('+li.Terminal+li.Ticket+')">'+str(li.Total)+'</td></tr>'   
            mensaje+='</tbody></table>'

            lista=json.dumps(mensaje)
            return HttpResponse(lista,content_type='application/json')

def principal(request):    
    return render(request,'index.html',{})         

    """ df = spark.read.format("jdbc") \
            .option("url",mysql_jdbc_url) \
            .option("driver",mysql_db_driver_class) \
            .option("dbtable",mysql_select_query) \
            .option("user",user_name) \
            .option("password",password) \
            .load()

    
    #df = spark.read.option("header","true").option("delimter",";").option("infierSchema","true").csv("D:/Spark/cfe_cabezal.csv")

    spark.sparkContext.setLogLevel("Error") 
    mysql_db_driver_class = "com.mysql.jdbc.Driver" 
    table_name = "cfe_cabezal"
    host_name = "192.168.1.50"
    port_no = str(3306)
    user_name = "root"
    password = "Anita2020"
    database_name = "independencia"
    useSSL="useSSL = false;"

    mysql_select_query = "(select * from "+table_name+") as cfe_cabezal limit 200"

    mysql_jdbc_url = "jdbc:mysql://" + host_name + ":" + port_no + "/" + database_name
    #cfe = CfeCabezal.objects.all()
    """