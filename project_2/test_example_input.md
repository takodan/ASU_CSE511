sbt clean assembly

spark-submit target/scala-2.11/CSE512-Hotspot-Analysis-Template-assembly-0.1.0.jar test/output hotzoneanalysis src/resources/point_hotzone.csv src/resources/zone-hotzone.csv

spark-submit target/scala-2.11/CSE512-Hotspot-Analysis-Template-assembly-0.1.0.jar test/output hotcellanalysis src/resources/yellow_trip_sample_100000.csv