from firebase_admin import credentials, firestore, initialize_app

credential = credentials.ApplicationDefault()
initialize_app(credential)

db = firestore.client()

def get_users():
    users = db.collection('users').get()
    return users

def get_todos(user_id):
    todos = db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
    return todos