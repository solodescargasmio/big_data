import findspark
from django.shortcuts import render,HttpResponse
from django.http import request
import sys
import math
from random import random
from operator import add
from pyspark.sql import SparkSession
from .models import Alumno


# Create your views here.
def inicio(request):
	return HttpResponse('Hasta aca todo bien')

def pi(request):

    findspark.init('D:\Spark\spark-2.4.7-bin-hadoop2.7')
    from pyspark import SparkConf
    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate() 
    df=spark.read.csv("C:/Users/yo/Desktop/archivo.csv",header=False,sep=";")
    df.show()
    #alumno=Alumno.objects.get()
    
    return HttpResponse(df)       
""" partitions = 2
    if math.isnan(partitions):
    	partitions = 3
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))
    spark.stop()
    return HttpResponse("Pi is roughly %f" % (4.0 * count / n))"""

def consulta(request):
	findspark.init()
	from pyspark import SparkConf
	spark = SparkSession\
			.builder\
			.appName("Consultas")\
			.master("local[*]")\
			.config("spark.jars","file:///D:/Spark/mysqlconector/mysql-connector/mysql-connector-java-5.1.49.jar")\
			.config("spark.executor.extraClassPath","file:///D:/Spark/mysqlconector/mysql-connector/mysql-connector-java-5.1.49.jar")\
			.config("spark.executor.extraLibrary","file:///D:/Spark/mysqlconector/mysql-connector/mysql-connector-java-5.1.49.jar")\
			.config("spark.driver.extraClassPath","file:///D:/Spark/mysqlconector/mysql-connector/mysql-connector-java-5.1.49.jar")\
			.enableHiveSupport()\
			.getOrCreate() 

	spark.sparkContext.setLogLevel("Error")	
	mysql_db_driver_class = "com.mysql.jdbc.Driver"	
	table_name = "alumno"
	host_name = "localhost"
	port_no = str(3306)
	user_name = "root"
	password = "****"
	database_name = "itsp"

	mysql_select_query = "(select * from "+table_name+") as alumnos"

	mysql_jdbc_url = "jdbc:mysql://" + host_name + ":" + port_no + "/" + database_name

	df = spark.read.format("jdbc") \
		.option("url",mysql_jdbc_url) \
		.option("driver",mysql_db_driver_class) \
		.option("dbtable",mysql_select_query) \
		.option("user",user_name) \
		.option("password",password) \
		.load()

	df.show()
	lista = df.select("Nombre").collect()
	dicc=[]
	for i in lista:
		dicc.append(i)
	df.select("Nombre","Apellido").show()	
	
	return HttpResponse(dicc)		   

"""
df=spark.read.csv("C:/Users/yo/Desktop/archivo.csv",header=False,sep=";")
    	df.show()with open("C:DesktopProjectAlerts.sql") as Al:
Alert= Al.read()
results = sqlctx.sql(Alert)"""	

	