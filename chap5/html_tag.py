def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (k, v) for k, v in sorted(attrs.items())) # 注意这里的生成器省略了括号, sorted 的排序
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s<%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def foo(name):
    print(name)


if __name__ == '__main__':
    print(tag('img', src="http://xxx.com"))
    print(tag(name='img', src="http://xxx.com"))
    print(tag('p', "hi", "there"))
    tags = {
        'name': 'p',
    }
    foo(name='kaiser')
    print('kaiser')
