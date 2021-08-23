
# https://login.bce.baidu.com/
# https://ai.baidu.com/ai-doc/OCR/3k3h7yeqa
# https://ai.baidu.com/ai-doc/SPEECH/Gk4nlz8tc
# https://cloud.baidu.com/doc/SPEECH/s/1k4o0bmc7


from aip import  AipSpeech

# 定义常量，此处替换为你自己的应用信息
APP_ID = '11322263'
API_KEY = 'gfExV6h1dp3YS5jlwS8P5GmQ'
SECRET_KEY = 'GwgtAyGWKilXOYrTTI5mmlyelGK81XUj'

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# # # 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# #
# # 识别本地文件
# #目前支持的格式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
result = aipSpeech.asr(get_file_content(r'16k-23850.amr'), 'amr', 16000,{'lan': 'zh',})
print(result)
list1=list(result.get('result'))
s=list1[0]
print(s)
cc=s.replace(',','')
print(cc)

result  = aipSpeech.synthesis('第一必然是我们的！', 'zh', 1, {'vol': 5,'per':1})
print(result)
# # # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('口号.mp3', 'wb') as f:
        f.write(result)
