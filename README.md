# ETL-Data-warehousing-simpsons
In this project a database about the simpsons series is put into AWS RDS Postgres and 

moved to AWS Redshift using AWS Glue to be transformed into a star schema and unloaded into

AWS S3 bucket to be used in Bi tools later. 
![AWS_diagram](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/2b94e7f6-e218-4d05-b5b4-c64677891e61)

# Steps
1- Redshift and Postgres RDS are created in AWS and simpsons tables are created and uploaded in RDS using attached codes rds.py, rds_sql.py 
![rds_db_diagram](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/672146f0-523c-4345-a51f-6f7081dcec53)


2-AWS Glue connections are created for both rds and redshift
![Glue_connections](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/430d1551-c471-4958-bd1e-d3f685854555)

3-AWS Glue crawlers are created to fetch the tables
![crawlers](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/83e00a50-4f0a-47a3-8d91-c19a2c155682)

after the crawlers are done running tables are created 
![crawlers_tables](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/4ab3488d-b737-44f5-ac5e-92d35a882309)

4-AWS Glue databases are created to put temporary fetched data in them
![Glue_databases](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/57478785-34c5-4f62-ad6f-97f3cce65f2e)

5- AWS Glue Jobs are created to move data from rds to redshift 
![aws_glue_job](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/472a57ff-ad28-4465-8221-5e221fe362a2)

6- Star Schema tables are created in redshift and unloaded to S3 bucket using attached codes redshift.py, redshift_sql.py 
![Star_Schema_Diagram](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/6b95ff4f-c3e0-4f69-9ec0-675ab090f022)


![s3_bucket](https://github.com/Somaya-Abdou/ETL-Data-warehousing-simpsons/assets/87602679/5be4341c-7f98-489a-943b-63f5486f7a32)



