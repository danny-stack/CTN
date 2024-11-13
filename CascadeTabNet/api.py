import os
import json
import base64
from pathlib import Path
from pydantic import BaseModel, Field
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class BBox(BaseModel):
    left: float
    top: float
    width: float = Field(ge=0.0)
    height: float = Field(ge=0.0)

    @classmethod
    def from_xyxy(cls, 
                  *, 
                  x1: float, 
                  y1: float, 
                  x2: float, 
                  y2: float):
        
        return cls(left=x1, 
                   top=y1, 
                   width=x2 - x1, 
                   height=y2 - y1
                   )

class ScoredBBox(BaseModel):
    bbox: BBox
    score: float

def cascade_inference(img_path):
    # MMDetection container's API URL
    url = "http://mmdetection_container_ip:8000/inference"  
    with open(img_path, "rb") as img_file:
        response = requests.post(url, files={"file": img_file})
    return response.json()

def change_cascadetb_result_to_sb_cls(cascadetb_result):
    '''
    cascadetb_result: the output of cascadetb is a tuple with two elements, we choose the first elements to be the input of this function(for example: result[0])

    '''
    scored_bbox_list = []
    for i in range(len(cascadetb_result[0])):
        box = BBox.from_xyxy(x1=cascadetb_result[0][i][0],y1=cascadetb_result[0][i][1],x2=cascadetb_result[0][i][2],y2=cascadetb_result[0][i][3])
        scored_bbox = ScoredBBox(bbox=box, score=cascadetb_result[0][i][4])
        scored_bbox_list.append(scored_bbox)
    for i in range(len(cascadetb_result[2])):
        box = BBox.from_xyxy(x1=cascadetb_result[2][i][0],y1=cascadetb_result[2][i][1],x2=cascadetb_result[2][i][2],y2=cascadetb_result[2][i][3])
        scored_bbox = ScoredBBox(bbox=box, score=cascadetb_result[2][i][4])
        scored_bbox_list.append(scored_bbox)
    return scored_bbox_list

class TableDetectionRequest(BaseModel):
    image_base64: str

def base64_to_png(base64_string, output_file_prefix="image"):
    # 去除Base64字符串中的前缀（如果有）
    if base64_string.startswith('data:image/png;base64,'):
        base64_string = base64_string.split(',')[1]

    # 解码Base64字符串
    image_data = base64.b64decode(base64_string)

    # 创建目标目录路径
    output_dir = Path.cwd() / "intflex_imgs"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 初始化文件名
    output_file = output_dir / f"{output_file_prefix}_1.png"
    counter = 1

    # 检查文件是否存在，如果存在则递增文件名
    while output_file.exists():
        counter += 1
        output_file = output_dir / f"{output_file_prefix}_{counter}.png"

    # 将解码后的数据写入PNG文件
    with open(output_file, 'wb') as f:
        f.write(image_data)

    return str(output_file)

# @app.post("/cascade_table_detection/")
# def cascade_table_detection(request: TableDetectionRequest):
#     try:
#         image_path = base64_to_png(request.image_base64)
#         # 调用mmdetection服务API
#         files = {'file': open(image_path, 'rb')}
#         response = requests.post("http://mmdetection_service:6007/inference", files=files)
#         if response.status_code == 200:
#             result = response.json()
#             return result
#         else:
#             raise HTTPException(status_code=500, detail="Error in mmdetection service")
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=404, detail=str(e))

@app.post("/cascade_table_detection/")
async def cascade_table_detection(request: TableDetectionRequest):
    try:
        # Convert image to file
        image_path = base64_to_png(request.image_base64)

        # Send the image file to the mmdetection API
        with open(image_path, "rb") as f:
            files = {"file": (image_path, f, "image/png")}
            response = requests.post("http://mmdetection_container:8000/inference", files=files)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error in mmdetection inference")

        result = response.json()
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6006)

