from flask import Flask, jsonify, request
from deepface import DeepFace
import json
import base64
app = Flask(__name__)



#models used in the deep face

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]





def analyze(imgbase64+, actions=['emotion',"gender","race"]):
    imgdata = base64.b64decode(imgbase64)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    obj = DeepFace.analyze("some_image.jpg", actions = actions)
    print(obj)
    return obj





@app.route("/mostEmotion", methods=['Post'])
def mostEmotion():
    #returns the image with the most emotion
    images=request.get_json()["images"]# base 64 of the images
    results=[]
    for imageBase64 in images:
        try:
            result=analyze(imageBase64,["emotion"])
            results.append(result["emotion"])
        except:
            results.append({"error":"face not found"})
            print("Image not added!")
    return json.dumps(results)








@app.route('/analyze', methods = ['POST'])
def Analyze():
    img_data=request.get_json()["base64"]
    try:
        return json.dumps(analyze( img_data))
    except:
        return {"error":"face not found!"}


@app.route("/", methods=['GET'])
def get_article():
    return "working"





if __name__ == "__main__":
    app.run(debug=True)
