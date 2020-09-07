# API to Power Dashboard Using Django

A backend project to populate the frontend with data retrieved from database. Missing values handled for major columns.

## Instructions

### Installation

To install this example on your computer, clone the repository and install dependencies mentioned in requirements file.

```bash
$ git clone git@github.com:donna54/Power-Dashboard-Django.git
$ cd analysis_project
```
### Start server on localhost

```bash
$ python manage.py runserver
```

#### Note

* All routes can be tested with any software development tool like Postman.
* URL's for uploading datasets need a csv file to be sent in the request body with key as 'file'.
* A median value would be used to fill in the missing values in 'NumSubDistrictHospitals_HMIS' column of 'HospitalBedsIndia.csv' file
* The most frequent occuring number is programmed to fill the missing values appearing in 'Negative' and 'Positive' columns of 'StatewiseTestingDetails.csv' file.