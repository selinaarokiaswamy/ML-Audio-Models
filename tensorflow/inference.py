import tensorflow as tf
from keras import models
import numpy as np
import sys

class_to_number = {0 : 1,  1 : 10,  2 : 100,  3 : 11,  4 : 12,  5 : 13,  6 : 14,  7 : 15,  8 : 16,  9 : 17,  10 : 18,  11 : 19,  
                   12 : 2,  13 : 20,  14 : 21,  15 : 22,  16 : 23,  17 : 24,  18 : 25,  19 : 26,  20 : 27,  21 : 28,  22 : 29,  
                   23 : 3,  24 : 30,  25 : 31,  26 : 32,  27 : 33,  28 : 34,  29 : 35,  30 : 36,  31 : 37,  32 : 38,  33 : 39,  
                   34 : 4,  35 : 40,  36 : 41,  37 : 42,  38 : 43,  39 : 44,  40 : 45,  41 : 46,  42 : 47,  43 : 48,  44 : 49,  
                   45 : 5,  46 : 50,  47 : 51,  48 : 52,  49 : 53,  50 : 54,  51 : 55,  52 : 56,  53 : 57,  54 : 58,  55 : 59,  
                   56 : 6,  57 : 60,  58 : 61,  59 : 62,  60 : 63,  61 : 64,  62 : 65,  63 : 66,  64 : 67,  65 : 68,  66 : 69,  
                   67 : 7,  68 : 70,  69 : 71,  70 : 72,  71 : 73,  72 : 74,  73 : 75,  74 : 76,  75 : 77,  76 : 78,  77 : 79,  
                   78 : 8,  79 : 80,  80 : 81,  81 : 82,  82 : 83,  83 : 84,  84 : 85,  85 : 86,  86 : 87,  87 : 88,  88 : 89,  
                   89 : 9,  90 : 90,  91 : 91,  92 : 92,  93 : 93,  94 : 94,  95 : 95,  96 : 96,  97 : 97,  98 : 98,  99 : 99}

def get_spectrogram(waveform):
  # Convert the waveform to a spectrogram via a STFT.
  spectrogram = tf.signal.stft(
      waveform, frame_length=255, frame_step=128)
  # Obtain the magnitude of the STFT.
  spectrogram = tf.abs(spectrogram)
  # Add a `channels` dimension, so that the spectrogram can be used
  # as image-like input data with convolution layers (which expect
  # shape (`batch_size`, `height`, `width`, `channels`).
  spectrogram = spectrogram[..., tf.newaxis]
  return spectrogram

def main(file_name):
    model = tf.keras.models.load_model("../ML-Audio-Models/tensorflow/marathi-40")
    #model.summary()

    x = tf.io.read_file(file_name)
    x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000,)
    x = tf.squeeze(x, axis=-1)
    waveform = x
    x = get_spectrogram(x)
    x = x[tf.newaxis,...]
    prediction = model(x)
    #print (prediction)
    print (file_name, class_to_number[np.argmax(prediction)])

if __name__ == '__main__':
    main(sys.argv[1])
