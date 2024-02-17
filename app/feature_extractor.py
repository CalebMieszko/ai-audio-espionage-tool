import librosa
import numpy as np
import os

# Define a function to extract MFCCs and other relevant features

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)

    # Add other features if needed
    return mfccs_processed

# Path to your dataset
path_to_dataset = "/path/to/your/dataset/"
files = [os.path.join(path_to_dataset, file) for file in os.listdir(
    path_to_dataset) if file.endswith('.wav')]

# Extract features for each WAV file
features = []
for file in files:
    data = extract_features(file)
    features.append(data)

# Convert to numpy array and save or proceed with additional steps
features_array = np.array(features)