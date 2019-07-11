# Large Scale Geofencing with Spark Streaming
Realtime Geofencing using Spark streaming for a vehicle tracking / fleet management usecases.

I created this to help some of my customers in the Fleet Tracking business who have in the order of million vehicles. When I googled for Spark + geospatial libraries i got some nice libraries - but none not being maintained regularly.
So made a decision not to create another library - and have least dependencies possible (shapely is the only real one).

Very open for feedback.


1. [Setup](1.%20Setup)

2. [Basics of Geofencing with Spark Streaming](2.%20Basics%20of%20Geofencing%20with%20Spark%20Streaming)

3. [Large Scale Geofencing with Spark Streaming](3.%20Large%20Scale%20Geofencing%20with%20Spark%20Streaming)

Note: Currently cleaning up and writing better documentation

__Performance Benchmark Summary__: 
* Roughly I was able to run geofencing for 3.7 million Geojson messages in 2 mins 10 sec (throughput of 28k/sec). 
* The cluster size was 32 cores (4 cores * 8 nodes). 
* Data was for 1000 vehicles (and one geofence for each).
Test data generator can be customized to generate data according to your scale.