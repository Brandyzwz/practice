def money(d):
    return d*6.28
d = int(input('请输入美元金额：'))
r = money(d)
print('%d美元折合成人民币%.2f元'%(d,r))
