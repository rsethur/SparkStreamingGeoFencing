# Setup

1. Create your Databricks Cluster (or any spark cluster)

2. Install the following dependencies in your cluster. Instructions are [here](https://docs.azuredatabricks.net/user-guide/libraries.html)
    * `shapely` via (PyPI)
    * `geojson` via (PyPI)
    * Eventhub-Spark Adapter: `com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.13` via maven coordinates (optionally you can check latest version of eventhub connector [here](https://mvnrepository.com/artifact/com.microsoft.azure/azure-eventhubs-spark))

3. Setup EventHub 
    * We need to create the following (replace XXXXX with your naming):
        * Eventhub Namespace: `XXXXX-eventhub-ns`
        * An eventhub for source data: `geofence-hub`
        * An eventhub to act as sink: `sink-geofence-hub`
        * We need an access key. In this case we will use `RootManageSharedAccessKey`
    * __Option 1: Through the Azure Portal__ 
        * Create the Namespace(`XXXXX-eventhub-ns`) and  both eventhubs(`geofence-hub` and `sink-geofence-hub`) via the Azure portal using the instructions [here](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)
        * Get the `RootManageSharedAccessKey` for the namespace using instructions [here](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#get-connection-string-from-the-portal). __Note__ that the last point in the instruction is to copy the `connection string promary key` - but we need to copy the `primary key` only
    * __Option 2: Using the Azure CLI (from local/dev machine)__
        * We have created the instructions for this [here](Setup%20Eventhubs%20using%20Azure%20CLI.md)
        * Follow the instructions to get the `connection strings` for both the eventhubs(geofence-hub and sink-geofence-hub)
        
    * Now you should have the access key handy (`primary key`)