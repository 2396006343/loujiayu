# money = 50
# print("钱包还有：",money,"元")
# money = money-10
# print("购买了冰淇淋，花费10元还剩下",money,"元")
# money = money-10
# print("购买了冰阔洛，花费10元还剩下",money,"元")
# print("最后钱包剩下还剩下",money,"元")
# print(type("黑发"))
# int_mata = int(12.11)
"""
print(type(11.22),11.22)
mama=int("123w")
print(type(mama),mama)
"""

"""
jinitaimei="鸡你太美"
yer="年"
print("你干嘛"+jinitaimei+"哎哟"+"实习了"+yer)
"""
"""
nian=2001
yue=3
ri=5
message="我出生于%s年%s月%s日"%(nian,yue,ri)
print(message)
jiage=9.5
Txu=112
yifu="T恤的价格为%d或者%f"%(Txu,jiage)
print(yifu)
"""
"""
kuandu=114.11541
A=1123
print("%5d"%kuandu)
print("%8d"%kuandu)
print("%5.2f"%kuandu)
print(f"野兽前辈{kuandu},啊啊啊啊{A}")
"""
"""
print("1+5等于%d"%(1+5))
print(f"5-1等于{5-1}")
"""
"""
name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily=1.2
growth_days=7
print(f"{name}+股票代码{stock_code}+当前股票价{stock_price}")
print("每日增长系数是%.1f,经过%d天的增长后，股票达到了：%.2f"%(stock_price_daily,growth_days,19.99*1.2**7))
"""
"""
name=input("你TM谁呀")
name=int(name)
print("%s你就是那舒克与贝塔,你给我等着"%name,type(name))
"""
"""
ku_1=True
ku_2=False
print(f"{10-10==1}{type(10-10==0)}")
print(f"{10-10==0}{type(10-10==0)}")
"""
"""
age=input("小亮给他整个活")
if age=="好的":
    print("忽略")

print("哼哼哼啊啊啊啊啊")
"""
"""
print(f"欢迎来到德莱联盟")
age=int(input("请输入你的年龄"))

if age>=18:
    print("你已经成年需要缴费11415")
    print("祝你开心")
print(type(age))
"""
"""
print("欢迎来到动物园")

if int(input("请输入你的年龄"))<=17:
    print("请交钱1000")
elif int(input("是否是VIP,0是是，1是否")) == 0:
    print("VIP免费")
else:
     print("恭喜你该交钱了")
"""
"""
if int(input("请输入第一次猜想的数字"))==10:
    print("恭喜你答对了")
elif int((input("不对再猜")))==10:
    print("恭喜你答对了")
elif int((input("最后猜一下")))==10:
    print("恭喜你答对了")
else: print("其实是10")
"""
"""
if int(input("你的年龄是多少"))>=10:
    print("不好意思，年龄超标，需要另外交钱")
    print("除非你有VIP")
    if (input("请问你有VIP吗")) == "有":
        print("VIP免费，请进入")
    else:print("不好意思，请交钱")
else:
    print("欢迎你，boy")
"""
"""
import random
num = random.randint(1,10)

shuzi=int(input("猜猜这个随机数字大小"))
if shuzi!=num:
    if shuzi>num:
        print("不好意思没有答对，你数字猜高了")
        shuzi = int(input("再猜猜这个随机数字大小"))
    elif shuzi<num:
        print("不好意思没有答对，猜小了")
        shuzi = int(input("再猜猜这个随机数字大小"))

    if shuzi > num:
        print("不好意思没有答对，你数字猜高了")
        shuzi = int(input("再猜猜这个随机数字大小"))
    elif shuzi < num:
        print("不好意思没有答对，猜小了")
        shuzi = int(input("再猜猜这个随机数字大小"))

    if shuzi > num:
                print("不好意思没有答对，你数字猜高了,没有机会了")
    elif shuzi < num:
                print("不好意思没有答对，猜小了，没有机会了")
    else:print("恭喜你猜对了")
else:
    print("恭喜你猜对了")
"""
"""
import random
num = random.randint(1,10)
a=1
ci=0
while(a):
    i=int(input("猜猜数字"))
    ci=ci+1
    if(i>num):
        print("大了")
    elif(i<num):
        print("小了")
    else: a=0
if(i==num):
    print("good")
    print("共猜了%s次"%(ci))
    """
"""
name="itheima is a brand of itcast"
a="a"
shuzi=0
for x in name:
    if(x==a):
        shuzi+=1
print(f"检测到的A有{shuzi}个")
"""
"""
a=0
num=int(input("请输入你的数字"))
for x in range(1,num):
    if(x%2==0):
        a=a+1
print(f"偶数共有{a}个")
"""
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
"""
"""
money=10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if(num>=5):
        print(f"员工{i}的绩效大于5,给予发工资1000,账户剩余{money}")
    else:
        print(f"员工{i}的绩效为{num},低于5,不给予发工资")
        continue
    if money>=1000:
        money-=1000
    else:
        print("没钱了，滚")
        break
"""
"""
def hanshu():
    print(f"你好\nhahaha")
hanshu()
hanshu()
"""
"""
num=37
num=input()
def tiwen(num):
    if(int(num)>37):
        print({f"{num}请您立刻隔离"})
    else:
        print({f"{num}体温正常"})

tiwen(num)
"""
"""
num=300
def add(x,y):
    global num
    num=500
    result = x+y
    print(f"2数相加的结果：{result},{num}")
    return result
print(f"{num}")
add(2,3)
print(f"{num}")
"""
"""
name = input("请输入您的名字")
money = 0


def atm_zhucaidan():
    # global num
    print(f"--------主菜单--------\n查询余额【输入1】\n存款【输入2】\n取款【输入3】\n退出【输入4】")
    num = int(input("请输入您的选择"))
    return num


def ATM_yuerchaxun():
    if num == 1:
        print(f"--------查询余额--------")
    print(f"{name}您好，您的余额剩余：{money}")


def ATM_chunqian(qian):
    global money
    money += qian
    print(f"---------存款--------")
    print(f"{name},您好，请输入您要存储的数额:{qian}已经存储成功")
    ATM_yuerchaxun()


def ATM_quqian(qian):
    global money

    print(f"---------取款--------")
    if (money < qian):
        print("不好意思，您取出的余额大于您的存款，无法取出")
    else:
        money -= qian
        print(f"{name},您好，请输入您要取出的的数额:{qian}已经取出成功")
    ATM_yuerchaxun()


while (1):
    num = atm_zhucaidan()
    if num == 1:
        ATM_yuerchaxun()
    elif num == 2:
        ATM_chunqian(int(input("请输入您要存储的额度")))
    elif num == 3:
        ATM_quqian(int(input("请输入您要取出的额度")))
    elif num == 4:
        print("退出成功")
        break
"""
# 列表
"""
steam=["jojo","dio"]
print(steam)
print(type(steam))

steam = ["itheima",66,True]
print(type(steam))
print(steam)

steam[0]="666"
print(f"替换掉第0位的结果{steam}")

steam.insert(1,"hahaha")
print(f"列表插入元素后的结果是{steam}")

steam.append(1)
print(f"列表尾部插入元素后的结果是{steam}")

steam2=[123,234,345]
steam.extend(steam2)
print(f"列表再追加新列表后的结果是：{steam}")

del steam[0]
print(f"删除第0个元素666后的结果{steam}")

my=steam.pop(5)
print(f"删除第5个元素后的结果{steam},取出的元素是{my}")

steam=["www","hahaha","www","jiji"]
steam.remove("www")
print(f"通过remove清除元素www后的结果是{steam}")

steam.clear()
print(f"列表被清空后的结果是:{steam}")

steam=["www","www","www"]
count=steam.count("www")
print(f"列表中的www数量是:{count}")

len()#可以知道列表的数量
"""
"""
liebiao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liebiao_1=[]
liebiao_2=[]
def haha():
    new = 0
    while new<len(liebiao):

        if liebiao[new]%2==0:
            liebiao_1.append(liebiao[new])
        new=new+1
    print(f"{liebiao_1}")
def wawa():
    for x in liebiao:
        if x % 2 == 0:
            liebiao_2.append(x)
    print(f"{liebiao_2}")
haha()
wawa()
"""
# 元组
"""
t1=(1,2,["wha","haha"])
t1[2][0]="shsa"
print(f"{t1}")
"""
# 字符串
"""
my_str = "ithima and it cast"
value=my_str[2]
valve2=my_str[-16]
print(f"从字符串{my_str}取下标为2的元素值是{value}，16的是{valve2}")

vala=my_str.index("and")
print(f"{vala}")

new_my_str=my_str.replace("and","和")
print(f"将其and替换成和后得{new_my_str}")

my_str = "hello papa haha"
my_str_list=my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得{my_str_list}")

my_str = "12hello papa haha21"
my_str_wawawa=my_str.strip("12")
print(f"将字符串{my_str}进行strip后{my_str_wawawa}")

count= my_str.count("pa")
print(f"将字符串{my_str}进行count后计算pa出现的次数为{count}")

num=len(my_str)
print(f"字符串{my_str}的长度为{num}")
"""

"""
my_str="itheima itcast boxuegu"
countr=my_str.count("it")
print(f"it共有{countr}个")
new_my_str=my_str.replace(" ","|")
print(f"将空格替换后{new_my_str}")
newww=new_my_str.split("|")
print(f"将|进行字符串分割后{newww}")
"""
# 序列
"""
my_list=[0,1,2,3,4,5,6,7,8]
result1=my_list[1:5]
result2=my_list[1:5:2]#起始1，结束5，步长2
print(f"结果1:{result1}")
print(f"结果2:{result2}")
my_list="012345678"
result1=my_list[::2]
print(f"结果1:{result1}")
result1=my_list[::-2]#负数的话反着来
print(f"结果1:{result1}")

my_str="万过新月，员序程马黑来，nohtyp学"
result1=my_str[9:4:-1]
print(f"结果1:{result1}")
result1=my_str[::-1][9:14]
print(f"结果1:{result1}")

my_str={"hahaha","www","aaa"}
my_str.add("转转转")
my_str.add("www")#由于集合有去重性，所以这个添加了也不会而外增加成两个www
print(f"my_set添加元素后的结果是{my_str}")
my_str.remove("hahaha")
print(f"my_set移除hahaha后{my_str}")
element=my_str.pop()#集合是随机取的，无法决定
print(f"集合被取出的元素是{element},取出元素后:{my_str}")
#取两个集合的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"取出差集后的结果是{set3}")
print(f"取出差集后原set1的内容{set1}")
print(f"取出差集后原set2的内容{set2}")
#消除两个集合的差集（就是两个都拥有的元素）
set1={1,2,3}
set2={1,5,6}
set1.difference_update(set2)
print(f"消除差集后原set1的内容{set1}")
print(f"消除差集后原set2的内容{set2}")
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(f"合并后的结果是{set3}")
print(f"合并后原set1的内容{set1}")
print(f"合并后原set2的内容{set2}")
#统计长度
num=len(set3)
print(f"集合内的元素数量为{num}")
#集合遍历不支持下标索引，不支持while循环
"""
"""
my_list=["hahaha","lalala","huhuhu","zazaza"]
yuanshu=set()
for x in my_list:
    print(f"{x}")
    yuanshu.add(x)
    print(f"列表的内容有：{my_list}")
    print(f"集合的元素有{yuanshu}")
"""
"""
#定义字典    key:蔡徐坤   value:小王
my_dict1={"蔡徐坤":2.5,"小王":85}
my_dict2={}#空字典
my_dict3=dict()#空字典
print(f"字典1内容：{my_dict1},类型:{type(my_dict1)}")
print(f"字典2内容：{my_dict2},类型:{type(my_dict2)}")
print(f"字典3内容：{my_dict3},类型:{type(my_dict3)}")
sore=my_dict1["蔡徐坤"]
print(f"蔡徐坤的分数为{sore}")
#定义嵌套字典
stu_scor_dict={
    "小王":{
        "语文":77,
        "数学":66,
        "英语":55
    },
    "小红":{
        "语文":57,
        "数学":76,
        "英语":85
    },
    "小亮":{
        "语文":97,
        "数学":56,
        "英语":45
    }
}
print(f"学生考试信息:{stu_scor_dict}")
score=stu_scor_dict["小王"]["语文"]
print(f"小王的语文成绩{score}")
score=stu_scor_dict["小亮"]["语文"]
print(f"小亮的语文成绩{score}")

#新加元素
my_dict1["小张"]=55
print(f"新增后{my_dict1}")
#更新就是和新加元素一样，但只是人物名要相同
my_dict1["小张"]=88
print(f"新增后{my_dict1}")
#删除
scor=my_dict1.pop("蔡徐坤")
print(f"字典被移除一个元素，结果：{my_dict1},被移除的是蔡徐坤成绩{scor}")
#清除就是
my_dict1.clear()
#取得字典的全部key
my_dict1={"蔡徐坤":2.5,"小王":85}
haha=my_dict1.keys()
print(f"{haha}")
#len和之前一样可以看数量
"""
bumen = {
    "王力宏": {
        "部门": "制造部",
        "工资": 6000,
        "级别": 1
    },
    "周杰伦":
        {
            "部门": "家庭部",
            "工资": 5000,
            "级别": 6
        },
    "林俊杰":
        {
            "部门": "家庭部",
            "工资": 7000,
            "级别": 6
        },
    "王宝强":
        {
            "部门": "制造部",
            "工资": 4000,
            "级别": 1
        }
}
"""
print("修改前")
print(f"{bumen}")
print("修改后")
for xinxi in bumen:
    if bumen[xinxi]["级别"] == 1:
        xiao=bumen[xinxi]
        xiao["级别"] = 2
        xiao["工资"]+=1000
        bumen[xinxi]=xiao
print(f":{bumen}")
"""  # 上面是视频的方法
"""
print("修改前")
print(f"{bumen}")
print("修改后")
for xinxi in bumen:
    if bumen[xinxi]["级别"] == 1:
        bumen[xinxi]["级别"] = 2
        bumen[xinxi]["工资"]+=1000

print(f":{bumen}")
"""
"""
my_list = [1,5,4,3,2]#列表
my_tuple = (1,2,3,4,5)#元组
my_str = "abcde"#字符串
my_set = {1,2,3,4,5}#集合
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}#字典

print(f"列表对象排序结果:{sorted(my_list)}")
"""
"""
#函数的位置传递，带*号的就是代表不定长，传进的参数位置合并为一个元组args是元组类型
def user_info(*args):
    print(f"{type(args)},{args}")
user_info("haha",18,[1,2,3,4])
#关键字传递不定长两个**号,传递键=值，就是字典那种
def user_haha(**us):
    print(us)
user_haha(name='tom',age=12,id=111)
#函数作为参数传递
def jiafa(compute):
    jia=compute(1,3)
    print(f"输出结果为{jia}")
def compute(x,y):
    return x+y
jiafa(compute)
"""
"""
# 多种传参的形式
def user_info(name,age,gender):
    print(f"姓名{name},年龄{age},性别{gender}")


# 位置参数默认形式
user_info('小明',20,'男')

# 关键字参数
user_info(age=12,name='小王',gender='女')
user_info(name='小夏',gender='女',age=18)


# 缺省参数（默认值）
def user_info(name,age,gender='男'):  # 设置默认值必须未设置默认值的后面，不能在前面
    print(f"姓名：{name}，年龄：{age},性别:{gender}")

user_info('小天',12)

user_info('小天',12,'女')


#函数的位置传递，带*号的就是代表不定长，传进的参数位置合并为一个元组,这里定义的args是这里的元组类型
def user_info(*args):
    print(f"{type(args)},{args}")
user_info("haha",18,[1,2,3,4])
# 关键字传递不定长两个**号,传递键=值，就是字典那种
def user_haha(**us):
    print(us)
user_haha(name='tom',age=12,id=111)
# 函数作为参数传递

#定义一个函数，接收另一个函数作为参数
def jiafa(compute): # 这里的compute传入的是代码的执行逻辑，也就是函数；这是一种计算逻辑的传递而不是数据的传递
    jia=compute(1,3) # 确定comput是函数
    print(f"输出结果为{jia}")


# 定义一个函数，准备作为参数传入另一个函数
def compute(x,y): # 直接（x,y）传入的就是数据传入
    return x + y

# 调用，并传入函数
jiafa(compute)

def test_func(compute):
    result = compute(1,2)
    print(f"结果:{result}")


# 通过lambda匿名函数形式将匿名函数作为参数传入
test_func(lambda x,y:x + y)
# 对比上面定义compute，lambada由于没有名字，只是匿名函数，并且只能写一行，只能使用一次,他的函数体相当于自带return
# 如果想用多次，就使用def关键字
"""

# 文件读取
# 打开文件
#f=open("E:\pychar\wanwan.txt","r",encoding="UTF-8")
# 读取文件.read
"""
print(f"读取10个字节：{f.read(10)}")
print(f"读取全部字节：{f.read()}")
print(f"--------------------------")
"""
# 读取文件.readlines
#lines=f.readlines()# 读取文件的全部行,封装到列表中
#print(f"lines读取内容:{lines}")
#print(f"lines对象类型:{type(lines)}")

# 读取文件.readline一次只读一行
# line=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(f"lines读取内容:{line}")
# print(f"lines读取内容:{line2}")
# print(f"lines读取内容:{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行的数据是:{line}")

# 关闭文件
#f.close()

# with open 语法操作文件
"""
with open("E:\pychar\wanwan.txt","r",encoding="UTF-8")as f:
    for line in f:
        print(f"每行数据:{line}")
"""

# 练习:
"""
f=open("E:\pychar\haha.txt","r",encoding="UTF-8")
lint=f.read()              # .read读取内容
coun=lint.count("haha")    # .通过字符串count来统计haha的出现数量，将统计出来的数值给coun
print(f"{coun}")           # .输出coun获得统计结果
"""

"""
f=open("E:\pychar\haha.txt","r",encoding="UTF-8") # r是读，w是写，a是追加的意思 
# 方法2 读取内容，一行一行的读取
coun=0
for leng in f:     # 通过for循环，读取一行行的内容
    word=leng.replace('\n','') # 可以使用字符,replace将单词结尾的换行符\n给替换掉，从而让\n不干扰判断
    # word=leng.strip() # 也可以使用strip将开头和结尾的\n给去除
    leng=word.split(' ')  # 使用字符.split将每行中的空格进行切分
    for shuzhu in leng:
        if shuzhu == 'jjjj':
            coun+=1
print(f"{coun}")
f.close()
"""
"""
写入操作
"""
# f = open("E:\pychar\loujiayu.txt","w",encoding="UTF-8")
# write写入
# f.write("Hello world!!!")
# # flush刷新
# f.flush()

# close关闭，内置有flush的功能
# f.close()
"""
追加模式
"""
# f = open("E:\pychar\loujiayu.txt","a",encoding="UTF-8")
# # write写入
# f.write("\n你好，世界！！！")
# f.flush()
# f.close()

"""
练习
"""
"""
# 打开文件准备读取
f=open("E:\pychar/bill.txt","r",encoding="UTF-8")
# 打开文件准备写入
ff=open("E:/pychar/bill.txt.bak","w",encoding="UTF-8")
# 设置for循环读取文件
for content in f:
    # 使用strip的字符用来删除文件中结尾处的换行符
    content = content.strip()
    # 使用split的字符，以逗号为切割点进行切割
    determine=content.split(",")
    # if语句判断determine【4】是否为测试，是就跳过，否则将内容录入ff中
    if determine[4] == "测试":
        continue
    ff.write(content)
    ff.write("\n")
f.close()
ff.close()
"""
"""
捕获异常
"""
# 基础捕获语法
try:
# 表示尝试的意思
    f = open("E:\pychar/jojo.txt", "r", encoding="UTF-8")
except:
    print("出现异常，因为文件不存在")
# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)