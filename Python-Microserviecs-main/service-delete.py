from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json
def _find_user(user, username):
    data = [x for x in username if x["user"]==user]
    return data

@app.route('/delete', methods=['DELETE'])
def delete():
    user = request.form.get('username')
    # return jsonify(user)
    _user = us.find_username(user)
    data = [x for x in _user if x["user"]==user]
    if data:
        us.user_delete(user)
        return jsonify({'message': 'Delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot delete user.'}), 401



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1