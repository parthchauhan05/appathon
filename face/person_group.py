import requests, json

def create(key,name,userData=None):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	url = base+'persongroups/' + name
	headers = {
				'Content-Type' : 'application/json',
				'Ocp-Apim-Subscription-Key': key
	}
	body = {
			'name' : name,
			'userData' : userData
	}
	response = requests.put(url,headers = headers, json = body)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def list(key):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups'
	response = requests.get(url,headers = headers)
	return response.json()

def delete(key,group_id):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key' : key
	}
	url = base+'persongroups/'+group_id
	response = requests.delete(url,headers = headers)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def trainStatus(key,personGroupId):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'persongroups/' + personGroupId + '/training'
	response = requests.get(url,headers = headers)
	return response.json()

def update(key,name,userData):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Content-Type' : 'application/json',
				'Ocp-Apim-Subscription-Key': key
	}
	body = {
			'name' : name,
			'userData' : userData
	}
	url = base+'persongroups/' + personGroupId
	response = requests.patch(url, headers = headers, json = body)
	if response.status_code == 200:
		return None
	else:
		return response.json()

def train(key,group):
	base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	headers = {
				'Ocp-Apim-Subscription-Key': key
	}
	url = base+'persongroups/'+ group +'/train'

	response = requests.post(url,headers = headers)
	if response.status_code == 202:
		return None
	else:
		return response.json()
