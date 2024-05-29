# Emotion Detection Model

This project is an emotion detection system built using Python, Flask, and a Keras-based deep learning model. The system processes video inputs to recognize and classify emotions such as happiness, sadness, disgust, anger, worry, etc.

## Features

- **Emotion Detection**: Recognizes emotions from video frames in real-time.
- **Web Interface**: Provides a user-friendly web interface to upload videos and view results.
- **REST API**: Exposes endpoints for video upload and emotion detection.

## Requirements

- Python 3.7 or above
- Flask 2.0 or above
- Keras 2.3 or above
- TensorFlow 2.3 or above
- OpenCV 4.5 or above

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/souravrjpt/emotionDetection.git
    cd emotionDetection
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the web interface**:
    Open your browser and go to `http://127.0.0.1:5000`.

3. **Upload a video**:
    - Use the web interface to upload a video file.
    - The system will process the video and display the detected emotions frame-by-frame.

## API Endpoints

- **Upload Video**: 
  - **Endpoint**: `/upload`
  - **Method**: `POST`
  - **Description**: Uploads a video file for emotion detection.
  - **Parameters**: 
    - `file`: The video file to be uploaded.
  - **Response**: JSON object with emotion detection results.

## Model Details

The emotion detection model is built using Keras with the TensorFlow backend. It is trained on a dataset of facial expressions to recognize various emotions. The model processes each frame of the video and outputs the detected emotion.

## File Structure

- `app.py`: The main Flask application file.
- `model.py`: Contains the Keras model loading and prediction logic.
- `utils.py`: Utility functions for video processing.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains static files like CSS and JavaScript.
- `requirements.txt`: Lists the required Python packages.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [souravrajput2670@gmail.com] or open an issue on GitHub.

---

Feel free to customize this README to better fit your project's specifics.
