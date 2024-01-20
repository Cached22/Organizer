import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';
import axios from 'axios';

jest.mock('axios');

describe('App component', () => {
  test('renders upload button', () => {
    render(<App />);
    const uploadButton = screen.getByTestId('uploadButton');
    expect(uploadButton).toBeInTheDocument();
  });

  test('calls object recognition API on image upload', async () => {
    const mockUploadResponse = { data: { message: 'Image uploaded successfully' } };
    axios.post.mockResolvedValueOnce(mockUploadResponse);

    render(<App />);
    const file = new File(['(⌐□_□)'], 'chucknorris.png', { type: 'image/png' });
    const input = screen.getByTestId('uploadInput');
    fireEvent.change(input, { target: { files: [file] } });

    expect(axios.post).toHaveBeenCalledWith('/api/upload', expect.any(FormData));
  });

  test('displays layout after successful recognition and optimization', async () => {
    const mockRecognitionResponse = { data: { recognizedItems: ['box', 'bicycle'] } };
    const mockOptimizationResponse = { data: { layout: 'Optimized layout data' } };
    axios.post.mockResolvedValueOnce(mockRecognitionResponse);
    axios.get.mockResolvedValueOnce(mockOptimizationResponse);

    render(<App />);
    const uploadButton = screen.getByTestId('uploadButton');
    fireEvent.click(uploadButton);

    const layoutView = await screen.findByTestId('layoutView');
    expect(layoutView).toHaveTextContent('Optimized layout data');
  });

  test('handles errors during image upload', async () => {
    axios.post.mockRejectedValueOnce(new Error('Network error'));

    render(<App />);
    const uploadButton = screen.getByTestId('uploadButton');
    fireEvent.click(uploadButton);

    const errorMessage = await screen.findByTestId('errorMessage');
    expect(errorMessage).toHaveTextContent('Network error');
  });
});