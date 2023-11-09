This folder consists of the following:
1. Python queries used for data collection
2. Data Description
3. Collected datasets:
  * Files starting with the label **Bcycle_data_to_data** is the actual dataset
  * Files starting with the label **Automation_logs** is data collection log with timestamp, # rows added and total # rows. 

**Data Description**:

The data is collected from [General Bikeshare Feed Specification (GBFS)](https://www.bcycle.com/gbfs), specific for the location Boulder, Colorado, United States. GBFS contains links to the following JSON files:
  1. [gbfs.json](https://gbfs.bcycle.com/bcycle_boulder/gbfs.json): A master document containing links to the following sub-documents.
  2. [gbfs_versions.json](https://gbfs.bcycle.com/bcycle_boulder/gbfs_versions.json): Contains the GBFS data version information.
  3. [system_information.json](https://gbfs.bcycle.com/bcycle_boulder/system_information.json): Contains BCycle app and website system information such as mobile app link, website link, contact phone number, contact email address, language used, and timezone followed.
  4. [station_information.json](https://gbfs.bcycle.com/bcycle_boulder/station_information.json): Contains station information including location coordinates, station name, station ID, and station address.
  5. [station_status.json](https://gbfs.bcycle.com/bcycle_boulder/station_status.json): Contains station status like functioning information and bike status including bike availability, dock availability, and type of bikes.
  6. [system_pricing_plans.json](https://gbfs.bcycle.com/bcycle_boulder/system_pricing_plans.json): Contains BCycle pricing information for students, single ride, month pass, and annual pass.
  7. [system_regions.json](https://gbfs.bcycle.com/bcycle_boulder/system_regions.json): Contains the system region information. The data is currently null.

Find the sample document here.

**Data Availability Record:**

The data collection was initiated on **10-16-23 19:45:03** with a 15-minute interval initially, which was later reduced to 1 minute. Each dataset is labeled with a from and to timestamp at the end of its name, in the format MMDDYYHHMMSS, indicating the timestamp of data available in the respective file.

1. **Bcycle_data_to_date_101623194503_110823173412 :** 
  * 10-16-23 19:45:03  --  10-17-23 01:00:52  -- Every 15mins
  * 10-17-23 01:03:59  --  10-19-23 11:53:45  -- Every 3mins
  * ----------break----------
  * 10-30-23 19:46:38  --  11-05-2023 17:26:10   -- Every 1min
  * ----------break----------
  * 11-06-2023 17:40:44   --  11-08-2023 17:34:12   -- Every 1min
