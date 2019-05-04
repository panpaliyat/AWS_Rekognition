# SJSU CS 218 Spring 2019 TEAM1

import json
import boto3

def lambda_handler(event, context):

	bucket = 'testbucket013712660'
	photo = event['body']
	region = 'us-west-2'
	
	client=boto3.client('rekognition', region)
	response = client.detect_text(
		Image = {
			"S3Object" : {
				"Bucket" : bucket,
				"Name" : photo
			}
		}
		)
		
	labels = ""

	for label in response['TextDetections']:
		if 'ParentId' in label:
	 		labels += label['DetectedText']+" "
		
	final_response = {
		"statusCode": 200,
		"statusDescription": "200 OK",
		"isBase64Encoded": False,
		"headers": {
			"Content-Type": "text/plain; charset=utf-8"
	  },
	  "body": "Extracted Text : " + labels
    }
    
	return final_response
