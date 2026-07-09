from pathlib import Path

import tensorflow as tf
from tensorflow.keras import layers, models

# ==========================================================
# Dataset Path
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR

IMG_SIZE = (128, 128)
BATCH_SIZE = 32

# ==========================================================
# Load Dataset
# ==========================================================

train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)

print("\nClasses:", train_ds.class_names)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = (
    train_ds
    .cache()
    .shuffle(1000)
    .prefetch(AUTOTUNE)
)

val_ds = (
    val_ds
    .cache()
    .prefetch(AUTOTUNE)
)

# ==========================================================
# Data Augmentation
# ==========================================================

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.15),
    layers.RandomZoom(0.10),
])

# ==========================================================
# Base Model
# ==========================================================

base_model = tf.keras.applications.MobileNetV2(
    input_shape=(128, 128, 3),
    include_top=False,
    weights="imagenet",
)

base_model.trainable = False

# ==========================================================
# Model
# ==========================================================

inputs = tf.keras.Input(shape=(128, 128, 3))

x = data_augmentation(inputs)

x = tf.keras.applications.mobilenet_v2.preprocess_input(x)

x = base_model(x, training=False)

x = layers.GlobalAveragePooling2D()(x)

x = layers.Dropout(0.2)(x)

outputs = layers.Dense(1, activation="sigmoid")(x)

model = tf.keras.Model(inputs, outputs)

# ==========================================================
# Compile
# ==========================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

model.summary()

# ==========================================================
# Early Stopping
# ==========================================================

early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=2,
    restore_best_weights=True,
)

# ==========================================================
# Train
# ==========================================================

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5,
    callbacks=[early_stop],
)

# ==========================================================
# Save Model
# ==========================================================

MODEL_DIR = BASE_DIR.parent / "models"

MODEL_DIR.mkdir(exist_ok=True)

model.save(MODEL_DIR / "leaf_validator.keras")

print("\nLeaf validator saved successfully!")