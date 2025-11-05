from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    img = await file.read()
    result = remove(img)
    return Response(content=result, media_type="image/png")
