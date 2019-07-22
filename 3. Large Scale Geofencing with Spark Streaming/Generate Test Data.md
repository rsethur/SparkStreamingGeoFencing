# Generate Test Data

__Note__: We will be executing this from your local/dev machine.

1. Setup new source event hub (`largescale-geofence-hub`) and sink eventhub (`largescale-sink-geofence-hub`) using instructions [here](../1.%20Setup/Readme.md).
    * Get the `primary key` as well as per the above instructions.
2. Setup local python environment (preferably conda/virtualenv)
    * Install python dependencies (Conda/virtualenv):
        * `pandas` `shapely` `geojson` `azure-eventhub`
3. Clone this git repo - we will be working on the code on this folder
4. Update `config.json`
    * Update the value for `EVENT_HUB_SAS_KEY` with the `primary key` you got above
5. Edit your preferences if any in the `GenerateTestData.py`
6. Execute `python GenerateTestData.py`. Note that this may take a while to execute (depending on how much data you are generating)