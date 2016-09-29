#!/usr/bin/python3
#coding:utf-8

import urllib
import urllib2
import traceback
import json

accessToken = "AAEAAH_qAbJTLWN03dqOTD2rQmM_C0SpaPxnAiu9xpXdv39oqg5kdeWz1ipIJBsCLpskISAircLmZ9CNUdEZZNlNG_LNGntivnhicep7DfDD7VpAp0sUVuoulvRM5V0w-6_DmGtT3CyambztSMeVCsPz11sxxLVjrMbsTL-pVQGqNdnWgMwvVjMCUAhsAOY9q1Mtr8YSCPq1i-TtyLORFWbMsJXQvvdYbrGPmFTEjsS9EwLqK4PSAFVAbNiH523QNmqnfdpV6d8ydQQMGBp-w9AZRdOlV_pUCOyu022CMb_F5xq_tuavwzfs2L_8XfwhVFV0JTaOZPOmLN2j1zJFwYY00wrEAQAAAAEAAKCmOlQaxBAU8j5D-Fx3UfqdeODP-3N4To-x3OMW21VwlwM8f4rNpWoUum5wiL8OGKYIKaWahtyzN8Hor72c4GEqYaojU9f1djWLlS_qnlADCXS26p9aJgDG1jGw1O9fQQDjBbVCz3ESx-5QmMiGAe1GkIE2i5S63CPlurbbIgiDlQVuWmm6K8lFc8Xv2WIFZqhG7GVx1arCPu1fYMf0xrlcjPlrMFvSbA_ucUYSo2EthigU5T3DSU6VOfQZ8JW6F0SK76RQJAbcygt9JYYulLrXLFFgMXo3I8FUpZlsJ5XIR119KTb9jR0pzWV_3w6Mx0wIH0Y-NCPj4ftDr-rKJVckuL4IB0O-a0zCXVlsftfPRGz7Obn31QAei7oLBNtEgYxE2-69U_hsuET008dhUuo20aA1bm5uxMGSNA-qCoYnIJQOLclE2mUdAsHU4BRlk0wAtQLd-0HkHv9qpiZ9FT_tQ2LOJKgB9qG3aR8dHrtXvCPcWscXutdYASqBW7lL07TfZXijXLGT9bVSfDS8oMbCiOrV4-d8oPUsWdc8mmcx2Fk3NYJUNmZSDRyxZ4bB3gYaHpPEuKGbIHskYLoBoKs"

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
		print "Access Token:\n", sourceCode["access_token"]
	except Exception as e:
		print traceback.format_exc()
	
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
		with open("./thinkphp.pdf", "rb") as f:
			data = f.read()
		request = urllib2.Request(url="https://api.easypdfcloud.com/v1/workflows/0000000005385BCA/jobs?file=thinkphp.pdf&start=true&test=false", data=data, headers=headers)
		request.get_method = lambda: 'PUT'
		sourceCode  = json.loads(urllib2.urlopen(request).read())
		print "jobID:\n", sourceCode["jobID"]
	except Exception as e:
		print traceback.format_exc()

jobID = "000000000060925B"
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
		print "Finished Flag:\n", sourceCode["finished"] # True
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
		print sourceCode
	except Exception as e:
		print traceback.format_exc()
		

def main():
	#getAccessToken()
	#createJob()
	#waitJobCompletion()
	downloadFile()	 #python pdf2html.py > a.zip    then unzip the zip file.

if __name__ == '__main__':
	main()