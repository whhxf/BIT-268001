# -*- coding: utf-8 -*-

sum,tmp = 0,1
for i in range(1,11):
	tmp *= i
	sum += tmp
print u'运算结果：%d' % sum	