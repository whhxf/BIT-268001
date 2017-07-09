# -*- coding: utf-8 -*-

n = raw_input(unicode('请输入整数N：','utf-8').encode('gbk'))
sum = 0
for i in range(int(n)):
	sum += i + 1
print unicode("1到N求和的结果：%d" % sum ,'utf-8').encode('gbk')