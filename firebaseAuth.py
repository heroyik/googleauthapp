import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC-2cVE6OJPzgMFd8LUSyVUIS5BDFCsB9I",
    "authDomain": "authapp-dba92.firebaseapp.com",
    "projectId": "authapp-dba92",
    "storageBucket": "authapp-dba92.appspot.com",
    "messagingSenderId": "211413579154",
    "appId": "1:211413579154:web:69c18fe00a31dd3f4c3d4b",
    "measurementId": "G-09Q8WQTTRG",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def signup():
    email = input("Sign up...\nEnter email: ")
    password = input("Endter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("User creation succeeded")
    except:
        print("Error occurred")


def login():
    email = input("Log in...\nEnter email: ")
    password = input("Endter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Signin succeeded")
        print(auth.get_account_info(login['idToken']))
    except:
        print("Signin failed")


ans = input("Are you a new user?[y/n]")
if ans == 'y':
    signup()
elif ans == 'n':
    login()
