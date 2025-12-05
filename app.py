from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import cv2
import base64
import numpy as np
import json
import os
from datetime import datetime
from utils.hand_recognition import HandRecognition
from utils.security import hash_template, verify_template

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize hand recognition
hand_recognizer = HandRecognition()

# Path for storing user data
USER_DATA_FILE = 'biometric_data/users.json'

def load_users():
    """Load user data from JSON file"""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save user data to JSON file"""
    os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/register')
def register_page():
    """Registration page"""
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard page (only accessible after login)"""
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', username=session['user'])

@app.route('/api/register', methods=['POST'])
def register():
    """Register new user with hand biometric"""
    try:
        data = request.get_json()
        username = data.get('username')
        image_data = data.get('image')
        
        if not username or not image_data:
            return jsonify({'success': False, 'message': 'Missing username or image'})
        
        # Load existing users
        users = load_users()
        
        # Check if user already exists
        if username in users:
            return jsonify({'success': False, 'message': 'Username already exists'})
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data.split(',')[1])
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Extract hand features
        features = hand_recognizer.extract_features(img)
        
        if features is None:
            return jsonify({'success': False, 'message': 'No hand detected. Please show your hand clearly.'})
        
        # Hash the biometric template
        hashed_template = hash_template(features)
        
        # Save user data
        users[username] = {
            'template': hashed_template,
            'registered_at': datetime.now().isoformat()
        }
        save_users(users)
        
        return jsonify({'success': True, 'message': 'Registration successful!'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

@app.route('/api/login', methods=['POST'])
def login():
    """Login user with hand biometric"""
    try:
        data = request.get_json()
        username = data.get('username')
        image_data = data.get('image')
        
        if not username or not image_data:
            return jsonify({'success': False, 'message': 'Missing username or image'})
        
        # Load users
        users = load_users()
        
        # Check if user exists
        if username not in users:
            return jsonify({'success': False, 'message': 'User not found'})
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data.split(',')[1])
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Extract hand features
        features = hand_recognizer.extract_features(img)
        
        if features is None:
            return jsonify({'success': False, 'message': 'No hand detected. Please show your hand clearly.'})
        
        # Verify against stored template
        stored_template = users[username]['template']
        if verify_template(features, stored_template):
            session['user'] = username
            return jsonify({'success': True, 'message': 'Login successful!'})
        else:
            return jsonify({'success': False, 'message': 'Biometric verification failed'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

@app.route('/api/logout')
def logout():
    """Logout user"""
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)