def sudo(num):
    if num == 1:
        return 1
    else:
        result = sudo(num-1)+num
        return result
sudo(10)
print(sudo(10))