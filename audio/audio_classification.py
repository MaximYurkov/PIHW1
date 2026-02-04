import tensorflow as tf
import tensorflow_hub as hub

m = hub.load("https://tfhub.dev/google/yamnet/1")

b = tf.io.read_file("audio/sample.wav")
w, sr = tf.audio.decode_wav(b)

w = tf.reduce_mean(w, axis=1) if len(w.shape) == 2 else w
w = tf.cast(w, tf.float32)

scores, embeddings, spectrogram = m(w)

print(int(sr.numpy()))
print(scores.shape, embeddings.shape, spectrogram.shape)
print("top_score", float(tf.reduce_max(scores).numpy()))

# Цель:
# распознавание звуковых событий в аудиофайле

# Выход:
# матрица вероятностей звуковых классов, 
# векторные представления аудиосигнала, 
# спектрограмма.

# python audio/audio_classification.py