import findspark
from django.shortcuts import render,HttpResponse
from django.http import request
import sys
import math
from random import random
from operator import add
from pyspark.sql import SparkSession


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
    partitions = 2
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
    return HttpResponse("Pi is roughly %f" % (4.0 * count / n))

	

	