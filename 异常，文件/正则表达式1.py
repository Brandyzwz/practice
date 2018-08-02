import re
test_label = "<html>hh</htmlbalabala>"
ret = re.match(r"<([a-zA-Z]*)>\w*</\>", test_label)
if ret:
    print(ret.group())
else:
    print("%s 这是一对不正确的标签" % test_label)