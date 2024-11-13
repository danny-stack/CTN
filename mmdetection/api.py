from fastapi import FastAPI, File, UploadFile
from mmdet.apis import init_detector, inference_detector
import mmcv
import uvicorn
from io import BytesIO
from PIL import Image

app = FastAPI()

CONFIG_FILE = './CascadeTabNet/Config/cascade_mask_rcnn_hrnetv2p_w32_20e.py'
CHECKPOINT_FILE = './epoch_36.pth'
MODEL = init_detector(CONFIG_FILE, CHECKPOINT_FILE, device='cuda:0')

@app.post("/inference")
async def inference(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = Image.open(BytesIO(img_bytes))
    result = inference_detector(MODEL, img)
    return {"result": result}  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

