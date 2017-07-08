# -*- coding: utf-8 -*-

str1 = raw_input(unicode('请输入一个人的名字：','utf-8').encode('gbk'))	
str2 = raw_input(unicode('请输入一个国家的名字：','utf-8').encode('gbk'))
result = unicode("世界这么大，{}想去{}看看",'utf-8').encode('gbk').format(str1, str2)
print result