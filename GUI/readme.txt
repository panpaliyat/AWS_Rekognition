This program works for "How to upload image into AWSS3 and get response from ALB for couple of services"

This code requires installation of below libraries/software/frameworks:
1)Python (2.7)
2)flask
3)boto

User should have valid AWS account in order to access any AWS components.

*Create bucket in AWS S3 with appropriate permissions. Collect the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

*Create the environment in python and install flask and boto in it.

*set these two keys as Environment variables in python:
SET AWS_ACCESS_KEY_ID=<Key_ID>
SET AWS_SECRET_ACCESS_KEY=<Access_Key_ID>

*run the program as python driver.python

