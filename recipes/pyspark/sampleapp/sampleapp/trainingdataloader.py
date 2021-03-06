#
# Copyright 2017 Adobe.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import LongType, DoubleType, IntegerType, StringType

def load(configProperties, spark):

    spark.sparkContext._jsc.hadoopConfiguration().set(str(spark.sparkContext.getConf().get("CONF_blobStoreAccount_KEY")),str(spark.sparkContext.getConf().get("CONF_blobStoreAccount_VALUE")))
    trainingDataLocation = str(configProperties.get("trainingDataLocation"))

    trainingSchema = StructType([
      StructField("id", LongType()),
      StructField("user", StringType()),
      StructField("text", StringType()),
      StructField("label", DoubleType())
    ])

    training = spark.read.schema(trainingSchema).format("csv").option("mode", "DROPMALFORMED").csv(trainingDataLocation)
    return training
