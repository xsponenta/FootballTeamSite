'Function module'

import secrets
import os
from PIL import Image
from main import app

def save_picture(form_picture: str) -> str:
    "Trim and saves picture"
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    i = Image.open(form_picture)
    i.save(picture_path)
    return picture_fn
