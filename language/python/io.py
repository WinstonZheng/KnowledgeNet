# IO
## File

open()函数返回带read()方法的对象，统称为file-like-Object（包括：内存字节流、网络流和自定义流等，要求拥有read()方法）。

- 管理文件资源
```
//try-finally
try:
    f = open('/path/to/file','r')
    print f.read()
finally:
    if f:
        f.close()
// with
with open('/path/to/file', 'r') as f:
    print f.read()
```

- 读文件
- read()

read()一次性读取全部文件内容。防止内存过载，调用read(size)方法，每次读取size字节内容。

- readline()

每次读取一行内容。

- readlines()

一次读取所有内容，按行返回。

> 二进制文件读取，例如：图片、视频等，用'rb'模式打开
> f = open('****','rb')
> 非ASCII编码文本文件，以二进制打开，然后解码
> f = open('/Users/michael/gbk.txt', 'rb')
>  u = f.read().decode('gbk')

- 写文件