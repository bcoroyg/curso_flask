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


def put_todo(user_id, description):
    todos_collection_ref = db.collection('users')\
        .document(user_id)\
        .collection('todos')
    todos_collection_ref.add({'description': description, 'done': False})


def delete_todo(user_id, todo_id):
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.delete()
    # todo_ref = db.collection('users')\
    #             .document(user_id)\
    #             .collection('todos')\
    #             .document(todo_id)
