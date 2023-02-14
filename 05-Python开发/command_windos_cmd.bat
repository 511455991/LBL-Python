:: 备注内容，cmd命令是windows系统的命令。bat文件为windows系统的批处理文件，相当于linux的shell脚本
%注释内容%

cd ..		%返回上级目录	% 
d:		%切换盘符		%	
echo  a		%输出内容：a 	%	
dir		%查看有哪些文件	%
cls		%清屏		%

ipconfig 	查看ip
ping www.baidu.com
netstat -na		查看端口使用
netstat -nao |findstr 3306	查看含3306字段的端口使用情况，-o为显示进程pid
tasklist			查看启动的所有程序及pid
tasklist |findstr 进程号	查看某进程pid是什么程序
netstat -na > a.txt		将查询到的结果输入到文件中
net start mysql		启动mysql服务		需要管理员运行cmd
net stop mysql		停止

services.msc	打开服务
slidetoshutdown	滑动关机
shutdown -s -t 60 	60s后定时关机
shutdown -a	取消定时关机
shutodwn -r	重启电脑

java -jar .\jar包名.jar		运行java项目的jar包
pip install 软件名==版本号	安装python包
pip install --upgrade 软件名	更新python包
pip uninstall 软件名		卸载python包
pip show -f 包名		查看指定包信息

