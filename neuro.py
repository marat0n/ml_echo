<<<<<<< HEAD
import tensorflow
import librosa
import librosa.display
import numpy as np

=======
>>>>>>> 63d1608acbfe90d89591b1e3e428431edba9612b
from tensorflow.keras.models import model_from_json

def neuro(arg):
    
    with open('model.json', 'r') as f:
        model = model_from_json(f.read())
   
    model.load_weights('weights.h5')

    data = []

    mfcc = []

    x, sr = librosa.load(arg)

    print(x)

    x = librosa.feature.mfcc(x, sr=sr)
    
    for val in x:
        mfcc.append(np.mean(val))

    data.append(np.array(mfcc))
    
    np.array(data)

    prediction_file = model.predict(data)

    labels = ['eng', 'rus']

    return labels[np.argmax(prediction_file[0])]
