from django.utils.decorators import method_decorator
from ninja.files import UploadedFile
from django.http import HttpRequest
from ninja import Router, File, Form
# 굳이 불러올 파일을 각각 명시하지 않아도, init 파일 작성을 통해서 바로 불러올 수 있음
from .schemas import NstResponse, NstRequest
from nstapp.services.nst_service import nst_apply
import json

router = Router()


@router.post("/", response=NstResponse)

def nst(request: HttpRequest, nst_request: NstRequest = Form(...), img: UploadedFile = File(...)) -> dict:
    # img = json.load(img)
    # nst_request.key = json.load(nst_request.key)
    # nst_request.picture = json.load(nst_request.picture)
    file_url = nst_apply(nst_request.key, nst_request.picture, img)
    return {"file_url": file_url}


# @router.get("/")
# def picture(nst_picture: NstPicture = Form(...)) -> str:
#     a = nst_picture
#     return a
