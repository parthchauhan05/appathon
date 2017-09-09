import requests,json

def addFace(key,group_id,person_id,face_url):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
    		'url' : face_url
	}
	url = base+'persongroups/' + group_id + '/persons/' + person_id + '/persistedFaces'
	response = requests.post(url,json = body, headers = headers)
	return response.json()

def person(key,group,person_id):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'persongroups/' + group + '/persons/' + person_id
	respond = requests.get(url,headers = headers)
	return respond.json()

def create(key,group,name,userdata=None):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
        'name': name,
	    'userdata' : userdata
	}
	url = base+'persongroups/'+ group +'/persons'
	response = requests.post(url,json=body,headers=headers)

	if 'application/json' in response.headers['content-type'].lower():
		return response.json()

def delete(key, personGroupId, personId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups/' + personGroupId + '/persons/' + personId
	response = requests.delete(url,headers = headers)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def deleteFace(key, personGroupId, personId, persistedFaceId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups/' + personGroupId + '/persons/' + personId + '/persistedFaces/' + persistedFaceId
	response = requests.delete(url, headers = headers)
	if response.status_code == 200:
		return None
	else:
		return response.json()


def faceUpdate(key, personGroupId, personId, persistedFaceId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key,
				'Content-Type' : 'application/json'
	}
	body = {
			'userData' : userData
	}
	url = base+'persongroups/' + personGroupId + '/persons/' + personId + '/persistedFaces/' + persistedFaceId
	response = requests.patch(url,headers = headers, json = body)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def getFace(key, personGroupId, personId, persistedFaceId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups/' + personGroupId + '/persons/' + personId + '/persistedFaces/' + persistedFaceId
	response = requests.get(url, headers = headers)
	return response.json()

def list(key, personGroupId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups/' + personGroupId + '/persons/'
	return response.json()

def update(key, personGroupId, personId, name, userData):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key,
				'Content-Type' : 'application/json'
	}
	body = {
			'name' : name,
			'userData' : userData
	}
	url = base+'persongroups/' + personGroupId + '/persons/' + personId
	response = requests.patch(url,headers = headers, json = body)
	return response.json()