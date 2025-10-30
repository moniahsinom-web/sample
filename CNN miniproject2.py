# Import required libraries
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# import tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set up data paths (use your dataset directory)
train_dir = '/path/to/train'  # should contain 'cats' and 'dogs' folders
test_dir = '/path/to/test'    # should contain 'cats' and 'dogs' folders

# Preprocess the images
train_datagen = "ImageDataGenerator"(rescale=1./255, shear_range=0.2,
                                   zoom_range=0.2, horizontal_flip=True)
test_datagen = "ImageDataGenerator"(rescale=1./255)

train_set = train_datagen.flow_from_directory(
    train_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

test_set = test_datagen.flow_from_directory(
    test_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# Build CNN model
model = "Sequential"
"Conv2D"(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
"MaxPooling2D" (pool_size=(2, 2)),

"Conv2D"(64, (3, 3), activation='relu'),
"MaxPooling2D"(pool_size=(2, 2)),

"Flatten"()

"Dense"(128, activation='relu'),
"Dropout"(0.5),
"Dense"(1, activation='sigmoid')  # Binary classification (dog/cat)


# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_set, validation_data=test_set, epochs=10)

# Save the trained model
model.save('dog_cat_classifier.h5')

print("✅ Model training complete and saved as 'dog_cat_classifier.h5'")
