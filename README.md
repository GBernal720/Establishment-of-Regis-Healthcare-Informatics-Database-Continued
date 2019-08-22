# Gilbert Anthony Bernal MSDS-696 Data Science Project

## Overview
The data science project that was worked on for the Regis MSDS 696 practicum is titled "Establishment of Regis Healthcare Informatics Database – Continued". The goal of this project was to continue from the last data science project and to complete building the database for the Regis Health Informatics school. In the previous project I picked the best database to use based on the requirements and created python codes to create database tables based of CSV files and upload the data a from these files to its unique table. After this an analysis was done to show a proof on concept on how these codes work an can be used. In this project continuation new python codes were created to allow for multiple file types to be used with the previous code used to create tables. This allows users the ability to use different file types instead of just a single one. A new code was also created to add data governance to the database. This makes it so the database stays clean by removing tables that are not being used any more. After the codes were created the PostgreSQL database was then created on the Regis sever. The codes used for the local database where then copied over to the server for testing. Chron scheduler was then added to the database as well to allow for code automation. This created a way for the Python codes to run on a consistent time. A HTML form was then created to allow users to upload files to the database. This makes it so the user can upload a file from their local computer to the Regis server for the scheduled codes to take the uploaded file and created their unique table for them. An analysis on Dengue fever cases in the Philippines was then done to show a proof of concept on how these codes and database could be used by students in the Regis Health Informatics School. 

## Requirements & Goal
For this project continuation there were numerous goals and requirements. The first goal was to create a way to allow for multiple data formats to be used with the previous project code. The previous code only allowed for CSV files. After looking through multiple health care organization databases CSV, JSON, and Excel were the most common formats that the databases stored their data in. Since the previous project’s codes took CSV files a code had to updated or created to allow for JSON and Excel files to run with the previous project codes. The next goal was to create a python code to add data governance to the database. This needed to be done so that the database stayed clean. If data governance was not added to this database, then there would be unused data on it. This unused data would take up unnecessary space that could make it harder to find data and fill up the allowed space for the database. The next goal was to create the PostgreSQL server on Regis Server. The database needed to be created on the server to test and all related codes. This had to be done to make any necessary updates to the codes as needed to make sure they ran successfully on the server. After this was done the next goal was to create a way to automate these codes on a consistent schedule. This had to be done so that if any individual were to upload a file to the server the codes needed to create their unique table would run within a reasonable time to create their table based off their file. Last goal and requirement was to create a HTML webform to allow for a file to be uploaded to the server. This webform allows users to upload a file from their local drive to the server so that their file can be created into a unique table for them to use. 
## Tools

### PostgreSQL
PostgreSQL is a free open source object-relational database system that uses the standard SQL language and extends the language with various features. The reason why this database was chosen in the previous project is because it cost nothing to download, use, and works well with CSV files. It also has a command that allows for quick CSV file upload called COPY. This command created a simple and quick way to upload the files to the table created for it. 

### Python
Python is an open source high level programming language. The reason why Python was chosen for this and the previous project is that it has various libraries that work well with PostgreSQL and has other libraries that could help with the goals of the project.
### Python Libraries Used
Below are the new Python libraries used for this project not previously used in the previous

**PANDAS:**
The PANDAS library is used to allow python to work and use data structures and data analysis tools. The reason why this library was used for this code was to take in JSON files and convert them to CSV files for the previous project codes to create a unique table for it. 

**XLRD:**
XLRD is a python library that allows python to work with Microsoft Excel spreadsheets. This library was needed in order go through an excel file, identify each sheet, and create a CSV based off each of the sheets within the file. These new CSV files are then turned into unique tables by the previous project codes. 

**TOUCH:**
The TOUCH library allows python to use a Linux command called touch. Touch allows for the creation of blank files. The was required for this project because it created a way to generate trigger files needed for the KSH files used for the Chron scheduler.  

### Chron

Chron is a UNIX tool that is used to schedule commands or script on a server to run automatically at a time the user chooses. This tool was chosen to automate the table creation and data governance codes. 

### HTML
HTML is a web-based code used to create websites. HTML was used for this project to create a webform to allow users to upload their data to the server to have a unique table created based on the file uploaded. 

### Tableau

Tableau is an analytical tool that can be used for building dashboards, live reporting, and analytics. This tool was chosen over other analytical tools because of its ability to connect directly to databases, ability to run SQL queries, built in functions, and for its ability to do complete analysis with the data loaded to the tool. 

# Part 1: Create Python Code
Two Python codes were created for this project. The two codes create where Convert.py and Database_Governance.py.

**Convert.py:** This code is used convert JSON and Excel files to a CSV file. The reason why they are being converted to CSV is because the codes used in the previous project for creating the unique tables works only with files in a  CSV format. Covering these files to a CSV instead of updating the previous code saved time, did not risk issues when updating previous code, and was the least path of resistance. This code works by using different python libraries for the file conversion. For JSON files PANDAS was used. PANDAS was chosen because of how it works with JSON files and its ability to export data frames to CSV. XLRD is used to go through each of the excel sheets within a file and covert them to a CSV file. This will turn a single excel file into a multiple CSV files depending on the number of sheets within it. The code uses an if statement to decide what library to use for conversion. 

![](Images/Convert_python.PNG)

**Database_Governance.py:** This code is used to check the age of a file that was used for creating a unique table. Based on the age of the file the code will go through and decide if the unique table created from that file needs to be deleted. If it does need to be deleted it connects to the PostgreSQL server and runs a drop table statement with the name of the of the file/table name.

![](Images/datagoverance_python.PNG)

# Part 2: Create PostgreSQL database on Regis server 
## Previous Project Issues

When working on the previous project I tried to create the PostgreSQL database on the server. When trying to do so I ran into a connection issue. When trying to connect I would either run into a timeout error. If I was able to connect, I would get disconnected after a period of time. After working to resolve this issue and testing with putty and WinSCP the issue was resolved. Once this issue was resolved the commands needed to install. Once the database was installed a new user was created along with a new database call H_INFO. Once this was done the database connections were modified to allow all users access from their local machine. 

**Step 1:** Run Commands needed for PostgreSQL database installation.

![](Images/Install_Postgre.PNG)

![](Images/complete_install.PNG)

![](Images/Postgre_Initialized.PNG)

![](Images/Start_Postgre.PNG)

**Step 2:** Create new database for health informatics school

![](Images/Create_H_INFO.PNG)

**Step 3:** Create new user

![](Images/Create_User.PNG)

**Step 4:** Open connections for database use

![](Images/open_access.PNG)

# Part 3: Copy and test all database python codes on server  

The codes created for this project have all been used on a local desktop database. To test them further for productional use they needed to be testing on the Regis server itself. All directories and codes used were copied on the server using WinSCP. Once they were copied to the server, they were then updated to use the server directories. Once this was done, they were tested and updated until they ran successfully. 

**Step 1:** Create directories needed for python codes on server

![](Images/mirror.PNG)

**Step 2:** Copy all python codes and data files for testing. 

![](Images/python_file_transafer.PNG)

![](Images/source_data.PNG)

![](Images/data_upload.PNG)

![](Images/python_file_transafer.PNG)

![](Images/completed_data_tranfer_purtty.PNG)

**Step 3:** Update files to use directories and Regis server

![](Images/up_date_gover.PNG)

![](Images/Updates_Import_CSV.PNG)

**Step 3:** Run files for testing 

![](Images/Import_CSV_Server_Test.PNG)

![](Images/Run_zoom.PNG)

![](Images/Governance_test.PNG)

**Step 4:** Check database for validation

![](Images/SQL_Database_check.PNG)

# Part 4: Install Chron scheduler on Regis server and create KSH files

To automate the table crkeation process and data governance check chon was installed on the Regis server to schedule when these codes need to run. To scheduler these codes for automation ksh files needed to be created to run the code. These codes were created for both the data governance and table creation codes. These codes were set to run on a 15 minute internal and will continue to run until a trigger file is found. Once it is found the file stops running. If there are any error an email would be sent to whoever is chosen to look into the issue. 

**Step 1:** Install Chron on Regis server

![](Images/crontab_installed.PNG)

**Step 2:** Create ksh files for both the data upload and data governance codes. 

![](Images/KSH1.PNG)

![](Images/KSH2.PNG)

**Step 3:** Add ksh files to Chron scheduler. 

![](Images/Cronjob_scheduled.PNG)

# Part 4: Create HTML webform

A webform was created to allow users to upload their data to the Regis sever from their local machine. This creates a way for students to upload their data to have a unique table created for them. 

![](Images/HTML.PNG)

![](Images/HTML_EXAMPLE.PNG)

# Part 5: Run Analysis to show proof of concept

## Overview

For this project data was obtained from two different sources. The first source was from HealthData.gov and data collected was on confirmed West Nile virus cases in different cities within California. The next source was from Los Angeles Almanac and the data collected form this source was on the total rainfall in Los Angeles recorded from the USC downtown campus. Once these sources were collected the CSV files were checked to make sure no issues would occur when the python script mention in part two was ran for to create the files needed for the analysis. The issues identified within the CSV files were in the headers. The headers had spaces in them which can cause a common issue when creating a table. To correct this the columns were renamed to make sure this issue would no occur. After that the files were renamed to use my username (gbernal) and then the name of the file. This way they would be easy to identify and remember. Once this was done the python files were ran to create the table and upload the data to the unique table created. After this was done a Tableau report was created to create the regression model, calculate the correlation and R squared values, and visually see if there was a correlation between the two. After doing this the results showed that there was no correlation between the amount of rainfall and confirmed cases of West Nile virus in Los Angeles California. 

**Step 1: Obtain Data**

West Nile Virus Source

![](Images/WNV_Site.PNG)

![](Images/WNV_Excel.PNG)

LA Rainfall Source

![](Images/LA_Rain.PNG)

![](Images/LA_Rain_Excel.PNG)

**Step 2: Clean Data and Rename files**

Two columns were seen to possibly cause an issue with the WNV excel data. Two of the columns had a space in the header. The Week Report column was removed since we are going to be doing this analysis by year and the Positive Cases columns was replaced with Postitive_Cases. 

![](Images/WNV_Excel_Clean.PNG)

![](Images/rename.PNG)

**Step 3: Run Python Import_CSV.py code**

![](Images/Run_Code.PNG)

![](Images/Table_Commands.PNG)

**Step 4: Create Query**

![](Images/Query.PNG)

**Step 5: Import Data into Tableau**

![](Images/Tableau_Connection.PNG)

![](Images/Tableau_Query.PNG)

**Step 6: Create Report**

![](Images/report_final.PNG)

![](Images/model.PNG)

# Results
When looking at the regression model created by Tableau its easy to see that our model line is not a good fit for the data used. This shows that there is no correlation between rainfall and number of confirmed cases. To check and make sure that spear man’s correlation and the R squared value were calculated. Our correlation value was at -.29 and our R-square value was at 8% . Both of these values show a weak correlation between rainfall and confirmed cases of West Nile virus. These results could be affected by the amount of data used or by the fact that the rainfall data was from a single area within LA. 

# Conclusion
Tools used and code created successfully worked as planned with no issues. The most important function COPY for the data ingestion worked as expected. The Python code also worked as expected. It created the tables based off the headers and made the correct choice for each of the column data types in the CSV file. It also uploaded the data to their unique tables with no issues. Tableau was also able to connect to the database with easy, use the query created, and created the report as needed. Overall the project was a success. 

# What’s next?

### Possible Project Ideas

* Add this project to Regis servers and add API
  * API would allow users to upload their CSV files to a directory for python codes to run and create their data tables
* Add data governance
  * Data governance would need to added to this database.
   * If not the database will get extremely messy and ill have a large amount of data stored in it that isn’t being used
* Update Import_Function.py to use other data formats
  * Make it so that the funciton can import any file regardless of its format

# References 

The World's Most Advanced Open Source Relational Database. (n.d.). Retrieved June 26, 2019, from https://www.postgresql.org/

Total Seasonal Rainfall (Precipitation). (n.d.). Retrieved June 26, 2019, from http://www.laalmanac.com/weather/we13.php

Valdez, L. (2018, October 10). Effects of rainfall on Culex mosquito population dynamics. Retrieved June 26, 2019, from https://arxiv.org/pdf/1703.08915.pdf

Welcome to Python.org. (n.d.). Retrieved June 26, 2019, from https://www.python.org/

West Nile virus. (2018, December 10). Retrieved June 26, 2019, from https://www.cdc.gov/westnile/index.html

West Nile Virus Cases, 2006-present. (2019, June 25). Retrieved June 26, 2019, from https://healthdata.gov/dataset/west-nile-virus-cases-2006-present

Youtube Presentation: https://www.youtube.com/watch?v=N-74fgEW76M&feature=youtu.be
