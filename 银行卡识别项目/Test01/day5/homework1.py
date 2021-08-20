#1
import keyword
print(keyword.kwlist)

#2
print("我们是'北京石油化工学院的同学!'")

#3
PI=3.14
r=5
C=PI*2*r
S=PI*(r*r)
print('"半径为5的圆的周长为：{:.2f}'.format(C),',其面积为：{:.2f}"'.format(S))

#4
print(r'\t hello world \t')
print('\\t hello world \\t')



#5
w1='我们是'
w2='北京石油化工学院的'
w3='同学'
print(w1+'\t'+w2+'\t'+w3)
print(w1+'\n\t'+w2+'\n\t\t'+w3)
