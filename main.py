from glob import glob

from flask import Flask, jsonify, request

import file_utils
from model.raid_model import MODEL_PATH, predict

app = Flask(__name__)


XRAY_UPLOADS = "xray_uploads"
XRAY_UPLOADS_RESULTS = "xray_uploads_results"


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    image_urls = data["images"]
    if not len(image_urls):
        return jsonify([]), 200

    file_utils.download_images(urls=image_urls, uploads_dir=XRAY_UPLOADS)

    images = glob(f"{XRAY_UPLOADS}/*.jpg")
    defects = predict(MODEL_PATH, images)

    file_utils.delete_uploads(uploads_dir=XRAY_UPLOADS)

    # Upload to cloud and delete image locally
    defect_uploads = file_utils.upload_results(XRAY_UPLOADS_RESULTS)

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
