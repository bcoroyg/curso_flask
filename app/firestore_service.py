from firebase_admin import credentials, firestore, initialize_app

credential = credentials.ApplicationDefault()
initialize_app(credential)

db = firestore.client()


def get_users():
    users = db.collection('users').get()
    return users


def get_user(user_id):
    users = db.collection('users').document(user_id).get()
    return users


def get_todos(user_id):
    todos = db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
    return todos


def user_put(user_data):
    user_ref = db.collection('users')\
                 .document(user_data.username)
    user_ref.set({'password': user_data.password})
