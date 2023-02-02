
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
from flask import Flask, request
import tensorfow as tf
import numpy as np

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Loa model & define classes
##########################################################################

model = tf.keras.models.load_model("best_model.h5")

##########################################################################
## Routes
##########################################################################

@app.route("/classify", methods=["POST"])
def classify():
    
    # Get the data from the request
    data = request.get_json()
    
    # Convert the data to a numpy array
    pixels = np.array(data["pixels"])
    
    # Reshape the array to match the model's input shape
    pixels = pixels.reshape(1, -1)
    
    # Use the model to make a prediction
    prediction = int(np.round(model.predict(pixels)[0][0]))
    
    # Return the predicted class as a response
    return {"class": str(prediction)}

##########################################################################
## Main
##########################################################################

if __name__ == "__main__":
    app.run()
