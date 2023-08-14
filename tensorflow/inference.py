import tensorflow as tf
from keras import models
import numpy as np
import sys

# I think number 100 will be class 2 and everything will shift right by 1!

class_to_number = {0 : 1, 1 : 10, 2 : 11, 3 : 12, 4 : 13, 5 : 14, 6 : 15, 7 : 16, 8 : 17, 9 : 18, 10 : 19,
                   11 : 2, 12 : 20, 13 : 21, 14 : 22, 15 : 23, 16 : 24, 17 : 25, 18 : 26, 19 : 27, 20 : 28, 21 : 29, 
                   22 : 3, 23 : 30, 24 : 31, 25 : 32, 26 : 33, 27 : 34, 28 : 35, 29 : 36, 30 : 37, 31 : 38, 32 : 39, 
                   33 : 4, 34 : 40, 35 : 41, 36 : 42, 37 : 43, 38 : 44, 39 : 45, 40 : 46, 41 : 47, 42 : 48, 43 : 49,
                   44 : 5, 45 : 50, 46 : 51, 47 : 52, 48 : 53, 49 : 54, 50 : 55, 51 : 56, 52 : 57, 53 : 58, 54 : 59,
                   55 : 6, 56 : 60, 57 : 61, 58 : 62, 59 : 63, 60 : 64, 61 : 65, 62 : 66, 63 : 67, 64 : 68, 65 : 69,
                   66 : 7, 67 : 70, 68 : 71, 69 : 72, 70 : 73, 71 : 74, 72 : 75, 73 : 76, 74 : 77, 75 : 78, 76 : 79,
                   77 : 8, 78 : 80, 79 : 81, 80 : 82, 81 : 83, 82 : 84, 83 : 85, 84 : 86, 85 : 87, 86 : 88, 87 : 89,
                   88 : 9, 89 : 90, 90 : 91, 91 : 92, 92 : 93, 93 : 94, 94 : 95, 95 : 96, 96 : 97, 97 : 98, 98 : 99,
                   99: 100 }

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
