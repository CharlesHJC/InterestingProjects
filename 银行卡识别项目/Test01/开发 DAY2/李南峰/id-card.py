#身份证图像识别
from aip import AipOcr
import base64
# 定义常量
APP_ID = '20317325' #你百度帐号上的APP_ID    ok_tester
API_KEY = 'yT2aD13QLpPPoRuBIS1wzVRE' #你百度帐号上的API_KEY
SECRET_KEY = 'Zp3NaGlS39l7DyyP11oXPRIRlvypr065'#你百度帐号上的SECRET_KEY

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
img=get_file_content('shenfen.jpg')



result_idcard=client.idcard(img,"front")
print(result_idcard,type(result_idcard))
print("姓名：",result_idcard['words_result']["姓名"]["words"])
print("身份证号：",result_idcard['words_result']['公民身份号码']['words'])
print("性别：",result_idcard['words_result']['性别']['words'])
print("出生日期：",result_idcard['words_result']['出生']['words'])
print("民族：",result_idcard['words_result']['民族']['words'])
print("住址：",result_idcard['words_result']['住址']['words'])