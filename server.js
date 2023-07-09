const express = require('express');
const bodyParser = require('body-parser');
const tf = require('@tensorflow/tfjs-node');
const path = require('path');

const app = express();
const port = 3000;

// Middleware to parse JSON data
app.use(bodyParser.json());

// Serve static files (optional)
app.use(express.static(path.join(__dirname, 'public')));

// Load and serve the ML model
const modelPath = path.join(__dirname, 'model.h5');

async function loadModel() {
  try {
    const model = await tf.loadLayersModel(`file://${modelPath}`);
    console.log('Model loaded successfully.');
    return model;
  } catch (err) {
    console.log('Error loading the model:', err);
    return null;
  }
}

let model;

// Initialize and load the model
loadModel().then((loadedModel) => {
  model = loadedModel;

  // Define a route for prediction
  app.post('/predict', (req, res) => {
    try {
      // Extract input data from the request
      const inputData = req.body.data;

      // Preprocess input data if needed
      // ...

      // Make predictions using the loaded model
      const predictions = model.predict(inputData);

      // Postprocess predictions if needed
      // ...

      // Return the predictions as a response
      res.json({ predictions });
    } catch (err) {
      console.log('Prediction error:', err);
      res.status(500).json({ error: 'Prediction failed' });
    }
  });

  // Start the server
  app.listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}).catch((err) => {
  console.log('Model loading error:', err);
});
