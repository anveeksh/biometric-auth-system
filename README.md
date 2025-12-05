# 🔐 Hand Biometric Authentication System

A real-time biometric authentication system using hand recognition through webcam. Built just for fun as a weekend project!

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Features

- **Real-time Hand Recognition**: Captures hand geometry through webcam
- **Biometric Authentication**: Uses MediaPipe for feature extraction
- **Secure Storage**: Encrypted biometric templates with SHA-256 hashing
- **Privacy-First**: No raw images stored, only encrypted templates
- **Web Interface**: Clean and responsive Flask-based UI
- **Session Management**: Secure user sessions

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Computer Vision**: OpenCV, MediaPipe
- **Security**: SHA-256 hashing, encrypted templates
- **Frontend**: HTML, CSS, JavaScript

## 📋 Prerequisites

- Python 3.8 - 3.11 (MediaPipe compatibility)
- Webcam
- Modern web browser (Chrome recommended)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/biometric-auth-system.git
cd biometric-auth-system
```

### 2. Create virtual environment

**Using venv:**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**Using conda:**
```bash
conda create -n biometric python=3.10 -y
conda activate biometric
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Navigate to: `http://127.0.0.1:5000`

## 📖 Usage

### Registration
1. Click "Register here" on the login page
2. Enter a username
3. Click "Start Camera" and allow camera access
4. Show your open hand clearly to the camera
5. Click "Capture Hand"
6. Click "Register" to complete registration

### Login
1. Enter your registered username
2. Click "Start Camera"
3. Show your hand to the camera
4. Click "Capture Hand"
5. Click "Login" to authenticate

## 📁 Project Structure

```
biometric-auth-system/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── templates/                  # HTML templates
│   ├── index.html             # Login page
│   ├── register.html          # Registration page
│   └── dashboard.html         # Dashboard after login
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Styling
│   └── js/
│       └── script.js          # JavaScript utilities
│
├── biometric_data/            # User data storage
│   └── users.json             # Encrypted biometric templates
│
└── utils/                      # Helper modules
    ├── __init__.py
    ├── hand_recognition.py    # Hand detection & feature extraction
    └── security.py            # Encryption & verification
```

## 🔒 Security Features

- **No Raw Data Storage**: Only encrypted biometric templates are stored
- **SHA-256 Hashing**: Secure hash generation for templates
- **Local Processing**: All biometric processing happens locally
- **Session Security**: Flask session management for authenticated users
- **Privacy-Preserving**: No images transmitted or stored

## 🎨 Screenshots

### Login Page
Clean interface with real-time camera feed and authentication controls.

### Dashboard
Successful authentication displays user information and security features.

## ⚙️ Configuration

You can modify settings in `app.py`:

- **Port**: Change `port=5000` to your preferred port
- **Host**: Change `host='127.0.0.1'` for network access
- **Secret Key**: Update `app.secret_key` for production

## 🐛 Troubleshooting

### Camera not working
- Ensure browser has camera permissions
- Check if another application is using the camera
- Try a different browser (Chrome recommended)

### "No hand detected" error
- Ensure good lighting conditions
- Show your open palm clearly
- Keep hand steady for 2-3 seconds
- Move closer to the camera

### MediaPipe installation issues
- MediaPipe requires Python 3.8-3.11
- Use conda environment with Python 3.10
- Check your Python version: `python --version`

## 🚧 Limitations

- Single hand detection only
- Requires good lighting conditions
- Works best with plain backgrounds
- Not suitable for production security (educational purpose)

## 🔮 Future Enhancements

- [ ] Multi-factor authentication (hand + face)
- [ ] Liveness detection to prevent spoofing
- [ ] Support for multiple hand poses
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Advanced encryption (AES-256)
- [ ] Mobile app version
- [ ] Docker containerization

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Author & Credits
**Developed by:**
**👨‍💻 Anveeksh Mahesh Rao**
**Cybersecurity Engineer | Founder of Cyber Tech Associates | Researcher | Educator**
### Who is Anveeksh Mahesh Rao
Anveeksh Mahesh Rao is a passionate Cybersecurity Professional, Cyber Crime Investigator, and Entrepreneur with expertise spanning digital forensics, vulnerability assessment, penetration testing, and cybersecurity education.

He is the Founder and Managing Director of Cyber Tech Associates, a firm providing end-to-end cybersecurity consulting, training, and digital investigation services. Under his leadership, Cyber Tech Associates has trained and empowered over 10,000 students, professionals, and institutions across India through workshops, seminars, and awareness programs on Cyber Crime Investigation and Cyber Forensics.

Anveeksh holds a B.Tech in Cyber Security and Cyber Forensics from Srinivas University and professional certifications including CISCO CCST. His career reflects a balance between technical expertise and strategic leadership, making him a driving force in cybersecurity innovation and education.

He has served as Guest Faculty and Keynote Speaker at numerous universities and organizations, inspiring the next generation of cybersecurity professionals through real-world insights and practical skill development.

Beyond technology, Anveeksh is also a motivational speaker and mentor, using his platform to share stories of career growth, entrepreneurship, and digital safety awareness.

📍 LinkedIn: www.linkedin.com/in/anveekshmrao

📧 Email: raoanveeksh@gmail.com

🌐 Website: www.anveekshmrao.com

## 🏁 License
This project is released under the MIT License — free for research, academic, and authorized commercial use.
```bash
MIT License © 2025 Anveeksh Mahesh Rao
Permission is granted to use, copy, modify, and distribute this software for lawful, authorized purposes only.
```

## ⚠️ Disclaimer

This project is created **just for fun** and educational purposes. It should **NOT** be used for actual security systems without proper security audits and enhancements.

---

**Built with ❤️ as a weekend project!**

If you found this interesting, give it a ⭐ on GitHub!
