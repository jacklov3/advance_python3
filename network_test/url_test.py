#-*- coding:utf-8 -*-

from  urllib.parse import *

#解析URL字符串

result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')

print(result)
#通过属性名和索引来获取URL的各部分
print('scheme:',result.scheme,result[0])
print('主机和端口:',result.netloc,result[1])
print('主机:',result.hostname)
print('端口:',result.port)
print('资源路径:',result.path,result[2])
print('参数:',result.params,result[3])
print('查询子符串:',result.query,result[4])
print('fragment:',result.fragment,result[5])
print(result.geturl())

result = urlunparse(('http', 'www.crazyit.org:80', 'index.php',
    'yeeku', 'name=fkit', 'frag'))
print('URL为:', result)

#解析查询字符串、返回dict

result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
print(urlencode(result))

# 被拼接URL不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result) # http://www.crazyit.org/users/help.html
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result) # http://www.crazyit.org/users/book/list.html
# 被拼接URL以斜线（代表根路径path）开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result) # http://www.crazyit.org/help.html
# 被拼接URL以双斜线（代表绝对URL）开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result) # http://help.html