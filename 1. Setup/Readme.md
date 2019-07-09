# Setup

1. Create your Databricks Cluster (or any spark cluster)

2. Install the following dependencies in your cluster. Instructions are [here](https://docs.azuredatabricks.net/user-guide/libraries.html)
    * `Shapely (PyPI)`
    * `geojson (PyPI)`
    * `Eventhub-Spark Adapter (maven coordinates)`: com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.13

3. Setup EventHub (from local/development machine)
    * Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) (optionally you can do this through Azure Portal)
    * Create event hub namespace and event hubs from the command line:
        * `az login`
        * Change location parameter as needed and execute: 
            * `az group create --name "geofence_rg" --location eastus`
        * Change namespace & location parameters and execute: 
            * `az eventhubs namespace create --name "XXXXX-eventhub-ns" --resource-group "geofence_rg" --location eastus`
        * Create an event hub that acts as source for spark streaming
            * `az eventhubs eventhub create --name "geofence-hub" --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns"`
         Create an event hub that acts as sink for spark streaming
            * `az eventhubs eventhub create --name "dest-geofence-hub" --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns"`
        * Get the "connection string primary key"
            * `az eventhubs namespace authorization-rule keys list --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns" --name RootManageSharedAccessKey`
            
4. Setup local python environment (preferably conda/virtualenv)
    * Install python dependencies (Conda/virtualenv):
        * `pip install azure-eventhub`