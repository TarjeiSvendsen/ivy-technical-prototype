from fastapi import FastAPI,UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from bson import ObjectId
from datetime import datetime
import os
from PIL import Image




app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_home():
    return FileResponse("static/html/index.html")


@app.post("/uploadimage/")
async def create_upload_image(image: UploadFile, filter:str,alpha_strength:int):
    
    match image.content_type:
        case "image/png":
            _extension = "png"
        case "image/jpeg":
            _extension = "jpeg"
        case "image/jpg":
            _extension = "jpg"
        case _:
            _extension = "png"
    if filter == None:
        filter = "c"
    
    _path = process_image(image.file,{"filter":filter,"alpha_strength":alpha_strength,"extension":_extension})
    return FileResponse(path=f"results/{_path}.png",filename=image.filename)




def process_image(image_to_process:bytes, image_attributes: dict):
    _filter_image = Image.open(f"filters/filter_{image_attributes["filter"]}.jpeg")
    _filter_image.putalpha(image_attributes["alpha_strength"])
    _filter_image_w,_filter_image_h = _filter_image.size
    
    _processed_image = Image.open(image_to_process)
    _processed_image_w, _processed_image_h = _processed_image.size
    offset = ((_processed_image_w - _filter_image_w) // 2, (_processed_image_h - _filter_image_h) // 2)
    _processed_image.paste(_filter_image,offset,_filter_image)


    save_string = ObjectId() # Generates an unique MongoID
    _processed_image.save(f"results/{save_string}.png")
    return save_string



def available_filters() -> list:
    """Not Implemented"""
    filter_path = "filters"
    replacement_values = {".png": "",".jpg": "",".jpeg":""}
    raw_filters =  os.walk(filter_path)
    final_filters = []
    for filter in raw_filters:
        final_filters.append(str.replace(filter,"filter_","").replace("."))
        