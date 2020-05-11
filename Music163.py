import execjs

js = open('./Music163.js', 'r').read()
ext = execjs.compile(js)

result = ext.call('start')
print(result)
