from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from ninja import Schema
import json


# key 는 파일 제목 역할을 할 변수입니다!

class NstRequest(Schema):
    key: str
    picture: str

#
# class NstPicture(Schema):
#
