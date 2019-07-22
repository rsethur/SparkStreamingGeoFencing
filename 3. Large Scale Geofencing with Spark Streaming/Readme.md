# Benchmark Setup

#### For instuctions on generating test data read [this](Generate%20Test%20Data.md)

### Test Data Generation
* No. of vehicles: 1000
* Frequency of realtime location event: 1 sec per vehicle
* Duration of events: 1 hour
* Total number of events: 
    * For one vehicle: 60*60 = 3600 events per hour
    * For 1000 vehicles: 3.6 million per hour
* No. of geofence polygons: 1000 ( 1 per vehicle)

### Event hub setup (not tuned for efficiency - just taking the max specs currently)
* No. of partitions: 32
* Throughput: 20 Mbps
* Ingress: 
    * Avg size of event data: 200 bytes
    * Throughput: 1000 * 200 bytes = 200 KB/s
 * Egress: similar to above (may be 100 bytes extra)
 
### Initial Databricks setup
* Cluster size: 8 nodes
* maxEventsPerTrigger in streaming query: 20,000