from fastapi import FastAPI,UploadFile
from PIL import Image

app = FastAPI(debug=True)



@app.post("/uploadimage/")
async def create_upload_image(image: UploadFile):
    process_image(image.file)
    return {"filename": image.filename}





_filter_image = Image.open("filters/filter_c.jpeg")
_filter_image.putalpha(12)
_filter_image_w,_filter_image_h = _filter_image.size


def process_image(image_to_process:bytes):
    _processed_image = Image.open(image_to_process)
    _processed_image_w, _processed_image_h = _processed_image.size
    offset = ((_processed_image_w - _filter_image_w) // 2, (_processed_image_h - _filter_image_h) // 2)
    _processed_image.paste(_filter_image,offset,_filter_image)
    

    _processed_image.save("results/result.png")