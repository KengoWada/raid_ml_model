import json
from glob import glob

import torch


MODEL_PATH = "best.pt"
FILE_SAVE_DIR = "xray_uploads_results"


def predict(modelpath: str, test_images: list):
    """
    Run inference with the yolov5 model
    """
    model = torch.hub.load("ultralytics/yolov5", "custom",
                           path=modelpath, force_reload=True)
    # Inference
    results = model(test_images)
    results.save(F"./{FILE_SAVE_DIR}")
    upload_results = results.tolist()

    defects = []
    for result in upload_results:
        df = result.pandas().xyxy[0]
        df_json = json.loads(df.to_json(orient="records"))
        df_json = [
            {
                "confidence": k["confidence"],
                "name": k["name"],
                "class": k["class"]
            }
            for k in df_json
        ]
        defects.append(df_json)

    return defects


if __name__ == "__main__":
    # Test image batch
    IMAGES = glob(
        "/content/drive/MyDrive/final_year_project/raid/test_images/*.jpg")

    predict(MODEL_PATH, IMAGES)
