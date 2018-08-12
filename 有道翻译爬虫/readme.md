破解有道翻译的几个关键地方说明：
- 表单数据 i :这是需要翻译的文本
- 表单数据 salt:是一个通过当前时间加上0-9的随机数计算得出的数字，具体运算过程如下:\
`formdata['salt'] = str(int(time.time()*1000))+str((random.randint(0,10)))`
- 表单数据sign:通过salt数据就该后通过计算哈希值生成的，具体过程如下:\
``  s = ("fanyideskweb" + formdata['i'] + formdata['salt'] + "ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8')
    h.update(s)
    formdata['sign'] = h.hexdigest()``
- cookie数据___rl__test__cookies:当前时间的毫秒数
`___rl__test__cookies':'%s'%str(int(time.time()*1000))}`
- 其他数据均通过浏览器直接获得

运行结果：

