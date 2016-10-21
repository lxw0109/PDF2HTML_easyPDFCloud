#!/usr/bin/python3
#coding:utf-8
#References: https://www.easypdfcloud.com/developer/reference

import urllib
import urllib2
import traceback
import json
import sys

def getAccessToken():
	"""
	Create a new Access Token.
	"""
	try:
		headers = {"User-Agent" : "Mozilla/5.0i (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"} 
		data = { "grant_type" : "client_credentials", "client_id" : "2e203051b6594f5a9763b5ffbeed3aa9", "client_secret" : "B5C6434F7F62B1229057C798217DD7D8BBA9B3A8FC76F0DC3D7072E195B366D7", "scope":"epc.api"}
		formData = urllib.urlencode(data)
		print "formData: ", formData
		request = urllib2.Request(url="https://www.easypdfcloud.com/oauth2/token", data=formData, headers=headers)
		sourceCode  = json.loads(urllib2.urlopen(request).read())
		print "Get Access Token:\n", sourceCode["access_token"]
		return sourceCode["access_token"]
	except Exception as e:
		print traceback.format_exc()

try:
	print "Getting Access Token."
	accessToken = getAccessToken()
except Exception as e:
	sys.exit(1)

def createJob():
	"""
	POST/PUT a pdf file. And create a new job to convert this pdf file.
	"""
	try:
		"""
		PUT https://api.easypdfcloud.com/v1/workflows/0000000005385BCA/jobs?file=&start=true&test=true
		Authorization: Bearer AAEAABwFhLE3zV8H1W4T83z2kmUFu_hY_TgRzBimGhOpss4MfzbpgrONFQs7L3hNxZrdtVVubQ_9Wv7-OtGwYleijwDVYgOXVk7ZUnVhDoaLHpNXSDR0IDFBP8aiRCFwafjPasXTXAPyQNL1I67XJ51m5cZKEsWpUM5rL5EJc4s_GEdMbqPlW-jKH1L0EYw9qwehJzSl15S83FKmr3tfSkLXAhaPMFKyDrO0vZrqkj_qsaCHtno5qFJcoWYWefFAIYFkn9rhdBUecbcpq99lp5tehlqBoZvJG34Qx-v5nGRZ_0Z4gjukpmMHwlqEBzd1DQeLo44CHwRm834vtUofvtBb9R7EAQAAAAEAACI21CkCsNaxRZB2Eyeg1jxy68MyI6hh1y6zNtzLfyozG9Oe1dk4jV-a5OJjm8dnT-SesIiKPuf1Kk6cRxlvHEunLe03q9a17jsadbvD3nsFOd_6zlJ80MyN23l1yAa0lcH7XrmJoxhHDtv1cLcGInTPttKXTewoT7AEmMDX2eZlnVl2nkj1aC0ErgDSiwlycOeVmrjXZKE3bBe2pJe5HeeKli3OdCHsMfnfV6JkPvfmXYET3lyQDIy8pho5aPcFewyIaHI9st8iFVuGWDX2J_QIFWhJn1QqPuKP5IRqdTE5RoED4SM6pQm-XU0PE3f2FziF4BafMnH7XJ_ezYOLHdaCI_scdujjDPKamlawVqqWcThtPZ67YqsrroT7-gsLtxontMvLBtM8sy7kD9gVzIuaFWB-jFeAzJz9mlh33P3r9KKPnF0zslOVVV87AsB-r0RpYiGPwL9T3ProzcJbR7iG5ZXAqxc8xQorLxwAOrc8L1HlrqYiAMviFIbdUFXdXcc1C6P6dzRrxxxsvNuGQIIFonAYYWC9kmtSPuS5eKMqgt0EPORXvHOc6AVCxbSPdxG4NcqYGYv5JxzHTKxp7o0
		Content-Type: application/pdf

		<The contents of the  will be inserted here>
		"""
		headers = {"User-Agent" : "Mozilla/5.0i (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
		"Authorization" : "Bearer " + accessToken,
		} 

		#data should be the content of the pdf file.
		#fileName = "table_down.pdf"
		fileName = "table.pdf"
		with open(fileName, "rb") as f:
			data = f.read()
		myURL = "https://api.easypdfcloud.com/v1/workflows/0000000005385BCA/jobs?file={0}&start=true&test=false".format(fileName)
		#myURL = "https://api.easypdfcloud.com/v1/workflows/0000000005385B9B/jobs?file={0}&start=true&test=false".format(fileName)
                
		request = urllib2.Request(url=myURL, data=data, headers=headers)
		request.get_method = lambda: 'PUT'
		sourceCode  = json.loads(urllib2.urlopen(request).read())
		print "Get jobID:\n", sourceCode["jobID"]
		return sourceCode["jobID"]
	except Exception as e:
		print traceback.format_exc()

try:
	print "Creating Job."
	jobID = createJob()
except Exception as e:
	sys.exit(1)

def waitJobCompletion(): #0000000000609211
	"""
	Judge whether the job has finished.
	"""
	try:
		"""
		POST https://api.easypdfcloud.com/v1/jobs/00000000006090C0/event HTTP/1.1
		Authorization: Bearer access-token
		"""
		headers = {"User-Agent" : "Mozilla/5.0i (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
		"Authorization" : "Bearer " + accessToken,
		} 
		request = urllib2.Request(url="https://api.easypdfcloud.com/v1/jobs/"+ jobID + "/event", headers=headers)
		request.get_method = lambda: 'POST'
		sourceCode = json.loads(urllib2.urlopen(request).read())
		#print "Finished Flag:\n", sourceCode["finished"] # True
		return sourceCode["finished"]
	except Exception as e:
		print traceback.format_exc()

def downloadFile():
	try:
		"""
		GET https://api.easypdfcloud.com/v1/jobs/0000000000609164/output?type=file HTTP/1.1
		Authorization: Bearer access-token
		"""
		headers = {"User-Agent" : "Mozilla/5.0i (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
		"Authorization" : "Bearer  " + accessToken,
		} 
		request = urllib2.Request(url="https://api.easypdfcloud.com/v1/jobs/"+ jobID + "/output?type=file", headers=headers)
		request.get_method = lambda: 'GET'
		sourceCode = urllib2.urlopen(request).read()
		#print sourceCode
		with open("./" + jobID + ".zip", "wr") as f:
			f.write(sourceCode)

	except Exception as e:
		print traceback.format_exc()
		
def main():
	print "In main()."
	try:
		while not waitJobCompletion():
			pass
	except Exception as e:
		sys.exit(1)
	print "Job completed!"
	downloadFile()

if __name__ == '__main__':
	main()
