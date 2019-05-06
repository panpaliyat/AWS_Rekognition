# SJSU CS 218 Spring 2019 TEAM1
import boto
import urllib
import urllib2
from boto.s3.key import Key

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method== 'GET':
		return render_template('index.html')
	
    if request.method == 'POST':        
        s3 = boto.connect_s3()       
        bucket_name = 'testbucket013712660'
        bucket = s3.get_bucket(bucket_name)
        k = Key(bucket)        
        files = request.files.getlist('file')
        for file in files:            
            contents = file.read()
            k.key = file.filename
            k.set_contents_from_string(contents)
	
	    url=''
	    if('DetectObject' in request.form and request.form['DetectObject']=='DetectObject'):
		    url = 'http://testalb-173425431.us-west-1.elb.amazonaws.com/lambda/ObjectDetection'
	    else:
		    url = 'http://testalb-173425431.us-west-1.elb.amazonaws.com/lambda/TextExtraction'
	    df=str(k.key)
	    print(df)
	    req = urllib2.Request(url)
	    req.add_header("Content-Type", 'text/plain')
	    response = urllib2.urlopen(req,df)
	    the_page = response.read()
	    print(the_page)
	    return the_page

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int('80'),
        debug=True
    )
