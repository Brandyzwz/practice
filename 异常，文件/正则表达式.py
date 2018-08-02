import re
string = "我是黑客，研究人工智能"
result = re.findall('黑客|人工智能',string)
if result[0] == '黑客' or result[1] == '人工智能':
    print('有风险')
