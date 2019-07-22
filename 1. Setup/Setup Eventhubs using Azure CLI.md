# Setup Eventhubs using Azure CLI (in your local/dev machine)
    
 1. Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) (optionally you can do this through Azure Portal)
    
 2. Create event hub namespace (Execute the commands in the command line)
    * `az login`
    * Change location parameter as needed and execute: 
        * `az group create --name "geofence_rg" --location eastus`
    * Change namespace & location parameters and execute: 
        * `az eventhubs namespace create --name "XXXXX-eventhub-ns" --resource-group "geofence_rg" --location eastus`
 3. Create an source and destination eventhub for spark streaming
    * `az eventhubs eventhub create --name "geofence-hub" --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns"`
    * `az eventhubs eventhub create --name "sink-geofence-hub" --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns"`
 4. Get the `RootManageSharedAccessKey` for the namespace by executing the below command (you will need this later)
    * `az eventhubs namespace authorization-rule keys list --resource-group "geofence_rg" --namespace-name "XXXXX-eventhub-ns" --name RootManageSharedAccessKey`