// Camera and Biometric Capture Utilities

class BiometricCapture {
    constructor(videoElement, canvasElement) {
        this.video = videoElement;
        this.canvas = canvasElement;
        this.stream = null;
        this.capturedImage = null;
    }

    async startCamera() {
        try {
            this.stream = await navigator.mediaDevices.getUserMedia({ 
                video: { 
                    width: { ideal: 640 },
                    height: { ideal: 480 },
                    facingMode: 'user'
                } 
            });
            this.video.srcObject = this.stream;
            return { success: true, message: 'Camera started successfully' };
        } catch (error) {
            return { 
                success: false, 
                message: `Camera error: ${error.message}` 
            };
        }
    }

    captureFrame() {
        if (!this.stream) {
            return { 
                success: false, 
                message: 'Camera not started' 
            };
        }

        this.canvas.width = this.video.videoWidth;
        this.canvas.height = this.video.videoHeight;
        const ctx = this.canvas.getContext('2d');
        ctx.drawImage(this.video, 0, 0);
        
        this.capturedImage = this.canvas.toDataURL('image/jpeg', 0.95);
        
        return { 
            success: true, 
            message: 'Frame captured',
            image: this.capturedImage
        };
    }

    getCapturedImage() {
        return this.capturedImage;
    }

    stopCamera() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
            this.stream = null;
            this.video.srcObject = null;
        }
    }

    isActive() {
        return this.stream !== null;
    }
}

// API Communication Helper
class BiometricAPI {
    static async register(username, imageData) {
        try {
            const response = await fetch('/api/register', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json' 
                },
                body: JSON.stringify({
                    username: username,
                    image: imageData
                })
            });

            return await response.json();
        } catch (error) {
            return { 
                success: false, 
                message: `Network error: ${error.message}` 
            };
        }
    }

    static async login(username, imageData) {
        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json' 
                },
                body: JSON.stringify({
                    username: username,
                    image: imageData
                })
            });

            return await response.json();
        } catch (error) {
            return { 
                success: false, 
                message: `Network error: ${error.message}` 
            };
        }
    }

    static async logout() {
        window.location.href = '/api/logout';
    }
}

// UI Helper Functions
class UIHelper {
    static showMessage(element, message, type) {
        element.textContent = message;
        element.className = `message ${type}`;
        element.style.display = 'block';
    }

    static hideMessage(element) {
        element.style.display = 'none';
    }

    static enableButton(button) {
        button.disabled = false;
        button.style.opacity = '1';
    }

    static disableButton(button) {
        button.disabled = true;
        button.style.opacity = '0.5';
    }

    static showLoading(button, originalText) {
        button.setAttribute('data-original-text', originalText);
        button.textContent = 'Processing...';
        button.disabled = true;
    }

    static hideLoading(button) {
        const originalText = button.getAttribute('data-original-text');
        if (originalText) {
            button.textContent = originalText;
        }
        button.disabled = false;
    }
}

// Form Validation
class FormValidator {
    static validateUsername(username) {
        if (!username || username.trim() === '') {
            return { 
                valid: false, 
                message: 'Username is required' 
            };
        }

        if (username.length < 3) {
            return { 
                valid: false, 
                message: 'Username must be at least 3 characters' 
            };
        }

        if (username.length > 20) {
            return { 
                valid: false, 
                message: 'Username must be less than 20 characters' 
            };
        }

        const usernameRegex = /^[a-zA-Z0-9_-]+$/;
        if (!usernameRegex.test(username)) {
            return { 
                valid: false, 
                message: 'Username can only contain letters, numbers, hyphens, and underscores' 
            };
        }

        return { 
            valid: true, 
            message: 'Valid username' 
        };
    }

    static validateImageCapture(imageData) {
        if (!imageData) {
            return { 
                valid: false, 
                message: 'Please capture your hand biometric first' 
            };
        }

        return { 
            valid: true, 
            message: 'Image captured' 
        };
    }
}

// Export for use in HTML files (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        BiometricCapture,
        BiometricAPI,
        UIHelper,
        FormValidator
    };
}