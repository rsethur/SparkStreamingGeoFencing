# Setup

1. Create your Databricks Cluster (or any spark cluster)

2. Install the following dependencies in your cluster
    * `Shapely (PyPI)`
    * `geojson (PyPI)`
    * `Eventhub-Spark Adapter (maven coordinates)`: com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.13

3. Install Azure tools in your local/development machine
    * Azure CLI
    * Install python dependencies (Conda/virtualenv):
        * `pip install azure-eventhub`

4. Setup EventHub (from local/development machine)
    * 