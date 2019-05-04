# SJSU CS 218 Spring 2019 TEAM1

import json
import boto3

def lambda_handler(event, context):

	bucket = 'testbucket013712660'
	
	photo = event['body']
	max_labels = 10
	min_confidence = 90
	region = 'us-west-2'
	
	client=boto3.client('rekognition', region)
	response = client.detect_labels(
		Image = {
			"S3Object" : {
				"Bucket" : bucket,
				"Name" : photo
			}
		},
		MaxLabels = max_labels,
		MinConfidence = min_confidence
		)
		
	labels = ""
	for label in response['Labels']:
		labels += label['Name']+","
	
	labels = "Detected Objects: ["+labels[:-1]+"]"	
	
	final_response = {
		"statusCode": 200,
		"statusDescription": "200 OK",
		"isBase64Encoded": False,
		"headers": {
			"Content-Type": "text/html; charset=utf-8"
	  },
	  "body": labels 	
    }
    
	return final_response