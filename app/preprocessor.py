import librosa
import numpy as np


def load_audio_files(path_to_files, label):
    features = []
    labels = []
    for file in path_to_files:
        # Load the audio file
        audio, sr = librosa.load(file, sr=16000, mono=True)
        # Extract MFCCs from the audio file
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        mfccs_processed = np.mean(mfccs.T, axis=0)

        features.append(mfccs_processed)
        labels.append(label)
    return np.array(features), np.array(labels)
