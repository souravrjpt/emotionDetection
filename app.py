from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
import pickle
from werkzeug.utils import secure_filename
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Load the pickled model

# load and prepare the image
def load_image(filename)    :
	# load the image
	img = load_img(filename, target_size=(64,64))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 64, 64, 3)
	# center pixel data
	img = img.astype('float32')
	# print(img)
	return img
	
	# load an image and predict the class
def run_example(img_path):
    # load the image
    img = load_image(img_path)
    # load mode
    model = load_model('model.h5')
    # predict the class
    index=['anger','contempt','disgust','fear','happy','sadness','surprise']
    result = zip(index,  model.predict(img)[0])

    # for i in result:
    # 	if result==1:
    # 		res=index[i]
    for i in result:
            if i[1] == 1.0:
                return i[0]
                    
    return "Image is not Good!!!!"

# Define a route for receiving images and making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the request
        image_file = request.files['image']
        image_file.save("test.jpg")

        img = load_img("test.jpg", target_size=(64, 64))
        img = img_to_array(img)
        img = img.reshape(1, 64, 64, 3)
        img = img.astype('float32')

        # Make a prediction using the loaded model
        # result = model.predict(img)
        result = run_example("test.jpg")

        # Return the predicted result as JSON
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run()
