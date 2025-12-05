import cv2
import mediapipe as mp
import numpy as np

class HandRecognition:
    def __init__(self):
        """Initialize MediaPipe Hand detection"""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.5
        )
        
    def extract_features(self, image):
        """
        Extract hand landmarks as biometric features
        Returns: numpy array of normalized landmark positions or None if no hand detected
        """
        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the image
        results = self.hands.process(image_rgb)
        
        # Check if hand is detected
        if not results.multi_hand_landmarks:
            return None
        
        # Get the first hand landmarks
        hand_landmarks = results.multi_hand_landmarks[0]
        
        # Extract landmark coordinates (21 landmarks, each with x, y, z)
        features = []
        for landmark in hand_landmarks.landmark:
            features.extend([landmark.x, landmark.y, landmark.z])
        
        # Convert to numpy array
        features = np.array(features, dtype=np.float32)
        
        # Calculate additional geometric features
        # Distance between key points for more robust recognition
        landmarks_array = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark])
        
        # Calculate distances between fingertips and palm base
        palm_base = landmarks_array[0]  # Wrist
        fingertips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky tips
        
        distances = []
        for tip_idx in fingertips:
            dist = np.linalg.norm(landmarks_array[tip_idx] - palm_base)
            distances.append(dist)
        
        # Calculate finger lengths (ratios)
        finger_lengths = []
        finger_base_indices = [1, 5, 9, 13, 17]  # Base of each finger
        for base_idx, tip_idx in zip(finger_base_indices, fingertips):
            length = np.linalg.norm(landmarks_array[tip_idx] - landmarks_array[base_idx])
            finger_lengths.append(length)
        
        # Combine all features
        geometric_features = np.array(distances + finger_lengths, dtype=np.float32)
        combined_features = np.concatenate([features, geometric_features])
        
        return combined_features
    
    def compare_features(self, features1, features2, threshold=0.15):
        """
        Compare two feature vectors using Euclidean distance
        Returns: True if features match (distance < threshold), False otherwise
        """
        if features1 is None or features2 is None:
            return False
        
        # Ensure same length
        if len(features1) != len(features2):
            return False
        
        # Calculate Euclidean distance
        distance = np.linalg.norm(features1 - features2)
        
        # Normalize by feature vector length
        normalized_distance = distance / np.sqrt(len(features1))
        
        return normalized_distance < threshold
    
    def __del__(self):
        """Cleanup"""
        self.hands.close()