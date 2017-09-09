import requests, json

def addFace(key,faceListId,image_url):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
    		'url' : image_url
	}
	url = base+'facelists/' + faceListId + '/persistedFaces'
	response = requests.post(url, headers = headers, json = body)
	return response.json()

def create(key,faceListId,name, userData = None):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
			'name' : name,
			'userData' : userData
	}
	url = base+'facelists/' + faceListId
	response = requests.put(url, headers = headers, json = body)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def delete(key,faceListId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'facelists/' + faceListId
	response = requests.delete(url, headers = headers)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def faceDelete(key,faceListId,persistedFaceId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'facelists/' + faceListId + '/persistedFaces' + persistedFaceId
	response = requests.delete(url, headers = headers)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def get(key, faceListId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'facelists/' + faceListId
	response = requests.get(url, headers = headers)
	return response.json()

def list(key):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'facelists/' 
	response = requests.get(url, headers = headers)
	return response.json()

def update(key,faceListId,name, userData = None):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = { 
				'Ocp-Apim-Subscription-Key': key,
				'Content-Type' : 'application/json'
	}
	body = {
			'name' : name,
			'userData' : userData
	}
	url = base+'facelists/' + faceListId
	response = requests.patch(url, headers = headers, json = body)
	if response.status_code == 200:
		return None
	else:
		return response.json()