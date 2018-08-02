# 远程仓库clone到本地推送
* 1 在Github上新建一个仓库，copy远程仓库ssh地址
* 2 在本地桌面 git clone +ssh远程地址，拉下来远程空仓
* 3 在本地的远程空仓库里直接push就可以推到远程仓库中
步骤：cd 到本地的远程空仓库
&emsp;&emsp;&emsp;touch 1.py 
&emsp;&emsp;&emsp; git add 1.py & git commit -m 'Hello'
&emsp;&emsp;&emsp;git log 
&emsp;&emsp;&emsp;git push origin master




# 本地仓库推送到远程仓库
* 1 **在本地初始化一个Git本地仓库**
&emsp;mkdir test
&emsp;cd test 
&emsp;touch 1.py
&emsp;git init
&emsp;git status
&emsp;git retome add origin +远程仓库SSH地址
&emsp;git remote -v 查看一下连接的远程仓库地址
&emsp;git add 1.py & git commit -m '提交'
&emsp;git log
&emsp;git push origin master
成功推送
* 2 **如果远程仓库为空的，可以执行以上操作。不是空的则应用以下操作**
>远程仓库拥有本地仓库没有的东西，需要Pull下来，重新整合，再一起推送到远程仓库

&emsp;mkdir test
&emsp;cd test 
&emsp;touch 1.py
&emsp;git init
&emsp;git status
&emsp;git retome add origin +远程仓库SSH地址
&emsp;git remote -v 查看一下远程仓库地址
&emsp;git pull origin master将远程仓库中本地仓库没有的拉下来
&emsp;git add . & git commit -m '全部提交'
&emsp;git push origin master
成功推送