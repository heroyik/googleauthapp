import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC-2cVE6OJPzgMFd8LUSyVUIS5BDFCsB9I",
    "authDomain": "authapp-dba92.firebaseapp.com",
    "projectId": "authapp-dba92",
    "storageBucket": "authapp-dba92.appspot.com",
    "messagingSenderId": "211413579154",
    "appId": "1:211413579154:web:69c18fe00a31dd3f4c3d4b",
    "measurementId": "G-09Q8WQTTRG",
    "databaseURL": "https://authapp-dba92.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

# storage.child("texts/.txt").put("1.txt")
storage.child("texts/1.txt").download(path="./",filename="downloaded.txt")