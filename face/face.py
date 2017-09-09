import requests,json
from flask import jsonify

def detect(key,image_url):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
    		'url' : image_url
	}
	url = base+'detect'
	response = requests.post(url,headers = headers,json = body)
	# face_ids = list()
	# for i in response.json():
	# 	face_ids.append(str(i['faceId']))
	return response.json()

def group(key,faceIds):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
			'faceIds' : faceIds
	}
	url = base+'group'

	response = requests.post(url,headers = headers, json = body)
	return response.json()

def identify2(key,image_url,group):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
    		'url' : image_url
	}
	url = base+'detect'
	response = requests.post(url,headers = headers,json = body)
	fo = open("/home/parth/Code/100cent/FlaskApp/FlaskApp/face/foo.txt", "rw+")
	fo.write(response.text)
	face_ids = list()
	for i in response.json():
		if not 'faceId' in i:
			return 'No face Found'
		face_ids.append(str(i['faceId']))
	
	body = {
        	'personGroupId' : group,
        	'faceIds' : face_ids,
        	'maxNumOfCandidatesReturned' : 5,
    		'confidenceThreshold' : 0.5
	}
	url = base+'identify'

	response2 = requests.post(url,json = body, headers = headers)
	result = list()
	cnt = 0
	for j in response.json():
		for i in response2.json():
			if all([len(i['candidates']) > 0, j['faceId'] == i['faceId']]):
				result.append((i['candidates'][0]['personId'], j['faceRectangle']))
	r = dict()
	for i in result:
		r[str(cnt)] = {'personId' : i[0], 'face' : i[1]}
		cnt += 1
	return r


def identify(key,image_url,group):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
    		'url' : image_url
	}
	url = base+'detect'
	response = requests.post(url,headers = headers,json = body)
	#return jsonify(**response.json())
	face_ids = list()
	for i in response.json():
		if not 'faceId' in i:
			return 'No face Found'
		face_ids.append(str(i['faceId']))
	body = {
        	'personGroupId' : group,
        	'faceIds' : face_ids,
        	'maxNumOfCandidatesReturned' : 5,
    		'confidenceThreshold' : 0.5
	}
	url = base+'identify'

	response = requests.post(url,json = body, headers = headers)
	return response.json()

def verify(key, faceId, personId, personGroupId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
			'faceId' : faceId,
			'personId' : personId,
			'personGroupId' : personGroupId
	}
	url = base+'verify'
	response = requests.post(url,headers = headers, json = body)
	return response.json()

def findSimilar(key, face_id, face_ids, maxNumOfCandidatesReturned = 10,mode ='matchPerson'):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
			'faceId' : face_id,
			'faceIds' : face_ids,
			'maxNumOfCandidatesReturned' : maxNumOfCandidatesReturned,
			'mode' : mode
	}
	url = base+'findsimilars'

	response = requests.post(url,json = body, headers = headers)
	return response.json()
