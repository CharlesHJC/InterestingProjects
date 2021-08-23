import sqlite3
################################################################################################
############################################<表User>############################################
# 添加用户信息
def addUser(c,conn,dir):
    # 验证参数正确性,并调整参数
    assert (dir['sex']=='男') or (dir['sex']=='女') or (dir['sex']==1) or (dir['sex']==2), '性别不正确'
    if dir['sex']=='男':
        dir['sex']=1
    elif dir['sex']=='女':
        dir['sex']=2

    assert (len(dir['ID_number'])==18), '身份证号位数不正确'

    #合成sql语句
    sql="INSERT INTO User VALUES('{0}','{1}','{2}','{3}','{4}');".format(dir['ID_number'],dir['username'],dir['sex'],dir['nation'],dir['address'])

    #执行sql语句
    c.execute(sql)

    #返回的结果——改变的行数
    result = conn.total_changes

    #事务提交
    conn.commit()

    return result
#################################################################################################
# 查询用户信息
def getUserData(c):

    #sql语句
    sql='''
        SELECT rowid,
        username,
        nation,
        address,
        CASE  WHEN sex=1 THEN '男'
              WHEN sex=2 THEN '女'
              ELSE NULL
        END AS sex
        FROM User;
        '''
    #返回的结果
    result=c.execute(sql)

    return result
##################################################################################################
############################################<表Card>##############################################
# 添加银行卡信息
def addCard(c,conn,dir):
    # 验证参数正确性,并调整参数
    assert (dir['type']=='借记卡') or (dir['type']=='信用卡') or (dir['type']==1) or (dir['type']==2) , '银行卡类型不正确'
    if dir['type']=='借记卡':
        dir['type']=1
    elif dir['type']=='信用卡':
        dir['type']=2


    sql="INSERT INTO Card VALUES('{0}','{1}','{2}','{3}');".format(dir['cardNO'],dir['validity'],dir['type'],dir['bank'])

    c.execute(sql)

    result = conn.total_changes #返回结果

    conn.commit()

    return result
###################################################################################################
# 查询银行卡信息
def getCardData(c):

    #sql语句
    sql='''
        SELECT rowid,
        username,
        cardNO,
        validity,
        CASE  WHEN type=1 THEN '借记卡'
              WHEN type=2 THEN '信用卡'
              ELSE NULL
        END AS type,
        bank
        FROM Card;
        '''
    #返回的结果
    result=c.execute(sql)

    return result