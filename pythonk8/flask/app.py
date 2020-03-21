import flask
app = flask.Flask(__name__)
import face_recognition
from PIL import Image
import io
# from werkzeug import secure_filename


@app.route('/')
def hello_world():
    return flask.render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    uploaded_files = flask.request.files.getlist("file")
    if len(uploaded_files) >= 2:
       face = uploaded_files[0]
       face_image_name = face.filename
       face.save(face_image_name)
       unknownface = uploaded_files[1]
       unknownface_image_name = unknownface.filename  
       unknownface.save(unknownface_image_name)
       known_image = face_recognition.load_image_file(face_image_name)
       unknown_image = face_recognition.load_image_file(unknownface_image_name)
       biden_encoding = face_recognition.face_encodings(known_image)[0]
       unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
       results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
       face_distances = face_recognition.face_distance([unknown_encoding], biden_encoding)
       data["prediction"] = str(results)
       data["confidence"] = str(face_distances)
       data["success"] = True
    else:
        data["error"] = "please send two images for check"
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run()



