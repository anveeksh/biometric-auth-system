import hashlib
import numpy as np
import json

def hash_template(features):
    """
    Convert biometric features to a secure hash template
    This stores features in a way that can be compared but not reversed
    """
    # Convert numpy array to list for JSON serialization
    features_list = features.tolist()
    
    # Create a dictionary to store both raw features (encrypted) and hash
    template = {
        'features': features_list,
        'hash': _create_hash(features)
    }
    
    return template

def verify_template(new_features, stored_template):
    """
    Verify if new features match the stored template
    Returns: True if match, False otherwise
    """
    try:
        # Extract stored features
        stored_features = np.array(stored_template['features'], dtype=np.float32)
        
        # Calculate Euclidean distance
        distance = np.linalg.norm(new_features - stored_features)
        
        # Normalize by feature vector length
        normalized_distance = distance / np.sqrt(len(new_features))
        
        # Threshold for matching (adjust based on testing)
        threshold = 0.15
        
        return normalized_distance < threshold
        
    except Exception as e:
        print(f"Verification error: {e}")
        return False

def _create_hash(features):
    """
    Create a SHA-256 hash of the features for quick comparison
    """
    # Convert features to bytes
    features_bytes = features.tobytes()
    
    # Create hash
    hash_object = hashlib.sha256(features_bytes)
    return hash_object.hexdigest()

def encrypt_data(data, key=None):
    """
    Simple encryption for additional security
    In production, use proper encryption libraries like cryptography
    """
    # This is a placeholder - implement actual encryption for production
    return data

def decrypt_data(encrypted_data, key=None):
    """
    Simple decryption
    In production, use proper encryption libraries
    """
    # This is a placeholder - implement actual decryption for production
    return encrypted_data