1. A website front-end based on ReactJS + Ant Design Pro. Includes serveral pages:
 - Dashboard with the overview of plant performance & finanical result. 
 - Plant list-view, with the daily & history performance information 
 - Alert list-view, where Alert is generate by the anomaly detection system by analysing the time-series data collected from plant. 
 - O&M list-view, list all the operation & maintenance tasks. where the task should associate with specific Alert. 
2. A PostgresDB to stored the assets information, the data model described at https://github.com/sheauhei/pvplants/blob/main/sample/data_model.txt
3. A InfluxDB to stored the time-series data logged from the PV plant. 
 - the data schema is described here: https://github.com/sheauhei/pvplants/blob/main/sample/time-series.txt
 - the logging interval is 5 min. 
4. A core-module, that used for data analysis to: 
 - Anomaly Detection for data collected from plants. Once detected, add a record into database.
 - Daily Plants Performance Analysis.
5. A reporting system, to generate the O&M report and finanical report
 - Display the result on a Dashboard system
