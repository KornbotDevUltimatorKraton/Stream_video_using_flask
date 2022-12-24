import base64
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/update_image", methods=["POST"])
def update_image():
    # Get the image data from the request
    image_data = request.json["image"]

    # Decode the base64 image data
    image_data = base64.b64decode(image_data)

    # Save the image to a file
    with open("/home/kornbotdev/Stream_WEBRTC_python/static/image.jpg", "wb") as f:
        f.write(image_data)

    return "OK"

@app.route("/video_rtc")
def web_rtc():

      return render_template("index.html")

if __name__=="__main__":

        app.run(debug=True,threaded=True,host="0.0.0.0",port=8080)
