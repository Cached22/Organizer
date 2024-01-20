import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Image } from 'react-native';
import axios from 'axios';

const API_BASE_URL = 'http://your-backend-api-url.com'; // Replace with your actual API URL

const App = () => {
  const [image, setImage] = useState(null);
  const [layout, setLayout] = useState(null);
  const [error, setError] = useState('');

  const handleImageUpload = async () => {
    try {
      // Assuming 'image' is the state where the image URI is stored
      const imageData = new FormData();
      imageData.append('image', {
        uri: image,
        type: 'image/jpeg', // or the correct image mime type
        name: 'upload.jpg',
      });

      const response = await axios.post(`${API_BASE_URL}/upload`, imageData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.success) {
        alert(UPLOAD_SUCCESS);
        recognizeObjects(response.data.imagePath);
      } else {
        setError('Image upload failed');
      }
    } catch (err) {
      setError('An error occurred during image upload');
      logEvent('Image upload error: ' + err.message);
    }
  };

  const recognizeObjects = async (imagePath) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/recognize`, { imagePath });
      if (response.data.success) {
        alert(RECOGNITION_SUCCESS);
        generateLayout(response.data.objects);
      } else {
        setError('Object recognition failed');
      }
    } catch (err) {
      setError('An error occurred during object recognition');
      logEvent('Object recognition error: ' + err.message);
    }
  };

  const generateLayout = async (objects) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/layout`, { objects });
      if (response.data.success) {
        alert(OPTIMIZATION_SUCCESS);
        setLayout(response.data.layout);
      } else {
        setError('Layout generation failed');
      }
    } catch (err) {
      setError('An error occurred during layout generation');
      logEvent('Layout generation error: ' + err.message);
    }
  };

  const logEvent = (message) => {
    // Implement logging logic here
    console.error(message);
  };

  return (
    <View style={styles.container}>
      {image && <Image source={{ uri: image }} style={styles.imagePreview} />}
      <TouchableOpacity style={styles.button} onPress={handleImageUpload}>
        <Text style={styles.buttonText}>Upload Image</Text>
      </TouchableOpacity>
      {layout && <Text style={styles.layoutPreview}>{JSON.stringify(layout)}</Text>}
      {error && <Text style={styles.errorText}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
  button: {
    backgroundColor: '#007bff',
    padding: 10,
    borderRadius: 5,
    margin: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
  imagePreview: {
    width: 200,
    height: 200,
    marginBottom: 10,
  },
  layoutPreview: {
    marginTop: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  errorText: {
    color: 'red',
    marginTop: 10,
  },
});

export default App;