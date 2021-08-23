import DB
import sqlite3
from aip import AipImageCensor
from aip import AipOcr
from aip import AipSpeech
#from playsound import playsound

# 定义常量
APP_ID = '20565663'  # 输入所创建应用的APP_ID
API_KEY = 'dCXCK7VCNSos92lfHHjci8sb'  # 输入所创建应用的API_KEY
SECRET_KEY = 'FZFY56XeBZHBrrE6PQwIWLdXPlkaQkdD'  # 输入所创建应用的SECRET_KEY

# 初始化
aipimageCensor = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)


# 连接数据库
conn = sqlite3.connect('eighth.db')
c = conn.cursor()

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def idcard(filePath):
    image = get_file_content(filePath)
    result_check = aipimageCensor.imageCensorUserDefined(image)

    if result_check.get('conclusion') == '合规':
        # 初始化AipFace对象
        aip0cr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 调用身份证识别
        result_idcard = aip0cr.idcard(image, "front")
        dir={
         'ID_number':result_idcard['words_result']['公民身份号码']['words'],
         'username': result_idcard['words_result']["姓名"]["words"],
         'sex': result_idcard['words_result']['性别']['words'],
         'nation':result_idcard['words_result']['民族']['words'],
         'address':result_idcard['words_result']['住址']['words']
         }
        result=DB.addUser(c,conn,dir)

        print(result)
        result=DB.getUserData(c)
        print(*result)
#        print(result_idcard, type(result_idcard))
#        print("姓名：", result_idcard['words_result']["姓名"]["words"])
#        print("身份证号：", result_idcard['words_result']['公民身份号码']['words'])
#        print("性别：", result_idcard['words_result']['性别']['words'])
#        print("民族：", result_idcard['words_result']['民族']['words'])
#        print("住址：", result_idcard['words_result']['住址']['words'])
         
         
        # 初始化AipSpeech对象
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
        # 调用语音识别
        text = '此人的姓名是' + result_idcard['words_result']["姓名"]["words"] + '家住' + result_idcard['words_result']['住址']['words']
        result = aipSpeech.synthesis(text, 'zh', 1, {'spd': 4, 'vol': 6})
        print(result)
    
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('check_id.mp3', 'wb') as f:
                f.write(result)
        s='check_id.mp3' 
        # 播放音频文件
#        playsound("check_id.mp3")
#        playsound("check_id.mp3")
        return s
    
    
    
    else:
        print(result_check)
        # 初始化AipSpeech对象
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
        # 调用语音识别
        result = aipSpeech.synthesis('这张图片不合规,请重新选择图片', 'zh', 1, {'spd': 4, 'vol': 6})
        print(result)
    
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('check_id.mp3', 'wb') as f:
                f.write(result)
        s='check_id.mp3' 
                # 播放音频文件
#        playsound("check_id.mp3")
        return s

def bankcard(filePath):
    image = get_file_content(filePath)
    result_check = aipimageCensor.imageCensorUserDefined(image)

    if result_check.get('conclusion') == '合规':
        # 初始化AipFace对象
        aip0cr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 调用身份证识别
        result_bank = aip0cr.bankcard(image)
        dir={
        'cardNO':result_bank["result"]["bank_card_number"],
        'validity':result_bank["result"]["valid_date"],
        'type':result_bank["result"]["bank_card_type"],
        'bank': result_bank["result"]["bank_name"]
        }
        result=DB.addCard(c,conn,dir)

        print(result)
        result=DB.getUserData(c)
        print(*result)
     
         
        # 初始化AipSpeech对象
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
        # 调用语音识别
            # 调用语音识别
        text = '这张银行卡的发卡行是' + result_bank["result"]["bank_name"] + '卡号是' + result_bank["result"]["bank_card_number"]
        result = aipSpeech.synthesis(text, 'zh', 1, {'spd': 4, 'vol': 6})
        print(result)

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('check.mp3', 'wb') as f:
                f.write(result)
    
        s='check.mp3' 
        # 播放音频文件
#        playsound("check_id.mp3")
#        playsound("check_id.mp3")
        return s
    
    
    else:
        print(result_check)
        # 初始化AipSpeech对象
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
        # 调用语音识别
        result = aipSpeech.synthesis('这张图片不合规,请重新选择图片', 'zh', 1, {'spd': 4, 'vol': 6})
        print(result)
    
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('check.mp3', 'wb') as f:
                f.write(result)
        # 播放音频文件
        s='check.mp3'    
        return s
