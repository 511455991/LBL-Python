##############################################################################################################
# shell脚本的使用
# file：command_linux_shell.sh
# author：LBL
# date：2023-2-15
#	 	
# linux系统中用户通过shell沟通内核，首行shebang指定的解释器会被优先使用，常见解释器：sh，bash，cshell，kshell等
# 在window中使用记事本编写utf-8格式文件会自动在文件中加BOM头：EF BB BF三个字节， \
# 导致移植到linux中无法使用，可使用sublime编辑器调整编码
# shell脚本要运行需要先添加执行权限。
# 运行的几种方式：	./a.sh    			执行当前目录下的a脚本,不加./会到PATH路径去找，然后找不到报错。
#		/bin/bash a.sh		开一个子进程，直接指定解释器来运行脚本。
# 		bash a.sh			/bin/bash的简写
# 		source a.sh		source命令会在原进程中执行强制执行文件中的命令。不关注有无权限。不开子进程。
# 		 . a.sh			是source的简写
#		bash -x a.sh		-x参数可查看脚本的运行过程，调试脚本使用
############################################################################################################## 				  


#!/bin/bash
<<comment
	1、可用来做多行注释
	2、常用来描述一个函数的用法说明
	3、使用任意字符串，不一定是comment
	
	输入输出和变量
comment

# 输入。read读取
read -t5 -p ‘请输入两个数字’ A B	# read读取用户输入-t5秒-p提示信息
[ -z $A ] && A=100			# 如果A为空，就将A赋值100
echo “$A+$B的结果是$[$A+$B]”	# 输出A+B结果

# 输出。				echo打印，打印变量。printf打印，与echo类似，有些不同
echo 脚本开始			# 打印字符串	
echo $1				# $n为位置参数。即执行脚本时传递的参数，n为数字
echo $0				# $0为当前脚本文件名
echo $*				# $*为脚本所有参数
echo $#				# $#为脚本参数数量
echo $?				# $?为上一条命令的退出状态码。成功0失败1。或上一个执行的函数返回值
echo $$				# $$为当前进程的PID


# 变量属性
declare			# declare用来声明变量，declare声明的默认是局部变量
			# -g声明全局变量
declare -i SUM=0		# -i声明整数变量
			# -a声明数组变量
			# -r声明只读变量
			# -p显示定义变量的语句，即属性和值

local			# local用来设置局部变量。变量的作用域默认是全局
local name=”张三”

begin_time=`date`			# `命令`可获取命令结果作为变量		获取当前时间交给begin_time
readonly begin_time			# 将变量设置为只读，不可修改
log=$(cat log.txt)			# $()同` `,都是执行命令,``不能嵌套，$()可以嵌套但只在bash解释器有效
echo $log		
unset log				# 删除变量,不能删除只读变量

# 字符串变量。			shell中变量默认值都是字符串，=两边不能有空格，变量使用才需要加$，重新赋值不用
NAME=“北京张三的北京弟弟”	# 定义变量
echo “${NAME}在工作”		# ${}输出变量。{}可省略，不建议省略。   		北京张三的北京弟弟在工作
echo ‘${NAME}在工作’		# 单引号强引用，所见即所得。 			${NAME}在工作
echo  ${#NAME} 			# ${#}获取字符串长度
echo  ${NAME:0:2}			# 从左截取字符串，${string:begin:length}		北京
echo  ${NAME:6}			# 省略length可截取到末尾。			弟弟
echo  ${NAME:0-2:2}			# 从右截取字符串，${string:0-begin:length}  	弟弟
echo  ${NAME:0-2}			# 省略length，从右开始截取到末尾		弟弟
echo  ${NAME#*京}			# ${string#}从头匹配指定字符串后的内容		张三的北京弟弟
echo  ${NAME##*北京}		# ${string##}从尾匹配指定字符串后的内容。	弟弟
echo  ${NAME%*张三}			# ${string%}匹配指定字符串前的内容	北京

# 数组变量
nums=(11 243 23 )			# 定义数组用(),元素使用空格分割
nums+=(7 “小明”)			# 添加元素。				11 243 23 7 小明
nums[2]=45			# 修改元素。				11 243 45 7 小明
unset ${nums[2]}			# 删除数组中元素				11 243 7 小明
echo ${nums[0]}			# 获取数组中元素				11
echo ${nums[*]}			# 获取数组所有元素。$arr[*]或者$arr[@]		11 243 45 7 小明
echo ${#nums[*]}			# 获取数组个数。				5
echo ${#nums[1]}			# 获取数组中某元素长度。			3
nums1=(11 12)
nums2=(13 14)
nums3=($nums1[*] $nums2[*])		# 数组拼接


# 运算符+  -  *  /  %  **  ++  --  +=  -+  *=  /=
num=`expr 2+2`			# 整数运算，bash本身变量都当成字符串不支持计算，expr是计算命令
num2=$(( 10 - 8 ))			# 整数运算，(( ))同expr。取结果需要加$
num2=$((i=i+10))			# (())会自动解析内部变量，里面的变量计算时不用加$
num3=`bc 1.1+1.2`			# bc是外部计算器，可小数运算，shell本身只可以整数计算
if ((10 >9 ));then			# 也可用来做比较条件。
    pass


<<a
判断语句 if
组合条件：
	-a 	与关系。	同&&，&是单与，前一个为0还会执行后一个；&&是双与，前为0直接返回0 ，效率更高。
	-o 	或关系。	同||
	！ 	非关系。
整数测试：
	-lt 小于			less than 
	-le 小于等于		less than or equal
	-gt 大于			great than 
	-ge 大于等于		great than or equal
	-eq 等于			equal
	-ne 不等于			not equal
字符测试：shell中==  !=  < > 只能用来比较字符串不能比较数字
	-n 	判断字符串是否为非空
	-z 	判断字符串是否为空
	== 	判断是否相等。同=
	!= 	判断是否不等
	\> 	判断字符一是否大于字符二，\是转义
	\< 	判断字符一是否小于字符二
	=~	判断字符是否匹配右侧正则
文件测试：
	test	test 可以对文件或字符串进行检测，判断某条件是否成立
	[  ]	test可用[  ]代替，if test -w /etc 等于 if[ -w /etc ]，[  ]内部两边必须右空格
	[[  ]]	[[ ]]支持&&、||这种符号，可读性更好,建议使用。[]中只能使用-a -o ！
			常用选项如下，还有其他选项
				-e 判断文件是否存在。常判断执行脚本时参数所写文件是否存在如$1
				-f 判断文件是否存在，且为普通文件
				-d 判断文件是否存在，且为目录文件
				-r 判断文件是否存在，且有读权限
				-w 判断文件是否存在，且有写权限
				-x 判断文件是否存在，且有执行权限
				-n 判断字符串是否为空
				
判断语句 case
case语句的选项支持根据正则匹配，如：*代表任意字符、[ ]单字符匹配、|或者......	

a
# if语句演示：
if [ -z "$str1" -o -z "$str2" ];then			# 使用""将变量包裹可避免奇葩问题：变量为空得话无引号会变成[ -z -o -z]是会报错的
    echo "字符串不能为空"			
    exit 0
fi

if [[ -z $str1  ||  -z str2 ]];then				# 效果同上。   
    echo "字符串不能为空”"	
    exit 0
fi

if [[ $tel =~ ^1[0-9]{10}$ ]];then				# 举例：检测tel变量是否符合正则匹配的手机号格式
	echo "是手机号"
fi

if [[ $# -gt 1 &&  $# -le 3 ]];then 			# 举例：检测脚本参数
    echo "参数个数正常，大于1个小于等于3个"
elseif [ $# -le 1 ];then
    echo "参数个数小于等于1个"
else
    echo "参数个数大于3个，有$#个"
fi

# 总结：条件是要处理数字用(( )) ，处理文件与字符串用[[  ]]


# case语句演示：
case $1 in				
[0-9])				
    echo "$1是数字"
    echo "分支遇到;;就结束啦";;			# ;;相当于while语句的break
[a-z])				
    echo "是小写字母";;		
*）					# 情况都没匹配上就会执行*)，*)相当于if语句的else
    echo "其他字符"				# 最后*)分支可以不用;;结尾，因为本身执行到esac也结束了
esac


<<a
循环结构(while ; until；for；for in ; select in)
a
# while循环
i=1;sum=0			
while(( i<=100 ));do				# while在条件成立时会循环。计算0-100累加
    (( sum+=i ))
    (( i++ ))
done
echo "sum:$sum"

# until循环
i=1;sum=0				# until在条件不成立时才会循环。与while相反
until (( i>100 ));do
    (( sum+=i ))
    (( i++ ))
    if sum >200 ;break 1			# break n用来跳出循环,n为循环层数，不写为所有循环
done					# continue n 用来跳过几次循环，默认一次
echo "sum:$sum"


# for循环
sum=0
for ((i=1; i<=100; i++));do			# for循环计算0-100累加。三个条件与java类似
    (( sum+=i ))
done
echo "sum:$sum"

# for  in 语句
nums=(10 20 30)
for num in $nums[*];do			# for循环 遍历数组元素
    if num==20;then
break
    elseif num==30;then
continue
    fi
    echo `expr num*2`
done

# select in 语句			 	select in语句类似于for in，但显示带编号的菜单，用户输入编号可以选择，完成交互.通常和case in 一起使用
echo “what is you favourite OS?”
select name in "linux" "windows" "mac";do
    case $name in 
    "linux")
        echo “linux是一个开源系统”		# 用户选择后执行的语句
        brek;;
    "windows")
        echo “windows是一个闭源收费系统”
        break;;
    "mac")
        echo “mac是苹果公司的”
        break;;				# 是无限死循环，ctrl+d或者遇到break才会退出
    *)
        echo “输入错误”
done


<<a
函数定义和调用、代码块
a
# 函数的定义和调用
function func(){
	echo “language: $1”
	echo “URL: $2”
	retrun `expr 1+1` 				# retrun为函数返回值。expr数学运算
}
func C++ http://www.baidu.com			# 调用函数，传两个位置参数。
echo $?						# 获取函数返回值。



# 代码块，开始符和结束符之间的内容是一个整体，可以直接打印、存入变量、
cat <<EOF							# 举例：显示一个菜单给用户，让用户输入字母选择功能。
d|D) show disk usages.	<<EOF代码块，EOF为结束符，当输入内容为EOF时结束
m|M) show memory usages.
s|S) show swap usages.
*) quit.
EOF
read -p "Your choice:" CHOICE

mysql -uroot -p12345 <<EOF						# 举例：自动登录mysql查询表并退出
use test;
select * from students where id<10;
exit;
EOF

tee /etc/a.txt <<'EOF'						# 举例:将代码块内容写入到a.txt文件中。tee命令是从标准输入读取内容写入文件或标准输出							
 这些是被写入文件的内容
 
EOF

$a <<EOF								# 举例：将代码块所有字符都存入变量a中
		代码块重定向，EOF分界符可随意指定。
		常与cat命令一起使用，显示一大块文本内容
EOF
echo $a




exit 0				# exit代表退出当前脚本。0为状态码

bash -n a.sh			# 检测a.sh脚本正确性