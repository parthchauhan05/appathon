from flask import *
import face as mcs
import pyrebase,os
from subprocess import check_output
app = Flask(__name__)
config = {
    'apiKey': "AIzaSyA1Q1RqHnR6APvwqzSZdoDEzyCyQXcZtFg",
    'authDomain': "appathon-be050.firebaseapp.com",
    'databaseURL': "https://appathon-be050.firebaseio.com",
    'projectId': "appathon-be050",
    'storageBucket': "",
    'messagingSenderId': "1085333713854"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
key = '21a982d979d04214ba2bd89eadacbf5c'
group = 'appathon'
nameoffile = len(db.child('appathon').child('photos').get().val())
nameofperson = 0
path = check_output(['hostname', '--all-ip-addresses']).split(' ')[0]+':8000'

@app.route('/')
def home():
    return "<h2> Welcome to Appathon by WIE. </h2> <h4> We are team Invincibles</h4>"

@app.route('/creategroup')
def creategroup():
    group = request.args['data']
    r = mcs.person_group.create(mcs_key,group)
    return 'No one created' if r == 'None' else 'Group '+group+' created'

@app.route('/addperson', methods = ['POST'])
def addperson():
    b = request.form['img']
    f = request.form['format']
    name = request.form['name']
    fh = open(str(nameoffile)+"."+f, "wb")
    fh.write(bytearray(b,'utf8').decode('base64'))
    fh.close()
    face_url = path+'/'+str(nameoffile)+'.'+f
    nameoffile += 1
    d = mcsAPI.face.detect(key,url)
    if len(d) == 0:
        return 'Upload another Image'
    else:
        person = mcs.person.create(key,group,name)['personId']
        mcs.person.addFace(key,group,name,face_url)
        db.child('appathon').child('users').child(str(nameofperson)).set(
            {
                'name':name,
                'mcs_id':person,
                'image_path':face_url
            }
        )
        nameofperson += 1
    return 'Person Added Successfully'

@app.route('/upload',methods=['POST'])
def upload():
    data = dict()
    b = request.form['img']
    f = request.form['format']
    #name = request.form['name']
    location = request.form['location']
    dict['location'] = location
    if event in request.form:
        event = request.form['event']
        dict['event'] = event
    
    event = request.form['event']
    fh = open(str(nameoffile)+"."+f, "wb")
    fh.write(bytearray(b,'utf8').decode('base64'))
    fh.close()
    face_url = path+'/'+str(nameoffile)+'.'+f
    data['id'] = nameoffile
    data['path'] = face_url
    db.child('appathon').child('photos').child(nameoffile).set(data)
    d = mcsAPI.face.detect(key,face_url)
    if len(d) != 0:
        mcsAPI.personGroup.train(key,group)
        trained = False
        while not trained:
            if mcsAPI.personGroup.trainStatus(key,group)['status'] == 'succeeded' :
                trained = True

        face_ids = mcsAPI.face.identify(key,face_url,group)
    else:
        for i in 
    nameoffile += 1
    return

@app.route('/test',methods=['POST'])
def test():
    return str(len(db.child('appathon').child('photos').get().val()))
     
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)
