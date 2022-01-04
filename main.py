import os
from glob import glob

import cloudinary
from flask import Flask, jsonify, request

from model.raid_model import MODEL_PATH, predict

from .utils import delete_uploads, download_images, upload_results

app = Flask(__name__)


cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)


XRAY_UPLOADS = "xray_uploads"
XRAY_UPLOADS_RESULTS = "xray_uploads_results"


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    image_urls = data["images"]
    if not len(image_urls):
        return jsonify([]), 200

    download_images(urls=image_urls, uploads_dir=XRAY_UPLOADS)

    images = glob(f"{XRAY_UPLOADS}/*.jpg")
    defects = predict(MODEL_PATH, images)

    delete_uploads(uploads_dir=XRAY_UPLOADS)

    # Upload to cloud and delete image locally
    defect_uploads = upload_results(XRAY_UPLOADS_RESULTS)

    image_results = []
    for i in range(0, len(image_urls)):
        data = {
            "image": image_urls[i],
            "results": defects[i],
            "result_image": defect_uploads[i]
        }
        image_results.append(data)

    return jsonify(image_results), 200


if __name__ == "__main__":
    app.run(debug=True)
