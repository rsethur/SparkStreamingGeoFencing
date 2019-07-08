import json
import time
from azure.eventhub import EventHubClient, EventPosition, EventHubSharedKeyCredential, EventData
import os
import math
import datetime
from datetime import timedelta
import random

START_DATETIME = datetime.datetime(year=2019, month=7, day=5, hour=7)

NUM_VEHICLES = 1024 #Make this a multiple of NUM_PARTITIONS
NUM_PARTITIONS = 32

NUM_VEHICLES_PER_PARTITION = int(NUM_VEHICLES / NUM_PARTITIONS)

SIZE_OF_EVENT_DATA_BYTES = 0.17 # in KB

SIZE_LIMIT_OF_EVENT_DATA_KB = 1024 # in KB

NUM_EVENTS_PER_BATCH = int(SIZE_LIMIT_OF_EVENT_DATA_KB/SIZE_OF_EVENT_DATA_BYTES) #calculated based on 1 MB limit on event data(Event hub)

NUM_EVENTS_PER_VEHICLE_PER_BATCH = int(NUM_EVENTS_PER_BATCH / NUM_VEHICLES_PER_PARTITION)

TIME_BETWEEN_EVENTS_SECS = 1 #in seconds
DURATION_FOR_DATA_GENERATION_MINS = 60 # in minutes
TOTAL_EVENTS_PER_VEHICLE = math.ceil((DURATION_FOR_DATA_GENERATION_MINS * 60)/TIME_BETWEEN_EVENTS_SECS)
TOTAL_EVENTS_FOR_ALL_VEHICLES = TOTAL_EVENTS_PER_VEHICLE * NUM_VEHICLES

EVENTS_PER_ITERATION_OVER_ALL_PARTITIONS = NUM_EVENTS_PER_BATCH * NUM_PARTITIONS
TOTAL_ITERATIONS_OVER_ALL_PARTITIONS = round(TOTAL_EVENTS_FOR_ALL_VEHICLES/EVENTS_PER_ITERATION_OVER_ALL_PARTITIONS) #Ideally this could be math.ceil to err in side of caution

OUT_OF_GEOFENCE_PROB = 0.1
GEOJSON_FILE_PATHS =["location_data/points/point_1.geojson", "location_data/points/point_2.geojson"]
global_event_id = 0 #keeps track of current event #
event_producer_list = []
geojson_list = []

global_current_batch_num = 0 #only for display

def main():
    init_event_hub()
    init_point_geojsons()
    print("TOTAL_ITERATIONS_OVER_ALL_PARTITIONS: ", TOTAL_ITERATIONS_OVER_ALL_PARTITIONS)
    print("Total batches: ", TOTAL_EVENTS_FOR_ALL_VEHICLES/NUM_EVENTS_PER_BATCH)
    curr_time = START_DATETIME
    for curr_global_iter in range(TOTAL_ITERATIONS_OVER_ALL_PARTITIONS):
        print("Global iter#: ", curr_global_iter)
        for curr_partition in range(NUM_PARTITIONS):
            vehicle_id_list_for_partition = list(range(curr_partition*NUM_PARTITIONS,(curr_partition*NUM_PARTITIONS) + NUM_PARTITIONS)) #could be precomputed for efficiency :)
            curr_time = handleSingleBatch(curr_partition, vehicle_id_list_for_partition, curr_time)

def handleSingleBatch(partition_id, vehicle_id_list, curr_time):
    eventBatchData = []
    global global_current_batch_num
    global global_event_id
    print("Processing batch# :", global_current_batch_num)
    for _ in range(NUM_EVENTS_PER_VEHICLE_PER_BATCH):
        for curr_vehicle_id in vehicle_id_list:
            curr_point = random.choices(population=geojson_list, weights=[1.0-OUT_OF_GEOFENCE_PROB, OUT_OF_GEOFENCE_PROB], k=1)[0]
            curr_point["vehicle_id"] = curr_vehicle_id
            curr_point["point_id"] = global_event_id
            curr_point["event_date"] = str(curr_time)
            eventBatchData.append(EventData(json.dumps(curr_point)))
            global_event_id += 1
        curr_time +=  timedelta(seconds=TIME_BETWEEN_EVENTS_SECS)
    event_producer_list[partition_id].send(eventBatchData)
    global_current_batch_num += 1
    return curr_time

def init_event_hub():
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)
    client = EventHubClient(host=config["EH_HOST"], event_hub_path=config["EH_NAME"],
                            credential=EventHubSharedKeyCredential(config["EVENT_HUB_SAS_POLICY"],
                                                                   config["EVENT_HUB_SAS_KEY"]),
                            network_tracing=False)

    for i in range(NUM_PARTITIONS):
        event_producer_list.append(client.create_producer(partition_id=str(i)))

def init_point_geojsons():
    for file_path in GEOJSON_FILE_PATHS:
        with open(file_path, 'r') as json_file:
            geojson_list.append(json.load(json_file))

if __name__ == '__main__':
    main()