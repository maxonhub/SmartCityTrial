# Imports the PySpark libraries
from pyspark import SparkConf, SparkContext

# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os

# Configure the Spark context to give a name to the application
sparkConf = SparkConf().setAppName("PollutionScript")
sc = SparkContext(conf = sparkConf)

textFile = sc.textFile(os.environ["SPARK_HOME"] + "\README.md")