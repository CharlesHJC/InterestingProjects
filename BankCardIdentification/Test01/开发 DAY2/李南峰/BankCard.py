#python百度ai的银行卡识别代码
from aip import AipOcr

# 定义常量
APP_ID = '20317325' #你百度帐号上的APP_ID    ok_tester
API_KEY = 'yT2aD13QLpPPoRuBIS1wzVRE' #你百度帐号上的API_KEY
SECRET_KEY = 'Zp3NaGlS39l7DyyP11oXPRIRlvypr065'#你百度帐号上的SECRET_KEY

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

#读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('yanhang.jpg')#将左侧括号内3.jpg替换为待识别的图片路径

#调用银行卡识别

result_bank=client.bankcard(image)
print(result_bank,type(result_bank))

print("银行卡号：",result_bank[ "result"]["bank_card_number"])
print("发卡银行：",result_bank[ "result"]["bank_name"])
