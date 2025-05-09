
#------------------------------------------------------------------------------------------------
#برای استفاده از کتابخانه ها یا باید از خود پایتون بگیری یا باید دانلود کنی و در پوشه پایتون بزاری
import math
math.pow(3,8)


#dir اسم کتابخانه رو داخلش میزاری و کل توابع رو داخلش میاره
dir(math)

#برای معرفی تابعی که نمیدونی چیه یا داخل اینترنت میزنی یا از helpکمک میگیری
help(math.isqrt)

#کتابخانه رندوم
#داده های رندوم میده
import random
dir(random)
help(random.randint)
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
#خلاصه کردن کد به این صورت هست
#یعنی از این به بعد این تابع را با این نام برگردون
from random import randint as ran
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
datetime #کتابخانه زمان و تاریخ 
import datetime
datetime.datetime.second
#اولی اسم کتابخانه است دومی اسم تابع است و سومی اسم چیزی که میخوایم
#------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------
#strptime=تبدیل رشته به تاریخ و زمان
#ex: 12 jun 2018 =====> 2018/06/12

# strftime= تبدیل تاریخ و زمان به رشته
# ex:2018-06-12 ====> 12 jun 2018
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
# در پایتون قسمت شرط ها میتوان از و -یا استفاده کرد برای مخفف کردن کد ها به کار میاد
# به عبارت های تو در تو نستد هم میگویند  nested
#ex:
# if a>30 and b<+45:
# print(d)

# if a>45 or d<45:
# print(d)
 #------------------------------------------------------------------------------------------------


"""
#اگر این کار رو انجام بدی میتونی بیشتر از یک خط کامنت بزاری بدون اینکه لازم باشه هشتگ بزاری
"""
#------------------------------------------------------------------------------------------------
#برای اینکه داده های را در یک خط بنویسیم و لازم نباشه ده خط بنویسیم به این صورت میشود نوشت
x,y,z="yellp" ,"black" ,"blue"
print(x,y,z)

#یا میتوان یک اتریبیوت را به چند تابع داد
x=z=a="blue"
print(x)


#میتوان به صورت لیست داد و سپس لیست را استخراج کرد
fruits:["apple","banana","cherry"]
fruits=x,y,z
print(x)
print(y)
print(z)

#------------------------------------------------------------------------------------------------
#فانکشن هایی که بیرون از یک متغیر ساخته میشوند میتواند داخل فانکشن هم استفاده شوند فقط باید صدا زده بشن
#X="HI
def myfunc():
 #print("python is + X)
 #اگر داخل یک فانکشن تابعی هم نام با تابع خارج از آن باشد فقط ان را میشود داخل فانکشن صدا زد.
 
 
 #برای اینکه تابع داخل که همنام هست رو صدا کنی میتونی از 
 #global 
# .
#استفاده کنیم

#x = "awesome"

#def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------  
#برای راحت کردن کار خود و برای اینکه از لازمه های تایپ ها استفاده نکنیم همرو داخل پرانتز میزاریم و نوع آن را قبل ا زآن مینویسیم
dict(name="alireza",age=24)
# -------------------------------------------------------------------  
#اعداد
a=234
a=23e4
#ای در اصل یعنی توان و همچنان اینتیجر هست
#همه ی حالت های عددی قابل تبدیل به یکدیگر هستند به غیر از کمپلکس
# -------------------------------------------------------------------


#برای اینکه دیگه دونه دونه استرینگ ننویسیم از سه تا دبل کوتیشین استفاده میکنیم
a="""hello to everyone from here,
hello to you from there,
hello to me from here"""
print(a)

#برای گرفتن مقدار کلی یک داده از len استقاده میکنیم
a="hello","to you"
print(len(a))

#برای اینکه ببینیم لغت خاصی درون متن داریم یا نه از این استفاده میکنیم
#حالت اول
a="hello to everyone in the class"
print("everyone" in a )

# حالت دوم
a="hello to everyone in the class"
if "everyone" in a:
 print("i find it")
 
#حالت سوم
a="hello to everyone in the class"
print("you" not in a)

#حالت چهارم
a="hello to everyone in the class"
if "expensive" not in a:
    print("there isn't  your word there")
# -------------------------------------------------------------------
#SLICING STRING
#با دادن عدد پوزیشن ما میتوانیم کاراکتر مخصوص به آن را برگردانیم
a="hello","world"
print(a[2:4])

#اگر خواستیم بگیم از فلان کاراکتر تا اخر به این صورت میزنیم
a="hello", "world"
print(a[2:])

#میتوان با استفاده از منفی کاراکتر را از آخر به اول برگرداند
a="hello", "world"
print(a[-2:-3])
# -------------------------------------------------------------------
#MODIFY STRING
#برای اینکه یک استرینگ رو کاملا بولد کنیم و به حالت کپیتال برگردونیم میتونیم از آپر استفاده کنیم
a="hello", "world"
print(a.upprt())
# -------------------------------------------------------------------
#همه ی این تمرینات مربوط به سایت هست، توضیحات در دفتر هست در تاریخ 15 رمضان به بعد
# STRING METHODS
#(یزرگ کردن حرف اول)
a="hello to everyone who hears me!!"
print(a.capitalize())


#کوچک کردن تمام استرینگ
a="HELLO TO EVERY ONE WHO CAN HEAR ME !!"
print(a.casefold())

#وسط بردن استرینگ به مقداری که دادی
a="hello to everyone who hears me!!"
b=a.center(110)
print(b)

#تعداد دفعاتی که لغت مشخصی تکرار شده رو برمیگردونه
a="hello to everyone who hears me!!"
b=a.count("hello")
print(b)

#کد متنی که دادی رو برمیگردونه
a="hello to everyone who hears me!!"
b=a.encode()
print(b)

#ترو برمیگردونه اگر اخر جمله با چیزی که تو خواستی یکی بود
a="hello to everyone who hears me!!"
b=a.endswith("!!")
print(b)

#لفتی که میخوای رو پیدا میکنه
a="hello to everyone who hears me!!"
b=a.find("to")
print(b)

#جای لغتی که میخوای رو بهت میده
a="hello to everyone who hears me!!"
b=a.index("hear")
print(b)

#اگر تو متنت عدد بود ترو برمیگردون
a="hello to everyone who hears me!!"
b=a.isalnum()
print(b)

#اگر کلا متن بود و عدد نداشت ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isalpha()
print(b)

#اگر فقط اعداد یک تا نه بود ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isdecimal()
print(b)


#اگر تماما اعداد ساده بودند ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isdigit()
print(b)

#اگر تمام کاراکترای متنت کوچک بودن ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.islower()
print(b)


#اگر تمام کارکترا عدد بودن ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isnumeric()
print(b)


#اگر کاراکترات قابل پرینت باشن ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isprintable()
print(b)


#اگر در کاراکترات اسپیس باشه ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isspace()
print(b)


#اگر حرف اول تمام لغات با حروف بزرگ باشه ترو برمیگردوننه
a="hello to everyone who hears me!!"
b=a.istitle()
print(b)


#اگر تمام کاراکترا با حروف بزرگ باشن ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.isupper()
print(b)

#حروفی که دادی رو با استفاده از چیزی که مشخص کردی مثل هشتگ جدا جدا برمیگردونه و جدا میکنه
a=("john","apple","blue")
b="#".join(a)
print(b)

#جمله رو از راست از لغتی که مشخص کردی به مقدار عددی که دادی جدا میکنه
a="banana"
b=a.ljust(40)
print(b)


#تمام حروف رو تبدیل به کوچک میکنه
a="hello to everyone who hears me!!"
b=a.lower()
print(b)


#تمام حروف رو تبدیل به بزرگ میکنه
a="hello to everyone who hears me!!"
b=a.upper()
print(b)

# لغت را از چپ میچسبونه به جمله و از راست جدا میکنه
a="banana"
b=a.lstrip()
print("of all fruits ",b,"is my favoourite.")

# لغت را از راست میچسبونه به جمله و از راست جدا میکنه
a="banana"
b=a.rstrip()
print("of all fruits ",b,"is my favoourite.")

#از لغتی که دادی چپ و راستشو جدا میکنه
a="hello to everyone who hears me!!"
b=a.partition("everyone")
print(b)

#جا به جا کردن لغات با چیزی که میخوای
a="hello to everyone who hears me!!"
b=a.replace("h","p")
print(b)

#لغتی و مکان چیزی که میخوای رو بهت میده
a="hello to everyone who hears me!!"
b=a.rfind("to")
print(b)


#لغتی و مکان چیزی که میخوای رو بهت میده
a="hello to everyone who hears me!!"
b=a.rindex("to")
print(b)




#لغت را به مقداری که دادی به راست میبره
a="hello to everyone who hears me!!"
b=a.rjust(90)
print(b)


#لغتی که دادی رو میزاره وسط ما بقی جمله رو به دو قسمت تبدیل میکنه
a="hello to everyone who hears me!!"
b=a.rpartition("everyone")
print(b)


#داده ها را تبدیل به لیست میکنه
a="applee","pink","black"
b=a.rsplit(",")
print(b)



#جمله ی مارا تبدیل به لیست میکنه
a="hello to everyone who hears me!!"
b=a.split()
print(b)


#از اونجایی که  با اسلش جدا کردی تبدیل به  لیست میکنه
a="hello to everyone \who hears me!!"
b=a.splitlines()
print(b)


#اگر جمله با لغتی که میخوایم شروع شده باشه ترو برمیگردونه
a="hello to everyone who hears me!!"
b=a.startswith("hello")
print(b)


#lower=>upper   upper=> lower
a="hello to everyone who hears me!!"
b=a.swapcase()
print(b)


#حرف اول هر لغت رو به حروف بزرگ تبدیل میکنه
a="hello to everyone who hears me!!"
b=a.title()
print(b)

#به تعدادی که میخوای جا میگیره 0000000050
a="50"
b=a.zfill(10)
print(b)
# -------------------------------------------------------------------
#لیست ها هسس
#ساختن لیست بدون کروشه
thislist=list(("apple","cherry","blule"))
print(thislist)

#برگرداندن تعداد مشخص از ایتم های لیست
thislist=["appele","blue","cheery"]
print(thislist[:2])

#ببینیم ایتمی در لیست هست یا نه
thislist=["appele","blue","cheery"]
if "apple" in thislist:
  print("we have that here!")


#برای جابحا کردن دو آیتم با یکدیگر با استفاده از ایندکس
thislist=["appele","blue","cheery"]
thislist[1]="green"
#اگر بیشتر از یکی بود 
thislist[2:3]="green"



#اگر ایندکس داشتیم خواستیم ایتم اضافه کنیم از اینسرت استفاده میکنیم
thislist=["appele","blue","cheery"]
thislist.insert(2,"watermelon")
print(thislist)

#اگر خوواستیم به لیست اضافه کنیم که در این صورت ایتم میره ته لیست
thislist=["appele","blue","cheery"]
thislist.append("purple")
print(thislist)


#برای خذف ایتم با استفاده از ایتم ریمو
thislist=["appele","blue","cheery"]
thislist.remove("orange")
print(thislist)

#حذف ایتم با ایندکس
thislist=["appele","blue","cheery"]
thislist.pop(1)
print(thislist)


#حذف با استفاده از دیل و روش دوم کل لیست رو حذف میکنه
del thislist[1]
del thislist

#با این روش لیست رو خالی میکنه و تحویل میده
thislist=["appele","blue","cheery"]
thislist.clear()
print(thislist)

#تکته:اگر بیشتر از یک مورد همنام باشد خود به خود اولی رو پاک میکنه


#برای دسته بندی لیست اب سورت
thislist=["appele","blue","cheery"]
thislist.sort()
print(thislist)


#اگر خواستیم از بزرگ به کوچیک ترتیب بندی کنه از کلمه کلیدی پایین استفاده میکنیم
thislist=["appele","blue","cheery"]
thislist.sort(reverse=True)
print(thislist)


# در سورت کردن حروف بزرگ اول لیست میشن و بعد از آن حروف الفبا اگر خواستیم این مورد اعمال نشه از این روش استفاده میکنیم
thislist=["appele","blue","cheery"]
thislist.sort(key=str.lower)
print(thislist)


#برای برگرداندن لیست به صورت برعکس از روش زیر میزنیم
thislist=["appele","blue","cheery"]
thislist.reverse()
print(thislist)

#برای کپی کردن لیست  با دو روش
thislist=["appele","blue","cheery"]
mylist=thislist.copy()
#or
mylist=list(thislist)


#ادقام کردن دو لیست به دو روش
thislist=["appele","blue","cheery"]
thislist2=["appele","blue","cheery"]

for x in thislist2:
  thislist.append(x)
print(x)

thislist2.extend(thislist)
# -------------------------------------------------------------------
#tuple
#در تیوپل ها هر مقدار میتواند باشد با پرانتز است و اگر فقط یکی باشد باید بعد از ان ویرگول گذاشت  تا ان را تیوپل بشناسد
#اگر خواستیم کلا ان تیوپل را حذف کنیم باید از دیل استفاده کنیم
#تیوپل ها غیر قابل تغییر هستند نظم پذیر هستند ایتم تکراری میگیرند ایندکس دارند قابل حذف و اضافه شدن  وحا به جا کرد ن ندارن
tuple1=("apple","ali")
del tuple1
print(tuple1)

tuple1=("apple",)

#تیوپل را میتوان انپک کرد و برعکس برگرداند 
tuple2=("ali","hassan","abbas")
(green,red,blue)=tuple2
print(green)

#اگر تعداد مقداری که میخوایم انپک کنیم بیشتر از مقادیر اسمی مان بود از ستاره استفاده میکنیم که ان ستاره را اگر هر جایی بزاریم متناسب با مکان ان اسامی ما را تقسیم میکند
fruits=("apple","cherry","banana")
(red,*blue)=fruits
print(red)
print(blue)
# -------------------------------------------------------------------
#set ست ها
# ست ها برای نگه داری داده هاست و ایندکس پذیر نیست غیر قابل تغییر و ترتیب ندارد هر بار به صورت رندوم داده ها را بر میگرداند  
#علامت ان کروشه هست  مورد تکراری ندار د و نمیگیرد
# قابلیت حذف و اضافه کردن ایتم به ان را دارد و تعویض نمیشود
#اگر ترو و 1 باشد جفت ان را یکی میدونه و هر بار فقط یکی از ان را بر میگرداند
#برای اندازه گیری ان از لن استفاده میشه
# همه نوع دیتا در ان قرار میگیرد به صورت ایندکس نمیشه ایتیمی را برگرداند ولی از فور و این میشه استفاده کرد 
""".update/.remove/.discard/.intersection_update/.intersection/.symmetric_difference_update/.symmetric_difference/.copy/.difference/.difference_update/.isdisjoint/.issubset متد های ست="""

#برای اضافه کردن یک ست به ست دیگر از این استفاده میکنیم موردی که میخوایم اضافه کنیم حتما نباید ست باشه هر تایپی میتونه باشه
set1={"alireza","hassan","abbas"}
set2={"zahra"}
set2.update(set1)
print(set2)

#برای حذف کردن از ریمو و دیسکار میتونیم استفاده کنیم  تو دیسکار اگر اون مورد نباشه ارور نمیده
set1={"alireza","hassan","abbas"}
set1.remove("alireza")
set1.discard("hassan")
print(set1)

#عملگر های clear , delدقیقا مثل لیست ها عمل میکنند


#برای نگه داشتن ایتم مشابه در دو ست از این استفاده میکنیم
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}.intersection_update(set2)
#or 
set1.intersection(set2)   #در این حالت ست جدید میسازه و مورد رو میریزه توش
print(set2)


#با استفاده از این عملگر همه ی موار د رو به غیر از موارد تکراری و مشابه ها نگه میدارد
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1.symmetric_difference_update(set2)
#or
set1.symmetric_difference(set2) # در این حالت ست جدید ساخته و موارد ر و میریزه توش
print(set2)

#برای کپی کردن ایتم های یک ست  وریختن ان در یک ست دیگه از این استفاده میکنیم
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1.copy(set2)
print(set2)

#برای حذف ایتم های مشابه و ریختن ان در یک ست جدید از دیفرنت استفاده میکنیم
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1.difference(set2)
#or
set1.difference_update(set2)    #در این حالت موارد مشابه در دو لیست را حذف میکند
print(set2)



#اگر هیچ ایتمی از ست یک در ست دو نباشه با استفاده از این حالت ترو میده و موارد غیر را فالس میده
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1.isdisjoint(set2)
print(set2)

#اگر تمام مقادیر الف در ب باشد ترو میده
set1={"alireza","hassan","abbas"}
set2={"alireza","hassan","abbas","roghaye"}
set1.issubset(set2)
print(set2)
# -------------------------------------------------------------------
#dictionary دیکشنری ها 
#دیکشنری ها ایتم تکراری نمیگیرند
#key=value میگیرند
#بااستفاده از کی میتوان اطلاعات رو برگردوند
#از len برای مقدار دیکشنری میتوان استفاده کرد

#استفاده از کانستراکتر به این صورت است
thisdict=dict(name="alireza", age=20)
print(thislist)

#برای صدا زدن به صورت زیر است
dict1={"name":"alireza", "age":20}
print(dict1)

#برای صدا زدن از گت هم استفاده میشود
dict1.get("age")
print(dict1)

#با استفاده از کی میتوان تمام کی ها را در قالب لیست برگرداند
dict1.keys()
print(dict1)


#برای گرفتن ولیو هم از دات ولیو استفاده میکنیم
dict1.values()
print(dict1)

#. item تمام مقادیر را در تیوپل هایی که در لیست قرار دارند بر میگردونه
dict1.items()
print(dict1)

#if برای موجود بودن از ان استفاده میکنیم
if "apple" in dict1:
  print(dict1)
  
#برای تغییر ولیو ها به صورت زیر عمل میکنیم
dict1["name"]="alireza"

# برای تغییر و اپدیت لیست از اپدیت استفاده میکنیم
dict1.update({"year":2020})
print(dict1)

#برای اضافه کردن ایتم به لیست از ان استفاده میکنم
dict1["age"]=20
print(dict1)

#برای حذف ایتم چند روش هست POP/CLEAR/REMOVE/POPITEM
dict1.popitem()
print(dict1)

#برای حذف ایتم ها
dict1.pop("name")
print(dict1)

#برای حذف ایتم مشخص
del dict1 ["age"]
print(dict1)

#برای پاک کردن و خالی کردن لیست
dict1.clear()
print(dict1)

#»میتوان به صورت اختصاصی کی و و لیو را برگرداند
for age in dict1.values():
  print("hi")
for age in dict1.keys():
  print("bye")
  

#برای کپی کردن دو لیست 
dict1.copy(dict1)
#or
dict1=dict(dict1)
print(dict1)

#به دیکشنری هایی که در یکدیگر قرار دارند نستد میگویند
child1={"age":20,"name":"alireza"}
child2={"age":20,"name":"alireza"}
child3={"age":20,"name":"alireza"}
newchild={"child1":child1, "child2":child2, "child3":child3}


#برای دسترسی به ایتم ها در نستد
child3={"age":20,"name":"alireza"}
print(child3["child3"]["name"])

#.formkey برای برگرداندن ایتم ها به صورت کی و ولیو
x=("key1","key2","key3")
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)

#با استفااده از setdefault ایتم رو به صورت ولیو برمیگردونه و اگر نبود وارد میکنه
thisdict1={"name":"alireza","age":20}
thisdict2=thisdict1.setdefault("model","benz")
print(thisdict2)
#-------------------------------------------------------------------------------------------------
#lambda
"""
لامبدا ها همان فانکشن های خودمون هستند با این تفاوت که بسیار ساده و کوتاه تر هستند بسیار به کار میان و بهترین عملکرد انها زمانی است که در یک فانکشن
 دیگر قرار می گیرند. نکته مهم این است که یک لامبدا همیشه باید ساده باشد تحت هر شرایطی باید ساده باشد وگرنه باید یک فانکش بلند نوشت"""
#نکته: لامبدا همیشه باید در یک متغیرباشد تا بشه صداش زد مثل ایکس

#مثال فانکش و سااده سازی ان با لامبدا
def mydef(a):
  a+=10
  print(a)
mydef(a=10)
#بعد ساده سازی با لامبدا
x=lambda a:a+10
print(x(20))
#-------------------------------------------------------------------------------------------------
#arrays
#آرایه ها
#  آرایه ها کار مارابرای گشتن بسیار اسان میکند انها را باید داخل لیست گذاشت و بعد از ان تمام متد های لیست برای ان قابل پیاد سازی است
#  وقتی که تعداد داده زیادی داشته باشیم از ارایه ها میتوانیم استفاده کنیم
array1=["cherry","apple","banana","strawberry","banana"]
array2=[1,2,3,4]

#اضافه کردن
array1.extend(array2)

#شماره ایتم گرفتن
array1.index(2)

# وارد کردن و جا دادن با ایندکس
array1.insert(1,"orange")

#حذف کردن با شماره ایندکس
array1.pop(1)

#حذف ایتم ها با سام
array1.remove("cherry")

#پاک کردن داخل لیست
array1.clear()

#کپی کردن لیست
array1.copy()

#تعداد تکرار یک ایتم در لیست
array1.count("bananan")

#برعکس کردن لیست
array1.reverse()

#مرتب کردن لیست
array1.sort()

#اضافه کردن و چسباندن لیست
array1.append(array2)
#-------------------------------------------------------------------------------------------------
#دیتا بیس
#data base
import sqlite3
#ایحاد فایل
connection=sqlite3.connect("test_db.db")
#خودکار اینجا به معنی کرسر هست و جدول میکشه و دفتر میخره
cur=connection.cursor()
create_statement="""
CREATE TABLE  IF NOT EXISTS  customer(
    id,
    name,
    address,
    phone
)
"""
cur.execute(create_statement)
connection.close()
#برای وارد کردن حتما باید کانکشن ساخت و اگر فایل کلوز بود بازش کرد دوباره تا بشه وارد کرد
connection=sqlite3.connect("test_db.db")
cur=connection.cursor()
insert_statement="""
INSERT INTO customer (id,name,address,phone)
VALUES(2,"ali","dsds",322224)
"""
cur.execute(insert_statement)
connection.commit()
connection.close()
#--------------------------------------------------------
#برای شرطی کردن که مثلا اگر ایدی دو بود برگردون و .......
connection=sqlite3.connect("test_db.db")
cur=connection.cursor()
print(list(cur.execute("SELECT * FROM customer")))
print(list(cur.execute("SELECT * FROM customer WHERE  id = 2")))
#--------------------------------------------------------
cur.execute("DELETE from basket where number=3") 

#--------------------------------------------------------
#برای تغییر یکی از رکورد ها با چیز دیگری 
connection=sqlite3.connect("test_db.db")
cur=connection.cursor()
cur.execute("""
            UPDATE customer 
            SET address="hi"
            WHERE id=2
            """)
connection.commit()
connection.close()
#-------------------------------------------------------------------------------------------------
#وب اسکرپینگ با دیتا ساینس
import requests
from bs4 import BeautifulSoup

for i in range(1,11):
    url=rf"https://www.iranjib.ir/jax/showarchive.php?p=1&_id={i}"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    tablessoup=soup.findAll("table")
    linklist=tablessoup[0].findAll("a")
    urls=[]
    for item in linklist:
         urls.append(item.get("href"))
import sqlite3
connection=sqlite3.connect("iranjib.db")
cur=connection.cursor()
tablecreation="""
CREATE TABLE IF NOT EXISTS information(
    id,
    title,
    date,
    summary,
    content
)
"""
cur.execute(tablecreation)
connection.close()  
import sqlite3
from multiprocessing.pool import ThreadPool
def scrape(url):
    connection=sqlite3.connect("iranjib.db")
    cur=connection.cursor()
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    title=soup.find("h1", {"class":"titlenas"}).getText()
    summary=soup.find("div", class_="newssummary").getText()
    divmain=soup.find("div",{"class":"matn"})
    contentlist=divmain.findAll("p")
    content=""
    for p_item in contentlist:
         content += p_item.getText() +"\n"
    articlesoup=soup.find("article")
    tableslist=articlesoup.find("table")
    trlist=tableslist.findAll("tr")
    date=trlist[1].findAll("td")[1].getText()
    insertquery="""
    INSERT INTO information
    VALUES(?,?,?,?,?)
    """
    id=1
    cur.execute(insertquery,(id,title,date,summary,content))
    connection.commit()
connection.close()
pool=ThreadPool()
pool.map(func=scrape,iterable=urls)

#-------------------------------------------------------------------------------------------------
#مالتی تریدینگ یا موازی کاری
import threading
import time

def  print_cube(num):
    for i in range(1000000000):
        if i %(num**3)==0:
            print("cube:{}".format(i**6))
        time.sleep(1)
    
def print_square(num):
     for i in range(1000000000):
        if i %(num**3)==0:
            print("square:{}".format(i**6))
        time.sleep(1)
        
t1=threading.Thread(target=print_square,args=(5,))
t2=threading.Thread(target=print_cube,args=(10,))

t1.start()
t2.start()
t1.join()
t2.join()

print("done!")
#-------------------------------------------------------------------------------------------------
#یحث TRY /EXCEPT
#اگر کدی که زدیم در جایی ارور داد استوپ نکنه و ارور رو نشون بده و ادامه ی کد رو بزنه
"""
The try      => خط ها رو به دنبال ارور میگرده
The except   =>کمک میکنه تا ارور رو هندل کنی
The else     => اگر ارور نبود میزاره اجرا کنه کد رو
The finally  => بدون توجه به ترای و اکسپت نتیجه رو حاصل میکنه
raise        => به ما کمک میکنه تا ارور رو شناسایی کنیم و بگیم ارور داده
"""
a=20
try:
    # b=a/0
    a+="k"
except (ZeroDivisionError,TypeError) as e :
    print(f'error:{e}')
    a+=10
    print(a)
print("fuck you mother fucker")
#--------------------------------------------------
a=20
try:
    # b=a/0
    a+="k"
except TypeError as e :
    print(f'error:{e}')
    a+=10
    print(a)
print("fuck you mother fucker")
#--------------------------------------------------
a=20
try:
    a/0
    a+="k"
except ZeroDivisionError as e :
    print(f'error:{e}')
    a+=10
    print(a)
except TypeError as e:
    print(f"typeerror:{e}")
print(a)
print("fuck you mother fucker")
#--------------------------------------------------
try:
    print("hello")
except:("there is a problem")
else:("nothing went wrong")
#--------------------------------------------------
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#--------------------------------------------------
x=2
if x<3:
    raise Exception("we stop the program because of a specific problem.")

#-------------------------------------------------------------------------------------------------
#map
#خودش وصل میکنه به لیستمون و فرایند رو انجام میده
t=[1,2,3,4,4]
def pow(e):
    print(e**2)
print(list(map(pow,t)))

#filter
#لیست ما را بر اساس فیلتری که مینویسیم فیلتر میکنه باعث سریع تر شدن کار میشوند
def cfilter(e):
    if e>5 :
        print(True)
print(list(filter(cfilter,t)))
#-------------------------------------------------------------------------------------------------#json
#دیکشنری که استرینگ شده
#زبانی که رابط بین همه ی زبان های برنامه نویسی هست چون همه میشناسنش
#کد دیکشنری رو خواستی بدی به فرانت کار جیسون میکنی میدی
#جیسون بیلت این هست و باید واردش کنی
# و با دامپ باید تبدیل به جیسوون کنی
import json
dict1={
    "name":"alireza",
    "lastname":"azizi",
    "age":24
}
ouutfile=open("info.txt","w")
json.dump(dict1,ouutfile,indent=6)#تبدیل پایتون به جیسون
json.loads(dict1)#تبدیل جیسون به پایتون
a=ouutfile.close()
print(a)
#-------------------------------------------------------------------------------------------------#
#generator
#وقتی حافظه محدود هست باید از جنریتور استفاده کنیم که نیاز به یادگیری بیشتری دارد
def readline(path):
    lines=[]
    with open(r"D:\4-PYTHON COURSE\PYTHON\info1.txt") as f:
        for line in f:
            lines.append(line)
            yield lines
g=readline("info1.txt")
a=list(g)
print(a)
print(g)
#-------------------------------------------------------------------------------------------------#
#دکوراتور
from datetime import datetime
def loger(func):
    def wrapper(*args,**kwargs):
        with open("log.txt") as f:
            today=str(datetime.today())
            f.write(f"{func.__name__}in {today}is called"+"\n")
            original=func(*args,**kwargs)
            f.write(f"the return value of {func.__name__}in date {today}is {original}"+"\n")
    print(wrapper)
def myfunc(text):
    print(text.title())
a=loger(myfunc)("hi how are you?")
print(a)
#-------------------------------------------------------------------------------------------------#
#polymorphism
#وقتی میخوایم یک متد را به دفعات زیاد در کلاس های محتلف استفاده کنیم این کمکمون میکنه
class a:
    def move(self):
        print("move")
class b:
    def move(self):
         print("move")
class c:
    def move(self):
        print("move")
#-------------------------------------------------------------------------------------------------
#scope
#یک متغیر که فقط در داخل جایی که ساخته شده میشه ازش استفاده کرد
#دو حالت Local , globalدارد
#حالت لوکال داخلی هست
#حالت گلوبال خارجی هست
#برای تغییر لوکال به گلوبال از کیور گلوبال هم میشه استفاده کرد
#در ارث بری کاربرد دارد 
#دو فانکشن در یکدیگر هم همین کار را میکنند
#global
x=300
def myfunc():
    print(x)
#local
def myfunc():
    x=300
    print(x)
#-------------------------------------------------------------------------------------------------
#ماژول 
#ماژول ها مثل کتابخانه ها برای ما عمل میکنن و ما فایل را با پسوند پایتون سیو میکنیم وی میتونیم هر موقع لازم بود ایمپورت کنیم
def a(name):
    print("hi"+name)
#فایل بالا را مثلا سیو کردیم و در زیر میخوایم وارد کنیم
"""
import mymodule
mymodule.name("alireza")
"""
#اگر لازم بود میتوانیم فقط یک متغیر را صدا بزنیم از فایل
"""
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import mymodule

a = mymodule.person1["age"]
print(a)
"""
#اگر لازم بود میتونیم اسم فایل را عوض کنیم برای استفاده داخلی
"""
import mymodule as mx

a = mx.person1["age"]
print(a)

"""
#اگر خواستیم لیست تمام فانکشن و متغیر های داخل فایل رو ببینیم از دیر استفاده میکنیم
"""
 import platform

x = dir(platform)
print(x)  
 
"""
#برای وارد کردن متغیر یا فانکشن مشخصی از فرام استفاده میکنیم
""""
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1

print (person1["age"])

"""
#-------------------------------------------------------------------------------------------------
#استفاده از دیت تایم برای زمان و تاریخ
#کد زیر زمان حال را میده
import datetime
print(datetime.datetime.now())
#اگر خواستیم به طور مشخص بگیم مثلا سال یا ماه را بده از زیر میزنیم
print(datetime.datetime.year)
x = datetime.datetime.now()
print(x.strftime("%A"))
#اگر خواستیم ابجکت تاریخ بسازیم به روش زیر عمل میکنی
#کد پایین زمان را به صورت پیش فرض صفر در نظر میگیرد اما میتوانیم تا ثانیه زمان بدیم که دلخواه می باشد
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
#برای اینکه فایلی که میخوانیم قابل خواندن باشه میتونیم از اس تی ار استفاده کنیم به روش زیر
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
#تمام حالت های مخففی که به ما زمان میدن
"""
%a =>	Weekday, short version	Wed	
%A =>   Weekday, full version	Wednesday	
%w =>	Weekday as a number 0-6, 0 is Sunday	3	
%d =>	Day of month 01-31	31	
%b =>	Month name, short version	Dec	
%B =>	Month name, full version	December	
%m =>	Month as a number 01-12	12	
%y =>	Year, short version, without century	18	
%Y =>	Year, full version	2018	
%H =>	Hour 00-23	17	
%I =>	Hour 00-12	05	
%p =>	AM/PM	PM	
%M =>	Minute 00-59	41	
%S =>	Second 00-59	08	
%f =>	Microsecond 000000-999999	548513	
%z =>	UTC offset	+0100	
%Z =>	Timezone	CST	
%j =>	Day number of year 001-366	365	
%U =>	Week number of year, Sunday as the first day of week, 00-53	52	
%W =>	Week number of year, Monday as the first day of week, 00-53	52	
%c =>	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C =>	Century	20	
%x =>	Local version of date	12/31/18	
%X =>	Local version of time	17:41:00	
%% =>	A % character	%	
%G =>	ISO 8601 year	2018	
%u =>	ISO 8601 weekday (1-7)	1	
%V =>	ISO 8601 weeknumber (01-53)	01
"""
#-------------------------------------------------------------------------------------------------
#import re
#با این کار میتوان به استرینگ دسترسی گرفت و تغییراتی اعمال کرد
"""
findall =>	Returns a list containing all matches
search	=> Returns a Match object if there is a match anywhere in the string
split	=> Returns a list where the string has been split at each match
sub	    => Replaces one or many matches with a string
[]	    => A set of characters	"[a-m]"	
\	    => Signals a special sequence (can also be used to escape special characters)	"\d"	
.	    => Any character (except newline character)	"he..o"	
^	    => Starts with	"^hello"	
$	    => Ends with	"planet$"	
*	    => Zero or more occurrences	"he.*o"	
+	    => One or more occurrences	"he.+o"	
?	    => Zero or one occurrences	"he.?o"	
{}	    => Exactly the specified number of occurrences	"he.{2}o"	
|	    => Either or	"falls|stays"	
()	    => Capture and group
\A	    => Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	    => Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"	
\B	    => Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"	
\d    	=> Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	    => Returns a match where the string DOES NOT contain digits	"\D"	
\s	    => Returns a match where the string contains a white space character	"\s"	
\S	    => Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	    => Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	    => Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	    => Returns a match if the specified characters are at the end of the string	"Spain\Z"
[arn]	=> Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	=> Returns a match for any lower case character, alphabetically between a and n	
[^arn]	=> Returns a match for any character EXCEPT a, r, and n	
[0123]	=> Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	=> Returns a match for any digit between 0 and 9	
[0-5][0-9]	=> Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	=> Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        => In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""
#-------------------------------------------------------------------------------------------------
#formating
#بعضی مواقع اطلاعاتی و متن هایی میگیریم که کنترلی روش نیست مثلا از دیتا بیس میاد برای اینکه تغییر بدیم و اضافه کنیم از فورمتین استفاده میکنیم به صورت زیر:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#عدد را به صورت دو عدد اعشار نشون میده
txt = "The price is {:.2f} dollars"
#چند تا داده
print(txt.format(price, price, price))
#اگر ترتیب داشته باشیم و با ترتیب بنویسیم میتونیم مالتی جواب بدیم
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#میتونیم ایندکس بدیم و همچنین اگر خواستیم از یک داده استفاده کنیم میتونیم با ایندکس یکسان استفاده کردن این کار را بکنیم
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
myorder = "I want {1} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#همچنین با اسم دادن هم میتونیم این کار رو بکنیم
list1= "i have a {carname} ,for {year} years."
print(list1.format(carname="ford", years=24))
#-------------------------------------------------------------------------------------------------
#کار با فایل ها
#برای باز کردن فایل ها از روش زیر استفاده میکنیم
a=open(r"D:\4-PYTHON COURSE\PYTHON\info1.txt","r")
"""
"r" => Read - Default value. Opens a file for reading, error if the file does not exist
"a" => Append - Opens a file for appending, creates the file if it does not exist
"w" => Write - Opens a file for writing, creates the file if it does not exist
"x" => Create - Creates the specified file, returns an error if the file exists
"t" => Text - Default value. Text mode
"b" => Binary - Binary mode (e.g. images)
"""
#برای باز کردن فایل روی سرور از دستور  رید استفاده میکنیم
f = open("demofile.txt", "r")
f.close()
print(f.read(5))
#مهمه که بعد از استفاده از فایل ان را ببندیم
#همچنین با دادن عدد به رید میتونیم مشخص کنیم چند خط از فایل رو بخونه

#برای برگردوندن خط به خط فایل از دستور رید لاین یا رید لاینز استفاده میکنیم
f = open("demofile.txt", "r")
print(f.readline())
#اگر فایل وجود نداشت و خواستیم انرا بوجود بیاریم از روش زیر استفاده میکنیم
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
"""
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"x" - Create - will create a file, returns an error if the file exist
"""
#یرای حذف فایل از روش زیر استفاده میکنیم و نیاز هست تا کتابخونه ی او اس را وارد کنیم
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#با استفاده از روش زیر میتونیم کل فولدر رو  پاک کنیم فقط در صورتی که فولدر خالی باشه
import os
os.rmdir("myfolder")
#-------------------------------------------------------------------------------------------------
#تمرین وب اسکرپینگ
import requests
from bs4 import BeautifulSoup
url=r"https://www.iranjib.ir/jax/showarchive.php?p=1&_id=1"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
tablessoup=soup.findAll("table")
linklist=tablessoup[0].findAll("a")
urls=[]
for item in linklist:
    urls.append(item.get("href"))
# print(urls)

urls=[]
for i in range(1,11):
    url=rf"https://www.iranjib.ir/jax/showarchive.php?p=1&_id={i}"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    tablessoup=soup.findAll("table")
    linklist=tablessoup[0].findAll("a")
    for item in linklist:
         urls.append(item.get("href"))
# print(len(urls))
# print(urls[0])


import sqlite3
connection=sqlite3.connect("iranjib.db")
cur=connection.cursor()
tablecreation="""
CREATE TABLE IF NOT EXISTS information(
    id,
    title,
    date,
    summary,
    content
)
"""
cur.execute(tablecreation)
connection.close()  

import sqlite3
connection=sqlite3.connect("iranjib.db")
cur=connection.cursor()
id=0
for url in urls:
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    title=soup.find("h1", {"class":"titlenas"}).getText()
    summary=soup.find("div", class_="newssummary").getText()
    # print(title)
    # print(summary)
    divmain=soup.find("div",{"class":"matn"})
    contentlist=divmain.findAll("p")
    # print(contentlist[0])
    content=""
    for p_item in contentlist:
         content += p_item.getText() +"\n"
    # print(content)
    articlesoup=soup.find("article")
    tableslist=articlesoup.find("table")
    # print(len(tableslist))
    trlist=tableslist.findAll("tr")
    date=trlist[1].findAll("td")[1].getText()
    insertquery="""
    INSERT INTO information
    VALUES(?,?,?,?,?)
    """
    id+=1
    cur.execute(insertquery,(id,title,date,summary,content))
    connection.commit()
connection.close()
#-------------------------------------------------------------------------------------------------
#numpy
#کتابخانه ای که در ترسیم نمودار ها ، اعمال ریاضی و همچنین عملکردی مانند لیست ها اما بهینه تر دارند
#کار آن کلا با آرایه هاست
#برای ساخت آن باید از array استفاده کرد
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
#چهار حالت داریم

#0d
import numpy as np
arr = np.array(42)
print(arr)

#1d
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2d
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3d
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

#برای چک کردن دامنشن یا ابعاد هر ارایه از روش زیر استفاده میکنیم
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#اگر خواستیم ابعاد بیشتر استفاده کنیم به صورت زیر عمل میکنیم
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#مانند لیست ها ایندکس پذیر هستند
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

#ایندکس گرفتن در بیشتر از یک دایمنشن
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

#ایندکس گرفتن در 3 دایمنشن
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#ایندکس گرفتن از آخر به اول
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

#مانند لیست ها اسلایس میگیرند
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#استپ میگیرند مثل لیست ها
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

#یک دایمنشن
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#اگر خواستیم نوع و تایپ اون آرایه رو چک کنیم به روش زیر میزنیم
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

#اگر خواستیم تایپ مشخص بدیم به روش زیر 
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


#اگر خواستیم تایپ رو عوض کنیم به روش زیر
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#کپی کردن باعث تغییر در ارایه اصلی نمیشود
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#در ویو به این صورت نیست
#تغییر در اصل یا فرع تاثیر میزاره رو هر کدوم از آنها
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)


#اعمال تغییر در ویو
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

#شیپ هر آرایه تعداد شماره های در هر کدوم از دایمنشن هاست
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#عدد 5 نشان دهنده ی 4 داده در ارایه هست
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


#کد زیر میشه 4 ارایه با هر کدوم 3 المان
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#دو ارایه که هرکدام 3 ارایه دارند که شامل 2 المان هستند
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#کد زیر 2 ارایه میده که هر کدام 2 ارایه دارند که 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#کد زیر همه ی ارایه ها را تبدیل به یکی میکند
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#برای اینکه المان ها را به صورت ساده بگیریم و ارایه نده به صورت زیر میزنیم
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
  
#کار بالا را به صورت ردیفی انجام میده
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
  
#بستگی به تعداد دایمنشن ها داره و باید تکرار کرد به صورت زیر
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
      
#به کمک ان ادیتور میتونیم کل کار بالا را انجام دهیم
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
  
#ایتریت کردن به کمک تایپ های متفاوت
import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  
#ایتریت کردن به کمک استپ های متفاوت
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
  
#عدد ایندکس رو میده و بعد عدد رو میده به روش زیر
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
#ادغام ارایه ها با یکدیگر
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#کار بالا در یک دایمنشن
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#همون کار با استاک
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

#انجام کار بالا به صورت ردیفی
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

#انجام کار بالا به صورت ارایه و ردیفی
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

#انجام کار بالا به صورت ستونی
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

#اسپلیت کردن
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

#برای سرچ کردن و پیدا کردن ارایه مورد نظر
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#پیدا کردن جای مناسب یک المان
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

#انجام کار بالا با جهت دهی مثلا از راست باشه یا از چپ
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

#سورت کردن و ترتیب بندی
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#فیلتر کردن یعنی کاری که میخوایم رو اعمال کنیم و بعد خروچی بگیریم
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


#ایجاد آرایه ی تصادفیک
from numpy import random
x = random.randint(100)
print(x)


#ایجاد آرایه ی تصادفی بین صفر و یک
from numpy import random
x = random.rand()
print(x)

#بین صفر و صد پنج داده تصادفی بده
from numpy import random
a=random.randint(100,size=(5))
print(a)

# سه ردیف داده تصادفی به ما بده که هر کدوم از آنها تصادففی هستند
from numpy import random
a=random.randint(100,size=(3,5))
print(a)

#به ما آرایه با یک دایمنشن میده که شامل 5 عدد تصادفی هست
from numpy import random
a=random.rand(5)
print(a)


#مثال بالا با 2 دایمنشن و سه ردیف شامل 5 داده تصادفی
from numpy import random
a=random.rand(3,5)
print(a)

#با چویس میتونیم بر طبق آرایه داده ها میتونیم جنریت کنیم 
from numpy import random
a=random.choice([3,4,5,6,7])
print(a)


#داده ای که 100 تا باشه تصادفی باشه و جواب از سه پنج و هفت باشه
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

#همون کد بالا فقط با دو دایمنشن
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

#شافل کردن داده های ما 
from numpy import random
import numpy as np

a=np.array([1,2,3,4,5,6])
random.shuffle(arr)
print(arr)

#کار شافل رو میکنه ولی داده ی اصلی رو تغییر نمیده بر عکس شافل
arr=np.array([1,2,3,4,5,6])
print(random.permutation(arr))

#کد های این قسمت کمک به ترسیم نمودار های مختلف میکند
#برای رسم این نمودار ها باید از کتابخونه سی بورن استفاده کنیم
import matplotlib.pyplot as plt
import seaborn as sns 
sns.displot([0,1,2,3,4,5],hist=False)
plt.show()
#هیست در بالا به ما کمک میکند که هیستوگرام داشته باشیم یا نه 

#توزیع نرمال
from numpy import random
a=random.normal(size=(2,3))
print(a)

#نمودار با انحراف معیار 2
from numpy import random
a=random.normal(loc=1,scal=2,size=(2,3))
print(a)

#نشان دادن نمودار ی محاسبه بالا
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000),hist=False)
plt.show()

#توزیع دم جمله ای یک توزیع گستته 
from numpy import random
a=random.binomial(n=10,p=0.5,size=10)
print(x)

sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)
plt.show()

#حالت زیر به ما کمک میکند که یک رویداد در یک زمان مشخص چند بار میتواند رخ دهد
from numpy import random
x=random.poisson(lam=2,size=10)
print(x)

sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()


#برای تتوصیف احتمالی استفاده می شود که در آن هر رویداد شانس یکسانی برای وقووع دارد
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

a=random.uniform(size=(2,3))
print(a)

sns.distplot(random.uniform(size=1000),hist=False)
plt.show()

#توصیف لجستیک برای توصیف رشد استفاده میشود
a=random.logistic(loc=1,scale=2,size=(2,3))
print(a)

sns.distplot(random.logistic(size=1000),hist=False)
plt.show()

#توزیع چند جمله ای تعمیم توزیع دو جمله ای است
a=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6,])
print(a)


#توزیع نمایی برای توصیف زمان تا رویداد بعدی به عنوان مثال استفاده میشود در شکست/موفقیت و غیره
from numpy import random
import matplotlib.pyplot  as plt
import seaborn as sns
a=random.exponential(scale=2,size=(2,3))
print(a)

sns.distplot(random.exponential(scale=1000),hist=False)
plt.show()

#توزیع چی که به عنوان مبانیی برای تایید فرضیه استفاده میشود
a=random.chisquare(df=2,size=(2,3))
print(a)
sns.distplot(random.chisquare(df=2,size=(2,3)))
plt.show()

#توزیع ریلی در پردازش سیگنال استفاده میشود
a=random.rayleigh(scale=2,size=(2,3))
print(a)

sns.distplot(random.rayleigh(scale=2,size=(2,3)))
plt.show()

#توزیعی که از قانون بیست هشتاد استفاده میکند
a=random.pareto(a=2,size=(2,3))
print(a)

sns.distplot(random.pareto(a=2,size=1000),hist=False)
plt.show()

#برای نمونه برداری از داده ها بر اساس قانون زیپف استفاده میشود
a=random.zipf(a=2,size=(2,3))
print(a)

a=random.zipf(a=2,size=1000)
sns.distplot(x[x<10],kde=False)
plt.show()

#تمام مطالب زیر در رابطه با یوفانک هست
#برای جمع کردن المان های دو داده به صورت ستونی و ریختن در ارایه جدید
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[]
for i,j in zip(a,b):
  c.append(i,j)
print(c)

#برای انجام کار بالا میتونیم از ادد هم استفاده کنیم که نتیجه یکسان میده
a=[1,2,3,4]
b=[5,6,7,8]
z=np.add(x,y)
print(z)

#ساختن یو فانک مخصوص به خودت که کار مشخصی انجام میده و باید اون رو وارد نامپای کنی 
import numpy as np
def myadd(x,y):
  print(x,y)
mmyadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4,5,6],[7,8,9,10,11]))

#ادد محتوا را جمع میکند و اراعه میدهد
import numpy as np
arr1=([1,2,3,4,5,6])
arr2=([1,2,3,4,5,6])
newarr=np.add(arr1,arr2)
print(newarr)

#کم کردن داده های دو المان
arr1=([1,2,3,4,5,6])
arr2=([1,2,3,4,5,6])
newarr=np.subtract(arr1,arr2)
print(newarr)

#ضرب کردن المان ها
arr1=([1,2,3,4,5,6])
arr2=([1,2,3,4,5,6])
newarr=np.multiply(arr1,arr2)
print(newarr)

#تقسیم کردن
arr1=([1,2,3,4,5,6])
arr2=([1,2,3,4,5,6])
newarr=np.divide(arr1,arr2)
print(newarr)

#به توان رساندن
arr1=([1,2,3,4,5,6])
arr2=([1,2,3,4,5,6])
newarr=np.power(arr1,arr2)
print(newarr)

#دو تابع زیر باقیمانده مقادری آرایه او مربوط به مقادری آرایه دوم را بر میگرداند و نتایج را در یک آرایه جدید بر  میگرداند
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr=np.mod(arr1,arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr=np.remainder(arr1,arr2)
print(newarr)


#این تابع هم ضریب و هم مد را بر میگرداند اولی ضریب و دومی مد هست
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr=np.divmod(arr1,arr2)
print(newarr)

#این تابع عملیات مطلق یکسان را انجام میدهند اما باید از ابسولوت استفاده کنیم تا با مث اشتباه نگیرد
arr=np.array([-1,-2,1,2,3-4])
newarr=np.absolute(arr)
print(newarr)


#برای رند کردن از تابع های زیر استفاده میکنیم
#trunction-fix-rounding-floor-ceil
import numpy as np
a=np.trun([-3.166,3.2222])
print(a)

a=np.fix([-3.166,3.2222])
print(a)

a=np.round([-3.166,3.2222])
print(a)

#به سمت پایین رند میکنه
a=np.floor([-3.166,3.2222])
print(a)


#به سمت بالا رند میکنه
a=np.ceil([-3.166,3.2222])
print(a)


#تابع در پایه 2 برمیگرداند
import numpy as np
arr=np.arange(1,10)
print(np.log2(arr))

#کار بالا در پایه 10
arr=np.arange(1,10)
print(np.log2(arr))

#کار بالا در پایه e

arr=np.arange(1,10)
print(np.log(arr))


#میتوانیم برای یه تابع داخلی ریاضی با دو پارامتر ورودی و یک پارامتر خروجی استفاده کینم
from math import log
import numpy as np

nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))

#جمع کردن المان های داخل یک تابع به صورت ستونی

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)

#این هم همون کار رو انجام میده اما تعداد المان بیشتری مییگره ولی ادد فقط 2 المان میگیره
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

#با اکس 
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

#cumsumکمک میکنه تا المان ها را دونه دونه اضافه کنیم
arr=np.array([1,2,3])
newarr=np.cumsum(arr)
print(newarr)

#پیدا کردن حاصل ضرب عناصر در یک آرایه از این تابع استفاده میکنیم
import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

#کار بالا با اکس ها
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)


#ضرب دونه دونه عناصر در هم
import numpy as np
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)

#کم کردن عناصر ها از یکدیگر
arr = np.array([10, 15, 25, 5])
newarr=np.diff(arr)
print(newarr)

#تکرار روند کم کردن
arr = np.array([10, 15, 25, 5])
newarr=np.diff(arr,n=2)
print(newarr)

#پیدا کردن پایین ترین مخرج مشترک
num1=4
num2=6
a=np.lcm(num1,num2)
print(a)

#پایین ترین مخرچ مشترک در آرایه
arr = np.array([3, 6, 9])
a=np.lcm.reduce(arr)
print(a)

import numpy as np
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)

#پیدا کردن بزرگترین مخرچ مشترک
num1=6
num2=10
a=np.gcd(num1,num2)
print(a)

#پیدا کردن بالایی در آرایه ها
a=np.array([1,2,3,4,5,5])
b=np.gcd.reduce(arr)
print(b)

#سینوس و کسینوس و رادیان و تانژانت
a=np.sin(np.pi/2)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)


arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)

x = np.arcsin(1.0)

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)

base = 3
perp = 4
x = np.hypot(base, perp)

#توابع زیر مقدار را بر حسب رادیان میگیررد و مقادیر لازمه را تولید میکند
import numpy as np
a=np.sinh(np.pi/2)
print(a)

#در آرایه
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

#پیدا کردن زاویه ها
import numpy as np
x = np.arcsinh(1.0)
print(x)

#Find the angle for all of the tanh values in array:
import numpy as np
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)

#مانند ست عمل میکند و تکراری ها را حذف میکند
arr=np.array([1,1,1,1,1,1,2,2,2,2,2,2,4,2,5,6,7,7])
a=np.unique(arr)
print(a)

#مشترکارو پیدا میکنه
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr=np.union1d(arr1,arr2)
print(newarr)

#برای یافتن تنها مقادیر موجود در هر دو آرایه از این متد استفاده میکنیم
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr=np.intersect1d(arr1,arr2,assume_unique=True)
print(newarr)

#تفاوتا رو پیدا میکنه
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)


#برای یافتن تنها مقادیری که در هر دو مجموعه وجود ندارند از متد استفاده میکنیم
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)

#-------------------------------------------------------------------------------
#کتابخانه پانداس
#پانداس یک کتابخانه برای انالیز داده هاست
#برای انالیز،پاک کردن،گشتن و دستکاری داده هاست
#به ما کمک میکنه ببینیم ارتباطی بین دو یا چند ردیف از داده ها هست یا نه
#بالاترین داده/پایین ترین داده/و داده ی میانگین کدام است
#کمک میکنه تا ردیف هایی که همخوانی ندارند را پاک کنه یا مقدار اشتباه دارند مثل خالی ها

#ساختار زیر به ما دو تا ردیف میده که شامل اسم ماشین و شماره ایندکس و شماره ان میباشد
import pandas
mydataset={
    "cars":["bmw","volvo","ford"],
    "passings":[3,4,5]
}
a=pandas.DataFrame(mydataset)
print()

#سریال در این کتابخانه مثل ردیف در تیبل هست
#یک ارایه یک بعدی هست که هرنوع داده ای را داخل خود نگه میدارد
#کد زیر ایندکس را به همراه شماره ی ان برمیگرداند
import pandas as pd
a=[2,3,5,5]
b=pd.Series(a)
print()

#اگر المان ها با چیز خاصی صدا زده نشوند انگاه با لیبل یا همون ایندکس صدا زده میشوند
a=[1,2,3,4,5]
b=pd.Series(a)
print(b[1])


import pandas as pd

#با ایندکس دهی میتونیم لیبل بسازیم
a=[1,2,3]
b=pd.Series(a,index=["x","y","z"])
# print(b)
# print(b["y"])

#کلید و واژه به عنوان سریال
#مثل دیکشنری ها میتونیم باهاشون سریال بسازیم
#کلید ها لیبل میشن
mypd={"day1":"saturday","day2":"SUNDAY","day3":"monday"}
a=pd.Series(mypd)
# print(a)

l1={"day1":100,"day2":200,"day3":300}
b=pd.Series(l1,["day3","day1"])
# print(b)

#دیتا فریم تیبل های  چند بعدی هستند
#سریال ها مثل ردیف ها هستند و دیتا فریم ما کل اون تیبل هست
data = {
    "duration": [50, 40, 45],
    "calories": [420, 380, 390]

}
b=pd.DataFrame(data)
# print(b)

import pandas as pd

#دیتا فریم یک دیتا استراکچتر دو بعدی هست مثل یک ارایه ی 2 بعدی یا یک تیبل با ردیف و ستون
data={
    "duration":[223,2323,322],
    "calories":[2,3,4]
}
#اینجا ما اطلاعات را وارد دیتا فریم کردیم
a=pd.DataFrame(data)
# print(a)

#اگر خواستیم جای ردیف را ببینیم از لاک استفاده میکنیم
# print(a.loc[1])


#برگرداندن با ردیف صفر ویک
print(a.loc[[1,2]])

#وقتی از []استفاده میکنیم یعنی داده تو دیتا فریم هست


#نام گذاری ایندکس های ما
#با کد زیر میخوایم ردیف هامون رو اسم گذاری کنیم
b=pd.DataFrame(data,index=["day1","day2","day3"])
# print(b)

#برای دیدن جای لاک ها از لاک استفاده میکنیم
# print(b.loc["day2"])


#بارگذاری فایل ها داخل دیتا فریم
df=pd.read_excel("NASEHI.xlsx")
# print(df)

import pandas as pd

#یک راه برای ذخیره کردن اطلاعات بزرگ استفاده از csv هست.
#بارگذاری این فایل در دیتا فریم
import pandas as pd

df = pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
#پرینت پایین کل دیتا فریم رو برمیگردونه
print(df.to_string()) 

#----------------------------------------------------------------------------------
#روش دیگه برای برگردوندن کل اطلاعات
#اگر داده ها زیاد باشند پانداس فقط پنج تای اول و پنج ردیف اخر رو بر میگردونه
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
print(df)

#برای دیدن ماکسیمم ردیف ها کد زیر رو میشه زد
import pandas as pd

print(pd.options.display.max_rows)

#اگر خواستیم ردیف ها رو تغییر بدیم از کد زیر میزنیم
pd.options.display.max_rows=9000
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
print(df)

import pandas as pd

#وارد کردن فایل جی سان 
#بیگ دیتا ها معمولا ذخیره یا استخراج میشوند به عنوان فایل جی سان
df=pd.read_json(r"D:\4-PYTHON COURSE\PYTHON\data.js")
print(df.to_string())

#جیسون مثل دیکشنری میمونند 
#اگر فایل جیسون نداری و داخل دیکشنری هستند میتونی از همونجا بخونیش

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 


import pandas as pd

#آنالیز داده ها با پانداس
#هد به ما کمک میکنه یک نگاه کلی راجع به داده ها و تعداد مشخصی از  ردیف ها را داشته باشیم
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
# print(df.head(3))

#متد تیل به ما کمک میکنه تا آخرین ردیف ها را ببینیم
print(df.tail())

#متد اینفو اطلاعات بیشتری به ما میده راحع به داده ها
print(df.info())


import pandas as pd
#پاک کردن دیتا ها یعنی دیتاهای خراب را درست کنیم
#دیتاهای خراب میتونن سلول های خالی ، فرمت اشتباه،دیتا اشتباه،تکراری ها باشند
#پاک کردن سلول های خالی
#سلول های خالی میتونن مشکل ایجاد کنن در بررسی داده ها
#به کمک کد زیر میتونیم سلول های خالی را پاک کنیم
#دراپنا دیتای جدید ایجاد کرده و تغییرایجاد میکند و در دیتای اصلی تغییری ایجاد نمیکند
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
new_df=df.dropna()
print(new_df.to_string())

#با کد زیر تمام ردیف ها را حذف میکنیم
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df.dropna(inplace=True)
print(df.to_string())

#جابجایی کردن ردیف های خالی با ردیف های پر
#تو این ردیف لازم نیست کل این ردیف ها را پاک کنیم
#fillna
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df.fillna(130,inplace=True)
print(df)

#مثال جابجا کردن ردیف خالی با المان خاصی
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df["Calories"].fillna(130,inplace=True)
print(df.to_string())


#یکی از روش های جابجا کردن سلول های خالی محاسبه کردن میانه،مد، و مین های المان هاست
a=df["Calories"].mean()
b=df["Calories"].median()
c=df["Calories"].mode()[0]
df["Calories"].fillna(a,inplace=True)
print(df.to_string())

#برای فیکس کردن دیتا با فرمت اشتباه دو کار داریم یا باید حذف کنیم یا تمام ردیف ها را کانورت کنیم 
#برای تبدیل داده اشتباه به فرمت زمان
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df["Date"]=pd.to_datetime(df["Date"])
print(df.to_string())


#برای حذف ردیف ها از کد زیر استفاده میکنیم
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df.dropna(subset=["Date"],inplace=True)
print(df.to_string())


#فیکس کردن دیتای اشتباه
#برای وارد کردن یک داده به ردیفی مشخص
df.loc[7,"Duration"]=45


#اگر دیتای ما کوچک باشد دونه دونه میتوان آنها را تصحیح کرداما اگر دیتای بزگتری باشد باید یک روند کلی بنویسیم براش
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=120
        
#کار بالا اما برای حذف کردن داده ها
for i in df.index:
    if df.loc[i,"duration"]>120:
        df.drop(i,inplace=True)
        
        
#حذف کردن مقادیر تکراری
#برای دیدن مقادیر تکراری میتونیم از کد زیر استفاده کنیم
print(df.duplicated())

#کد زیر برای حذف مقادیر تکراری
df.drop_duplicates(inplace=True)

#وقتی اینپلیس ترو میزنیم یعنی میخوایمم مطمین بشیم که تغییرات در نسخه اصلی هست نه در دیتای جدید

import pandas as pd
#پیدا کردن ارتباطات با پانداس
#متد کور به ما در این رایطه کمک میکند
#این متد رابطه ی بین هر ستون رو محاسبه میکند
##این متد ستون های غیر عددی را نادیده میگیرد
#نتیجه را به صورت دو عدد منفی یک و یک میدهد که اگر بالا تر از نه دهم باشد به بالا خوب است و اگر افزایش بدیم بقیه هم افزایش پیدا میکند
#منفی نه دهم هم خوب هست اما اگر اگر متغیری را افزایش دهیم دیگری افزایش پیدا نمیکند
#اگر د, دهم باشد یعنی رابطه خوبی ندارند اگر یک متغیری افزایش پیدا کند دیگری پیدا نمیکند
a=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
b=a.corr()
print(b)



#اماده کردن دیاگرام به کمک پانداس
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
# df.plot()
# plt.show()

#گرفتن نمودار پراکندگی 
#kind="scatter"
#داده بالا x,y میگیرد
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df.plot(kind="scatter",x="Duration",y="Calories")
plt.show()


#کار با هیستوگرام
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\4-PYTHON COURSE\PYTHON\data.csv")
df["Duration"].plot(kind="hist")
plt.show()
#----------------------------------------------------------------------------------
#scipy library
#scientific python
#این کتابخانه از نامپای در پشت صحنه استفاده میکند
#کمک به بهینه سازی و سگنال پراسسینگ میکند
#با کد زیر میتوان لیست تمام  واحد ها را در ماژول ثابت مشاهده کرد

from scipy import constants
print(dir(constants))

#واحد مشخص شده را بر حسب متر بر میگرداند
print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21


#واحد مشخص را بر حسب بایت بر میگرداند
print(constants.kibi)
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)

#واحد مشخص را بر حسب کیلوگرم میده
print(constants.gram)
print(constants.metric_ton)
print(constants.grain)
print(constants.lb)
print(constants.pound)
print(constants.oz)
print(constants.ounce)
print(constants.stone)
print(constants.stone)
print(constants.long_ton)
print(constants.short_ton)
print(constants.troy_ounce)
print(constants.troy_pound)
print(constants.carat)
print(constants.atomic_mass)
print(constants.m_u)
print(constants.u)

#واحد های مشخص بر حسب رادیان میده
print(constants.degree)
print(constants.arcmin)
print(constants.arcminute)
print(constants.arcsec)
print(constants.arcsecond)

#واحد های مشخص بر حسب ثانیه میده
print(constants.minute)
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)

#واحد های مشخص برای طول
print(constants.inch)
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.micron)
print(constants.au)
print(constants.astronomical_unit)
print(constants.light_year)
print(constants.parsec)

#فشار
print(constants.atm)
print(constants.atmosphere)
print(constants.bar)
print(constants.torr)
print(constants.mmHg)
print(constants.psi)

#محیط و فضا
print(constants.hectare)
print(constants.acre)

#حجم
print(constants.liter)
print(constants.gallon)
print(constants.gallon)
print(constants.gallon_US)
print(constants.gallon_imp)
print(constants.fluid_ounce)
print(constants.fluid_ounce_US)
print(constants.fluid_ounce_imp)
print(constants.barrel)
print(constants.bbl)


#سرعت
print(constants.kmh)
print(constants.mph)
print(constants.mach)
print(constants.speed_of_sound)
print(constants.knot)

#دما
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)

#انرژی
print(constants.eV)
print(constants.electron_volt)
print(constants.calorie)
print(constants.calorie_th)
print(constants.calorie_IT)
print(constants.erg)
print(constants.Btu)
print(constants.Btu_IT)
print(constants.Btu_th)
print(constants.ton_TNT)

#قدرت
print(constants.hp)         #745.6998715822701
print(constants.horsepower) #745.6998715822701


#فشار
print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665

#بهینه ساز ها یا ریشه یک معادله رو میدن یا حداقل و کوچک ترین مقدار را
#نامپای قادر به یافتن ریشه یک معادله خطی است اما غیر خطی را خیر
#برای معادله غیر خطی از سای پای استفاده میکنیم

#مثال
from scipy.optimize import root
from math import cos
def eqn(x):
    print(x+cos(x))
myroot=root(eqn,0)
print(myroot.x)

#نشان دادن منحنی ها 
#ماکسیمم و مینیمم منحنی ها

from scipy.optimize import minimize
def eqn(x):
    print(x ** 2 + x +2)
mymin=minimize(eqn,0,method="BFGS")
print(mymin)

#sparse data
#داده هایی هستند که المان های بی استفاده دارند یعنی معنی خاصی ندارند
#دو نوع دارد csc /csr
#csr=برای برش  سریع ردیف های فشرده 
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([0,0,0,0,0,1,1,1,1,2])
# print(csr_matrix(arr))


arr=np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)

#محاسبه ی غیر صفر ها
print(csr_matrix(arr).count_nonzero())

#حذف صفر ها از ماتریکس با این متد
mat=csr_matrix(arr)
mat.eliminate_zeros()
print(mat)


#حذف تکراری ها
mat=csr_matrix(arr)
mat.sum_duplicates()
print(mat)


#تبدیل سی اس ار به سی اس سی
newarr=csr_matrix(arr).tocsc()
print(newarr)

#csc=ستون ها را این کار میکند

#گراف ها شکل مهمی از دیتا استراکچرا هستند
#پیدا کردن تمام اطلاعات مرتبط با هم
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr)
print(connected_components(newarr))

#با استفاده از متد زیر میتونیم کوتاه ترین راه بین دو المان را میشه پیدا کرد
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr)
print(dijkstra(newarr,return_predecessors=True,indices=0))


#پیدا کردن کوتاه ترین راه بین تمام المان ها
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))


#کار بالا را انجام میدهد اما وزن منفی هم بدست میاورد
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))


#این اولین پیمایش عمق را از یک گره برمیگرداند
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

#اولین پیمایش وسعت را از یک گره برمیگرداند
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))

#داده های مکانی به داده هایی اطلاق می شود که در یک فضای هندسی نمایش داده میشوند
#با این روش یک چند ضلعی را به چند مثلث تبدیل میکنیم تا بتوانیم مساحت آنرا بدست اوریم
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points=np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
])
simplices=Delaunay(points).simplices
plt.triplot(points[:,0],points[:,1],simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()

#بدنه محدب کوچکترین چندضلعی است که تمام نقاط داده شده را پوشش میدهد
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

#یک ساختار داده ای است که برای پرسجو نزدیکرتین همسایه بینه شده است
#kd=ابجکت کی دی را برمیگردونه
#کوعری هم به ما تزدیک ترین همسایه یا محل ان را میده
from scipy.spatial import kdTree
points=[(1,-1),(2,3),(-2,3),(2,-3)]
kdtree=kdTree(points)
res=kdtree.query((1,-1))
print(res)


#فاصله بین دو نقطه و کار های دیگه میکنه
from scipy.spatial.distance import euclidean
p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)

#فاصله را با 4 جهت میده به ما
from scipy.spatial.distance import cityblock
p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)

#زاویه کسینوس بین دو نقطه را میدهد
from scipy.spatial.distance import cosine
p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)

#نسبت بیت هایی است که در آن دو بیت متفاوت است
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)

#سایپای قابلیت ماندگاری  و همکاری با متلب را نیز برای ما فراهم میکند
#نحوه ی وارد کردن اطلاعات با فرمت متلب
#savemat(filename-mdict-do_commpression)
#روش پایین یک فایل با این نام میسازه
from scipy import io
import numpy as np
arr=np.arange(10)
io.savemat("arr.mat",{"vec":arr})

#وارد کردن دیتا از فرمت متلب
#loadmat(filename)
from scipy import io
import numpy as np
arr=np.array([1,2,3,4,4,5,6,7,7,8,8,3])
io.savemat("arr.mat",{"vec":arr})
mydata=io.loadmat("arr.mat")
print(mydata)
#روش زیر فقط برای نمایش داده مورد نظر
print(mydata["vec"])
#در شرایط بالا ارایه ما یک بعدی است اما بعد از پرینت دو بعدی میشود برای حل این موضوع کار زیر را انجام میدهیم
mydata=io.loadmat("arr.mat",squeeze_me=True)
print(mydata["vec"])

#interpolation
#در یادگیری ماشین بکار میاد داده های گمشده را درون یابی میکند و نقاط گم شده را میدهد
#scipy.interpolation
#یک بعدی=interp1d(x,y)
from scipy.interpolate import interp1d
import numpy as np
xs=np.arange(10)
ys=2*xs+1
inter_func=interp1d(xs,ys)
newarr=inter_func(np.arange(2.1,3.0,1))
print(newarr)

#در درون یابی 1 بعدی نقاط برای یک منحنی منفرد پردازش میشوند،در حالی که در درون یابی اسپلاین نقاط در برابر یک یک تابع تکه ای تعریف شده با چند جمله ای به نام اسچلاین پردازش میشوند
#univariatespline(xs,ys)
from scipy.interpolate import UnivariateSpline
import numpy as np

xs=np.arange(10)
ys=xs**2 +np.sin(xs) +1
inter_func1=UnivariateSpline(xs,ys)
newarr1=inter_func1(np.arange(2.1,3,0.1))
print(newarr1)


#تابع پایه شعاعی تابعی است که مطابق با یک نقطه مرجع ثابت تعریف شده است
from scipy.interpolate import Rbf
import numpy as np
xs=np.arange(10)
ys=xs**2 + np.sin(xs)+1
interp_func=Rbf(xs,ys)
newarr2=interp_func(np.arange(2.1,0,0.1))
print(newarr2)

#statistical significant test
#یعنی جواب حاصله یک دلیلی پشتش داره و رندم انتخاب نشده
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

#اگر خواستیم فقط پی ولیو را برگردانیم صدا میزنیم
res = ttest_ind(v1, v2).pvalue
print(res)

#Null Hypothesis
#فرض بر این است که مشاهده از نظر آماری معنادار نیست

#Alternate Hypothesis
#فرض بر این است که مشاهدات بنا به دلایلی است و جایگزین فرضیه صفر است

#One tailed test
#هنگامی که فرضیه ما فقط برای یک طرف رزش آزمایش میشود ،به آن تست یک دنباله میگویند
"the mean is equal to k", "we can have alternate hypothesis:"
"the mean is less than k", "or"
"the mean is greater than k"

#Two tailed test
#زمانی که فرضیه ما برای هر دو طرف ارزش آزمایش میشود
"""
 "the mean is equal to k", we can have alternate hypothesis:
"the mean is not equal to k"
In this case the mean is less than, or greater than k, and both sides are to be checked   
"""

#kstest
import numpy as np
from scipy.stats import kstest
v=np.random.normal(size=100)
res=kstest(v,"norm")
print(res)

#برای دیدن خلاصه ای از یک آرایه
import numpy as np
from scipy.stats import describe
v=np.random.normal(size=100)
res=describe(v)
print(res)


import numpy as np
#from "scipy.stats" import skew, kurtosis

v = np.random.normal(size=100)

# print(skew(v))
# print(kurtosis(v))

#-----------------------------------------------------------------------------------------------------
#SQL
#زبانی برای ذخیره  و دستکاری اطلاعات دیتابیس هست
#ورودی ها و کلمات کلیدی sqlکیس سنستیو نیستند
#بعضی از اطلاعات سمی کالن میگیرند
#با زدن سمی کالن باعث میشه که توضیحات در اس کیو ال  از هم جدا بشند و بتونیم اطلاعات بیشتری رو وارد کنیم
#مهم ترین دستورات 
"""
select=استخراج داده از دیتا بیس
update=بروزرسانی داده ها در دیتابیس
delete=حذف داده ها از دیتا بیس
insert into=وارد کردن داده جدید در دیتا بیس
create database= ساهتن دیتا بیس جدید
alter database=اصلاح یک پایگاه داده
creat table=ساختن تیبل جدید
alter table=اصلاح تیبل ها
drop table=حذف تیبل ها
create index=ساخت ایندکس جدید
drop index=حذف ایندکس

"""
#از سلکت برای انتخاب داده از دیتا بیس استفاده میکنیم
#select customername, city from customer;
#select column1, column2,....
#from table_name;

"""
برای انتخاب تمام ستون ها به صورت زیر عمل میکنیم
select * from customers;

کد زیر فقط داده هایی که باهم متفاوت هستند را صدا میزنه
Select Distinct country From customers;

با کد زیر میتونیم تعداد داده های مختلف را بشمریم
select count(distinct country) from customers;

where
زمانی که از ور استفاده میکنیم در اصل داریم یک فیلتر گزاری میکنیم و میگیم جایی که مشخص کردم اطلاعاتی که مشخص کردم رو برگردون
select * from customors
where country="mexico";
or/
select column1mcolumn2,....
from table_name
where condition;

صدا زدن با ایدی
select * from customers
where customer id=1;

where not city="berlin"
And postalcar=123112

where not city="berlin"
or city="london"

#ترتیب گرفتن با order
"""
# select * from products
# order by price;

# select column1,column2,.....
# from table_name
# order by coulmn 1, column2 , ...... ASC|DESC


# #مرتب کردن دیسندیگ یا اسندینگ
# select * from products
# order by price DESC

# اگر خواستیم بر اساس حروف الفبا مرتب کنیم به صورت زیر انجام میدیم
# select * from product
# order by productname;

# #select * from proucts
# order by productname DESC;

# ترتیب بندی بر اساس چیزی که بهش میدی 
# select * from customers
# order by country,customername;

# اسندینگ دادن و دیسندیگن دادن همزمان
# select * from customers
# order by country ASC, customername DESC;
"""











#-----------------------------------------------------------------------------------------------------
#django
#جنگو یک فریم ورک سمت وب هست که به ما کمک میکند تا برای انجام یک پروژه نیازی به زدن کد های تکراری نداشته باشیم و  همچنین مزیت هایی ازجمله امنیت بالا و سرعت بالا نیز دارد
#کمک میکند تا با استفاده از پایتون بتوانیم سایت بهینه تری را بالا بیاریم
#mvt=model/view/template

model=
مدل دیتا را از دیتا بیس میگیره،بهترین راه برای گرفتن دیتا اس کیو ال هست

view=
درخواست از سایت رو میگیره مدل مرتبط رو وارد میکنه و نتیجه میگیره که چه داده ای روو ارسال کنه و نتیجه نهایی رو میده
در فایل زیر ذخیره میشه
views.py

template=
فایلی که شما تعریف میکنی که چطوری باید نتیجه ها پرزنت بشن.


url=
کمک میکنه تا در صفحات مختلف وب بگردیم در فایل زیر دخیره میشه
urls.py

#کاری که میکنه اینه که سایت یا اپ رو ساختی وصل میکنی به فایل ویو نوع و مدل رو میبینه اطلاعات مرتبط رو ارسال میکنه و بعد وصل میشه به یوارال وکد را وارد میکنه

#مراحل ساخت
py -m venv myworld
myworld\Scripts\activate.bat
py -m pip install Django
django-admin startproject my_tennis_club
تو پوشه ما تنیس این کد رو میزنیم
py manage.py runserver
رو عدد کلیک کرده تا فعال شه

#app
#چیزهایی که در وب قرار میدیم و رابط ما با کاربره مثل یک فرم و در نهایت وصل به دیتا بیس میشود.

مراحل ساخت app
py manage.py startapp members
کد بالا باید در پوشه ای که میخوای برنامه بسازی زده بشه
#فایل ویو
#http میگیره و جواب میده به صورت html
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    print(HttpResponse("hello world"))
# به روش بالا پیام را میفرستیم به وب
#قدم بعدی
#Create a file named urls.py in the same folder as the views.py file, and type this code in it:

"""
#where 
#میتونه شامل چند المان بشه با (و) و (مثل)
"""
select *
from customers
where country= "spain" and customername like "g%";


select column1, column2,.....
from table_name
where condition1 and condition2 and condition3.....;

select * cutomers 
where country= "germany"
and city= "berlin"
and postalcode > 123232;

#استفاده از یا برای وصل کردن ها
select * from customers
where country="spain" and *customer name like "g%" or customername like "r%");
#درصد هایی که زدیم یعنی با این کلمات شروع بشه

select *
from customers
where country="germany" or country="spain";
---------------------------
or
حداقل باید یکی از شرایطی که داریم درست باشه
select * from customers
where city ="berlin" or customername like "g%" or country="norway";
---------------------------
عملگر Not
نتیجه عکس میده به ما و منفی
select * from customers
where not country="spain";


select column1,column2,...
from table_name
where not condition;

select * from customers
where customername not like "a%",

اگر خواستیم رنجی بدیم به صورت زیر میدیم
select * from customers
where customerid not between 10 and 60;

select * from customers
where city not in ("paris", "london");

select * from customers
where not customerid>50;

select * from customers
where not customerid<50;

----------------
insert into 
با این متد میتونیم رکورد جدیدی به تیبل اضافه کنیم

insert into table_name(column1,column2,column3,....)
values(value1,value2,value3,.....)

اگر قراره چیزی که اضافه میکنیم به همه ردیف ها اضافه بشه لازم نیست مشخصش کنیم
insert into table_name
values(value1,value2,value3)

مثال:
insert into customers (customername, contactname, address, city, postalcode, country)
values("cardinal", "tomb.eriches","skagen 21 " , "stavanger" , 4005 , "norway");

insert into (customername, city, country)
values("cardinal","stabanger", "norway")

وارد کردن چند ردیف
insert into customer(customername,contactname,address,city,postalcode,country)
values
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');

-----------------------------------------
null value
یعنی فیلدی که خالیه

select column_names
from table_name
where column_name is null


select column_name
from table_name
where column_name is not null


select customername,contactname,address
from customers
where address is null;

select customername,contactlist, address
from customers
where address is not null
"""
"""
update
رکوردهای موجود در تیبل فعلی را تغییر میدهد
update table_name
set column1=value1,column2=value2,.....
where condition;

update customers
set contactname="alfred schmidt", city="frankfurt"
where customerid=1;



update multiple
update contactname="juan"
where country="mexico"

warning=
update cutomers
set contactname="juan";
اگر where را نزاریم اون تغییر برای همه ی المان ها اعمال میشن

-------------------------------------------------------------
sql delete statement
برای حذف یک المان در تیبل موجود
delete from table_name where condition;
delete from customers where customername="alfreds futterkiste";
delete tablename;
delete from customers;
drop table customers;

--------------------------------------------------------------
selects 
در اینجا یادمیگرییم چطوری چندتا ردیف رو صدا بزنیم
select top
ینی از بالا چند ردیف رو صدا بزنیم
select top * 3 from customers;

شرطی کردن
select top 3 * from customers
where country="germany";


ترکیب ترتیب بندی و شرطی کردن
select top 3 * from customers
order by customername desc;

--------------------------------------------------------------
min/max
min=کم ترین ولیو
max=بیشترین ولیو

select min (price)
from products;

select max(price)
from products;

select min(column_name)
from table_name
where condition;

select max(column_name)
from table_name
where condition;

برای اسم دادن به فیلد جدیدمون
select min(price) as smallestprice
from products;

-------------------------------------------------------------------
count
تعداد ردیف هایی را برمیگرداند که با یک ممعیار مشخص مطابقت دارند.
select count(*)
from products;

select count(cplumn_name)
from table_name
where condition;


ترکیب کردن where
select count(productid)
from products
where price>20;

اگر ستاره بدیم همه ی ردیف ها را شامل میشه حتی خالی ها رو اما اگر اسم بدیم ردیف های خالی را شامل نمیشه
select count(productname)
from products;


نادیده گرفتن تکراری ها
select count (distinc price)
from products;

select count(*) as [number of records]
form products;

-----------------------------------------------------
select sum (quantity)
from orderdetails;

select sum(column_name)
from table_name
where condition;


select sum(quantity)
from orderdetails
where productid=11;

select sum(quantity) as total
from orderdetails;


select sum(quantity * 10)
from orderdetails;

#اضافه کردن تیبل به یک تیبل دیگه برای جمع کردن دااده ها
select sum(price *quntity)
from orderdetails
left join products on orderdetails.productid=products.productid
----------------------------------------------------
average
پیدا کردن میانگین
select avg(price)
from products;

select avg(column_name)
from table_name
where condition;

select avg(price)
from products
where categoryid=1;

select avg(price) as [average price]
from produts;


select * from products
where price >(select avg(price) from products);

----------------------------------------------------
LIKE
در where قرار میگیره برای گشتن دنبال چیزی با پترنی مشخص
% = صفر یک یا چند کاراکتر میگیره
_ = یکی المان میگیره

select * from customers
where customername like "a%";

select column1
from table_name
where columnn like pattern;

select * from customers
where citu lik "l_nd__";


#شروع اسم مشتری که با ب باشه و با اس تموم بشه
select * from customers
where customername like "b%s";


select * from customers
where customername like "%or%";

#با بی شروع بشه و حداقل 3 کاراکتر طول داشته باشه
select * from customers 
where customername like "a__%";


select *from customers
where customername like "_r%";

#جایی که همه این حرف و داشته باشند
select * from customers
where customername like "%a%";
--------------------------------------------------------
wildcard charecter
یک کاراکتر عالم برای جایگزینی یک یا چند کاراکتر در یک رشته استفاده میشود
از where /like استفاده میشود

select * from customers
where customername like "a%";

charecters=
% = صفر یا هر مقدار کاراکتر 
_ = کاراکتر تکی
[] = هر کاراکتر تکی با براکت
^ =هر چیزی که داخل براکت نباشه رو ارایه میده
- = هرچیزی که تک کاراکتری باشه رو نمایش میده
{} = کاراکترهای جا افتاده را نشان میده

select * from customers
where customername like "% es";

select * from customers
where customername like "%mer%;

select * from customers
where city like "_ondon";

select * from customers
where city like "l__on";

هر چیزی که یکی از کاراکترای زیر رو داشته باشه رو بده
select * from customers
where customername like "[bsp]%";

هر چیزی که از ای تا اف را داشته باشه و باهاش شروع بشه
select * from customers
where cutomername like "[a-f]%";


select *from customers 
where customername like "a__%";

select * from customers
where customername like "_r%";

select * from customers
where country like "span";
-------------------------------------------------------------------
in
عملگری است که المان های مشخص در where مشخص میکند
in=کوتاه شده ی or هست

select * from customers
where country in ("germany","france","uk");

select column_name(s)
from table_name
where column_name in (value1,value2,......);

select * from customers
where country not in("germany","france","uk")

select * from customers
where customerid in (select customerid from orders)

select * from customers
where customerid not in (select customerid from order)
-------------------------------------------------------------------
between
همون رنج هست از فلان تا فلان

select * from product
where price between 10 and 40

select column_name(s)
from table_name
where column_name between value1 and value2

select * from products
where price not between 10 and 20;


select * from product
where price between 10 and 20
and categoryid in (1,2,3);

select * from products
where productname between "carnarvon tigers" and "mozzarella di giovanni"
order by productname;
-------------------------------------------------------------------
aliases
نام مستعار برای دادن نام نموقت به جدول یا ستونی در جدول استفاده میشود.
اغلب برای خوانایی بیشتر نام ستون ها استفاده میشود.
 نام مستعار فقط برای مدت زمان آن پرس و وجو وجود دارد
 
select customerid as id
from customers

select column_name as alias_name
from table_name;

select column_name
from table_name as alias_name;

select customerid as id , customernsame as customer
from customers;

اگر اسم موقت ما اسپیس زیاد داشت در براکت بزار
select productname as [my great products]
from products;

یا

select productname as "my great products"
from products;

select customername,address+","+postalcode+""+city+","+country as address
from customers;


select + from customers as persons;

select o.orderid, o.orderdate, c.customername
from customers as c, orders as o
where c.customername="around the horn" and c.customerid=o.customerid;
-------------------------------------------------------------------------------
join
این متد چند ردیف را از دو یا چند تیبل بهم وصل میکنه برطبق ردیف های بین آنها

select orders.orderid,customers.customername, orders.orderdate
from orders
inner join customers on orders.customerid=customers.customerid;


چهارنوع مختلف اضافه کردن داریم
inner join - left join - right join - full outer join 

inner join = مشترکات دو تیبل را برمیگردانه
left join = تمام سمت چپ به همراه مشترکات دوتا تیبل
right join = تمام سمت راست و مشترکات دو تا تیبل
full outer join = کل اولی با کل دومی به همراه مشترکات 



from orders
innere join customers
on orders.customerid=cutomers.customerid;

select column_name
from table
inner join table2
on table.column_name = table2.cplumn_name;


select products.productid, product.productname, categories.categoryname
from products
inner join categories on products.categoryid=categories.categoryid;

join = inner join
select products.productid, products.productname, categories.categoryname
from products 
join categories on products.categoruid=categories.categoryid;

برای چسباندن سه تیبل از order استفاده میکنیم
select orders.orderid,customers.customername,shippers.shippername
from((orders
inner join customers on orders.customerid=customer.customerid)
inner join shippers on orders.shipperid=shippers.shipperid);
    

"""
""" 
the left join
تمام سمت چپ و مشترکات دو تیبل
select column_name(s)
from table
left join table2
on table1.column_name=table2.column_name;



select customers.customername,orders.orderid
from customers
left join orders on customers.customerid=orders.customerid
order by cusmers.customername;

----------------------------------------------------------------

right join table
select column_name(s)
from table1
right join table2
on table1.column_name=table2.column_name;

select order.orderid,empliyees.lastname, employees.firstname
from orders
right join employees on orders.employeeid=employees.employeeid
order by orders.orderid;
-----------------------------------------------------------------
full outer join
select column_name(s)
from table1
full outer join table2
on table1.column_name=table2.column_name
where condition;

------------------------------------------------------------------
sql self join

تیبل با خودش همسو میشود
select column_name(s)
from table1 t1 , table1 t2
where condition;

select a.customername as customername1, b.customername as customernam2, a.city
from customers a , customers b
where a.customerid<> b.customerid
and a.cit = b.city
order by a.city;

---------------------------------------------------------------------
sql union operator

این عملگر برای ترکیب مجموعه نتیجه دو یا چند عبارت استفاده میشود.
تمام انتخاب شدده ها باید شامل ردیف های یکسان باشد
نوع داده باید یکسان باشد در هر دو مورد
ردیف های انتخاب شده باید نظم یکسانی داشته باشند

select column_name(s) from table1
union
select column_name(s) from table2;

برای اینکه مقادیر تکراری را انتخاب کنیم به صورت زیر عمل میکنیم
select column(names) from table1
union all
select column_name(s) from table2

select city from customers
union
select city from suppliers
order by city;

select city,country from customers
where country="germany"
union
select city,country from suppliers
where country="germany"
order by city;

---------------------------------------------------------------------
the sql group by statement

این عبارت ردیف هایی را که مقادیر یکسانی دارند در ردیف های خلاصه گروه بندی میکند، مانند تعداد مشتریان در هر کشور را بیابید
count(),max(),min(),sum(),avg()
select column_name(s)
from table_name
where condition
group by column_name
order by column_name;



select count (customerid),country
from customers
group by country;

select count(countryid),country
from customers
group by country
order by count(customerid)desc;

select shippers.shippername,count(orders.orderid) as numberoforders from orders
left join shippers on orders.shipperid=shippers.shipperid
group by shippername;



"""

"""
sql having clausE
WHEREاین متد اضافه شد چون از نمیشه برای جمع توابع استفاده کرد

select column_name(s)
from table_name
where condition
group by column_name(s)
having condition
order by column_name(s);


select cont(customerid),country
from customers
group by country
having count(customerid)>5;

select count(customerid),country
from customers
group by country
having count (customerid)>5
order by count (customerid) desc;

select emplyees.lastname , count (orders.orderid) as numberoforders
from (order
inner join employee on orders.emplyeeid=employees.employeeid)
group bt lastname
having count (orders.orderid)>10;


select employees.lastname , count (orders.orderid) as numberoforders
from orders
inner join employees on orders.employeeid=employees.employeeid
where lastname="davolio" or lastname= "fuller"
group by lastname
having count(orders.orderid)>25;

--------------------------------------------------------------------
sql exists operator

این عملگر برای تست موجود بودن یک داده استفاده میشود
اگر وجود داشته باشد ترو برمیگرداند

select column_name(s)
from table_name
where exists
(select column_name from table_name where condition);


select suppliername
from suppliers
where exists (select productname from products where products.supplierid=supplier.supplierid and price<20);


select suppliername
from suppliers
where exists (select prodictname from products where products.supplierid=supplieres.supplierid and price>22);


--------------------------------------------------------------------
ANY/ALL
اجازه میده تا المان یک ستون را با رنجی از المان های دیگه مقایسه کنیم
جواب ترو و فالس هست
select column_name(s)
from table_name
where column-name operator any
(select column_name
from table_name
where condition);

select column_name(s)
from table_name
where column_name operator all
(select cplumn_name
from table_name
where condition);

select productname
from products
where productid=any
(select producctid
from orderdetails
where quantity=10);


select productname
from products
where productid=any
(select productid
from orderdetails
where quantity >99);


select productname
from product
where productid=any
(select productid
from orderdetails
where quantity>1000);

select all productname
from products
where true;

select productname
from products
where productid=all(
    select productid
    from orderdetails
    where quantity=10
);
--------------------------------------------------------------------
sql select into
اطلاعات درون یک تیبل را در یک تیبل دیگه کپی میکنه
select *
into newtable [IN externaldb]
from oldtable
where condition;

select * into customersbackup2017
from customers;

select * into customerbackup2017
from customer

select * into customerbackup2017 in "backup.mdb"
from customers;

select cusotmername,contactname into customersbackup2017
from customers;

select *  into customersgermany
from customers
where country="germany";

select customers.customername,orders.orderid
into customersorderbackup2017
from customers
left join odrders on customerid=orders.customerid;

#select into=همچنین میتواند یک تیبل جدید بسازد که خالی است فقط از (ور) استفاده کنید تاداده ای را برنگرداند
select * into newtable
from oldtable
where 1=0;
--------------------------------------------------------------------
insert into select
دااده های یک تیبل را در یک تیبل دیگر قرار میدهد و لازم است که داده های هدف مچ باشد


insert into table2
select * from table1
where condition;

insert into(c1,c2,c3,c4,....)
select c1,c2,c3,....
from table1
where condition;

insert into customers (customername,city,country)
select suppliername, ccity, country from suppliers;

insert into customers (customername,contactname,address,city,postalcode,country)
select suppliername,contactname,address,city,postalcode,country from suppliers;

insert into cusotmers(customername,city,country)
select suppliername,city,country from suppliers
where country ="germany"


--------------------------------------------------------------------
sql case expression
مانند تابع های شرطی در پایتون میباشد و اگر شرط اول اجرا شود تمام میشود و ترو میدهد
case
when conditon1 thern result1
when condition2 then result2
when conditionn then result n
else reslut
end;

select orderid,quantiy,
case
when quantity > 30 then "the quantity is greate than 30"
when quantity > 30 then "the quantity is 30"
else "the quantity is under 30"
end as quantitytext
from orderdetails;

select customername,city,country
from customes
order by 
(case
when city is null then country
else city
end);

--------------------------------------------------------------------
is null
اگر در انجام عملیاتی در یک تیبل مثل ضرب دو ردیف در یکدیگر اگر یکی از آنها خالی باشد 
تمام جواب صفر و خالی خواهد بود برای جلوگیری از این کار زیر را انجام میدهیم
select prodcutname,unitprice*(unitinstock + ifnull(unitsonorder,0))
from products;

select productname,unitprice *(unitinstock + coalesce(unitsonorder,0))
from products;


select productname,unitprice *(unitinstocj + isnull (unitsonorder,0))
from products;

select productname,unitorice * (unitinstock + coalesce(unitsonorder,0))
from products;
--------------------------------------------------------------------
stored procedure
اگر یک کد را بارها و بارها میزنیم و تکرار میکنیم برای جلوگیری از تکرار این عمل
ان را ذخیره میکنیم و در صورت نیاز فقط آن را صدا میزنیم


ساختن
create procedure procedure_name
as
sql_statemenet
go;

صدا زدن
exec procedure_name;

create procedure selectallcustomers
as 
select * from customers
go;

exec selectallcustomers;

یک پارامتر را صدا زدن
create procedure selectallcustomers @city nvarchar(30)
as 
select * from cusotmers where city = @ city
go;

exec selectallcustomers @city = "london";
--------------------------------------------------------------------
برای کامنت نویسی از راه های مختلف میشه این کار را کرد اکر تک خط بود به صورت زیر:

--SELECT * FROM Customers;
SELECT * FROM Products;

SELECT * FROM Customers -- WHERE City='Berlin';


اگر چند خط بود به صورت زیر:
/*Select all the columns
of all the records
in the Customers table:*/
SELECT * FROM Customers;


select * from customers where (customername like "l%:
or customername like "r%" /* or customernam like "sJ%"
or customername like "t%"*/ or customername like "w%")
and country="usa"
order by customername;
--------------------------------------------------------------------
عملگر های sql
+	Add	
-	Subtract	
*	Multiply	
/	Divide	
%	Modulo
&	AND
|	OR
^	exclusive OR
=	Equal to	
>	Greater than	
<	Less than	
>=	Greater than or equal to	
<=	Less than or equal to	
<>	Not equal to
+=	Add equals
-=	Subtract equals
*=	Multiply equals
/=	Divide equals
%=	Modulo equals
&=	Bitwise AND equals
^-=	Bitwise exclusive equals
|*=	Bitwise OR equals
ALL	         TRUE if all of the subquery values meet the condition	
AND	         TRUE if all the conditions separated by AND is TRUE	
ANY	         TRUE if any of the subquery values meet the condition	
BETWEEN	     TRUE if the operand is within the range of comparisons	
EXISTS	     TRUE if the subquery returns one or more records	
IN	         TRUE if the operand is equal to one of a list of expressions	
LIKE	     TRUE if the operand matches a pattern	
NOT	         displays a record if the condition(s) is NOT TRUE	
OR	         TRUE if any of the conditions separated by OR is TRUE	
SOME	     TRUE if any of the subquery values meet the condition
--------------------------------------------------------------------
"""
"""
روش ساختن db
create database testdb;


روش حذف دیتابیس
drop database testdb

بک آپ گرفتن دیتا بیس
backup database testdb
to disk="filepath";


این روش بک آپ گرفتن برای زمانی است که شما داده هایی که نسبت به اخرین دفعه تغییر داده اید
سیو میشوند
backup database testdb
to disk="filepath"
with differential;



روش ساخت تیبل
create table table_name(
    personid int,
    lastname varchar(25),
    firstname varchar(255),
    address varchar(255),
    city varchar(225)
);

اگر خواستیم تیبلی بسازیم که المان هایی از یک تیبل موجود داشته باشد به صورت زیر عمل میکنیم
create table new_table_name as 
select column1, column2,....
from exisiting_table_name
where......;


create table testtable as
select customername,contactname
from customers;


حذف تیبل به صورت زیر است
drop table shippers;

حذف اطلاعات درون یک تیبل نه خود تیبل
truncate table shippers;


روش زیر به ما کمک میکند تا اطلاعات درون یک تیبل را حذف/اضافه/تغییر/و کارهای دیگه روی تیبل انجام دهیم
alter table customers
add email varchar(234);

alter table customers
drop cplumn email;

alter table table_name
rename column oldnam to newname


alter table table_name
alter column_name datatype;


alter table table_name
modify column_name datatype;

alter table persons
add dateofbirth date;

برای تغییر نوع داده یا همان دیتا تایپ کار زیر را انجام میدهیم
alter table persons
alter column dateofbirth year;

alter table persons
drop column dateofbirth;

alter table persons
drop column dateofbirth;

ایجاد محدودیت یا فیلتر با کد زیر
create table table_name(
    column1 datatype constraint,
    column2 datatype constraint,
    column datatype  constraint,
)

محدودیت ها برای محدود کردن نوع داده هایی که میتوانند در جدول قرار گیرند استفاده میشوند
این امر صحت و قابلیت اطمینان داده های جدول را تضمین میکند. اگر هر گونه نقضی بین محدودیت و عمل داده وجود داشته باشد اقدام لغو میشود.
محدودیت ها میتوانند سطح ستون یا سطح جدول باشند. محدودیت های سطح ستون برا ییک ستون اعمال میشود و محدودیت های سطح جدول برای کل جدول اعمال میشود.

دستورات محدودیت ها برای sql

not null=مطمین باش که یک ستون نمیتوان خالی باشد
unique=مطمین باش که تمام داده ها تکراری نباشد
primary key=ترکیب دو تای بالایی
foreign key=جلوگیری از کاری که بتواند ارتباط بین دو تیبل را از بین ببرد
check=مطمین باشید که یک داده تمام شروط لازم را داشته باشد
default=یک شرط پیش فرض قرار دهید برای داده هایی که شرطی ندارند
create index=برای ایجاد و بازیابی سریع داده ها از پایگاه داده استفاده میشود



شرط خالی نبودن
به صورت پیش فرض نمیتواند خالی باشد اما این کار تاکید میکند
create table persons(
    id int not null,
    lastname varchar(224) not null,
    firstname varchar(222)not null,
    age int
);

alter table persons
alter column age int not null;


شرط یک و تک بودن
create table persons(
    id int not null unique,
    lastname varchar(222)not null,
    firstname varchar(222),
    age int
);

alter table persons
add unique(id);


حذف فیلتر یکی بودن
alter table persons
drop index uc_persons;

primary key فیلتر
این فیلتر کمک میکند تا هر المان را در تیبل بشناسیم و شناسایی کنیم
اینها باید داده های تکی باشند و شامل داده های خالی نباشند
هر تیبل ففقط یکی میتواند داشته باشد
create table persons(
    id int not null,
    lastname varchar (333) not null,
    firstname varchar(234),
    age int,
    primary key(id)
);

alter table persons
add primary key (id);

حذف آن
alter table persons
drop primary key;

-----------------------------------------
sql foreign key constraint
foreign key=جلوگیری از کاری که بتواند ارتباط بین دو تیبل را از بین ببرد

create table odrders(
    orderid int not null,
    ordernumber int not null,
    personid int,
    primary key (orderid),
    foreign key (personid) refrences persons (personid)
);

alter table orders
add foreign key(personid) refrences persons (personid);

برای نام گذاری یک فارن کی به صورت زیر عمل میکنیم
alter table orders
add constraint fk_personorder
foreign key(personid) refrences persons(personid);

حذف یک فیلتر فارن کی 
alter table orders 
drop foreign key fk_personorder;

------------------------------------------------------------------
check= چک کردن برای اینکه ببینیم آیا یک المان تمام شرایط لازم را دارد یا نه
اگر یک محدودیت چک را روی یک ستون تعریف کنید فقط مقادیر خاصی را برای این ستون مجاز میکند
اگر یک محدودیت چک را روی یک جدول تعریف کنید میت واند مقادیر ستون های خاص را بر اسا مقادیر ستون های دیگر د ردیف محدود کند.

create table persons(
    id int not null,
    lastname varchar(222) not null,
    firstname varchar (333),
    age int check (age>=18)
);

برای اجازه دادن به نامگذاری یک محدودیت و برای تعریف یک محدودیت در چندین ستون از دستور زیر استفاده میکنیم
create table persons(
    id int not null,
    lastname varchar (222) not null,
    firstname varchar (333),
    age int,
    city varchar(333)
    consraint chk_person check (age>=18 and city="sandnes")
)

alter table persons
add check (age>=19);

حذف فیلتر چک
alter table persons 
drop constraint chk_personage;
---------------------------------------------------------------
sql default constraint
یک ارزش پیش فرض به ستون ها میده
اگر ان ارزش را نداشته باشند به کل ان ستون ها میدهد
create table persons(
    id int not null,
    lastname varchar(333) not null,
    firstname varchar(333),
    age int,
    city varchar (222) default "sandnes"
);

alter table persons 
add constraint df_city
default "sandnes" for city;

حذف
alter table persons
alter column city frop default;
-----------------------------------------------------------------------
sql create index statement
برای ایجاد نمایه ها در حداول استفاده میشود
ایندکس ها برای بازیابی داده ها از پایگاه داده سریعتر از موارد دیگر استفاده میشوند.کربران نمیتواند ایندکس ها را ببینند. آنها فقط برای سرعت بخشیدن به جستجو ها و پرس و جوها استفاده میشوند
زمان اپدیت این تیبل هایی که ایندکس دارند بیشتر از آنهاست که ندارند 

ساخت ایندکس ها
create index index_name
on table_name (column1,column2,.....);

ساخت ایندکس های تک و واحد
create unique index index_name
on table_name (column1,column2,.....);


create index idx_lastname
on persons (lastname);

create index idx_pname
on persons(lastname,firstname);

حذف ایندکس ها
drop index index_name.index_name;

---------------------------------------------------------------------
sql auto increment field
افزایش خودکار اجازه میدهد تا زمانی که یک رکورد جدید در جدول درج میشود. یک عدد منحصر به فرد به طور خودکار تولید شود.
اغلب این فیلد کلید اصلی است که میلیم هر بار که یک رکورد جدید درج میشود به طور خودکار ایجاد شود


create table persons(
    personid int identity (1,1) primary key,
    lastname varchar(333) not null,
    firstname varchar(333),
    age int
);

insert into persons(firstname,lastname)
values("lars","monsen");

--------------------------------------------------------------------
sql working with dates
کار با تاریخ ها

date             => format YYYY-MM-DD
datetime         => format: YYYY-MM-DD HH:MI:SS
smalldatetime    => format: YYYY-MM-DD HH:MI:SS
year             => format YYYY or YY


مثال کار با تاریخ ها
select * from orders where orderdate="2008_11_11"

------------------------------------------------------------------------
sql create view statement
ویو یک جدول محازی است که بر اساس مجموعه نتایج یک دستور در اس کیو ال است.
یک نما درست مانند یک جدول واقعی شامل سطر ها و ستون هاست فیلدهای یک ویو فیلد هایی از یک یا
چند جدول واقعی در پایگاه داده هستند.
میتوانید عبارات و توابع اس کیو ال را به یک ویو اضافه کنید و داده ه را طوری ارایه دهید که گویی داده ها از یک جدول منفرد میایند

create view view_name as
select column1,column2,......
from table_name
where condition;


create view [brazil customers] as
select customername, contactname
from customers
where country="brazil";

select * from [brazil customers]


create view [products above aberage price] as
select productname,price
from products
where price >(select avg(price) from products);

select * from [products above average price];

----------------------------------------------------------ئخد
updaint a view
create or replace view view_name as
select column1,column2,......
from table_name
where condition;

example
create or replace view[brazil customers]as
select customername,contactname,city
from customers
where country="brazil";

---------------------------------------------------------
sql dropping a view

drop view view_name;

drop view[brazil customers];

----------------------------------------------------------
"""
"""
SQL KEYWORDS

ADD	                 =>  Adds a column in an existing table
ADD                  =>  CONSTRAINT	Adds a constraint after a table is already created
ALL        	         =>  Returns true if all of the subquery values meet the condition
ALTER                =>	 Adds, deletes, or modifies columns in a table, or changes the data type of a column in a table
ALTER COLUMN         =>  Changes the data type of a column in a table
ALTER TABLE          =>  Adds, deletes, or modifies columns in a table
AND	                 =>  Only includes rows where both conditions is true
ANY	                 =>  Returns true if any of the subquery values meet the condition
AS	                 =>  Renames a column or table with an alias
ASC	                 =>  Sorts the result set in ascending order
BACKUP DATABASE      =>	 Creates a back up of an existing database
BETWEEN	             =>  Selects values within a given range
CASE	             =>  Creates different outputs based on conditions
CHECK	             =>  A constraint that limits the value that can be placed in a column
COLUMN	             =>  Changes the data type of a column or deletes a column in a table
CONSTRAINT           =>	 Adds or deletes a constraint
CREATE	             =>  Creates a database, index, view, table, or procedure
CREATE DATABASE      =>	 Creates a new SQL database
CREATE INDEX         =>	 Creates an index on a table (allows duplicate values)
CREATE OR REPLACE    =>  VIEW	Updates a view
CREATE TABLE         =>	 Creates a new table in the database
CREATE PROCEDURE	 =>  Creates a stored procedure
CREATE UNIQUE        =>  INDEX	Creates a unique index on a table (no duplicate values)
CREATE VIEW          =>	 Creates a view based on the result set of a SELECT statement
DATABASE	         =>  Creates or deletes an SQL database
DEFAULT              =>	 A constraint that provides a default value for a column
DELETE               =>	 Deletes rows from a table
DESC                 =>	 Sorts the result set in descending order
DISTINCT             =>	 Selects only distinct (different) values
DROP                 =>	 Deletes a column, constraint, database, index, table, or view
DROP COLUMN        	 =>  Deletes a column in a table
DROP CONSTRAINT      =>	 Deletes a UNIQUE, PRIMARY KEY, FOREIGN KEY, or CHECK constraint
DROP DATABASE        =>	 Deletes an existing SQL database
DROP DEFAULT         =>	 Deletes a DEFAULT constraint
DROP INDEX	         =>  Deletes an index in a table
DROP TABLE   	     =>  Deletes an existing table in the database
DROP VIEW	         =>  Deletes a view
EXEC                 =>	 Executes a stored procedure
EXISTS	             =>  Tests for the existence of any record in a subquery
FOREIGN KEY          =>  A constraint that is a key used to link two tables together
FROM                 =>	 Specifies which table to select or delete data from
FULL OUTER JOIN      =>	 Returns all rows when there is a match in either left table or right table
GROUP BY             =>	 Groups the result set (used with aggregate functions: COUNT, MAX, MIN, SUM, AVG)
HAVING	             =>  Used instead of WHERE with aggregate functions
IN	                 =>  Allows you to specify multiple values in a WHERE clause
INDEX                =>	 Creates or deletes an index in a table
INNER JOIN           =>	 Returns rows that have matching values in both tables
INSERT INTO          =>  Inserts new rows in a table
INSERT INTO SELECT   =>	 Copies data from one table into another table
IS NULL              =>	 Tests for empty values
IS NOT NULL          =>	 Tests for non-empty values
JOIN	             =>  Joins tables
LEFT JOIN            =>	 Returns all rows from the left table, and the matching rows from the right table
LIKE	             =>  Searches for a specified pattern in a column
LIMIT	             =>  Specifies the number of records to return in the result set
NOT	Only             =>  includes rows where a condition is not true
NOT NULL             =>	 A constraint that enforces a column to not accept NULL values
OR	                 =>  Includes rows where either condition is true
ORDER BY             =>	 Sorts the result set in ascending or descending order
OUTER JOIN           =>	 Returns all rows when there is a match in either left table or right table
PRIMARY KEY	         =>  A constraint that uniquely identifies each record in a database table
PROCEDURE	         =>  A stored procedure
RIGHT JOIN	         =>  Returns all rows from the right table, and the matching rows from the left table
ROWNUM	             =>  Specifies the number of records to return in the result set
SELECT               =>	 Selects data from a database
SELECT DISTINCT      =>	 Selects only distinct (different) values
SELECT INTO          =>	 Copies data from one table into a new table
SELECT TOPv	         =>  Specifies the number of records to return in the result set
SET	Specifies        =>  which columns and values that should be updated in a table
TABLE	             =>  Creates a table, or adds, deletes, or modifies columns in a table, or deletes a table or data inside a table
TOP                  =>  Specifies the number of records to return in the result set
TRUNCATE TABLE       =>	 Deletes the data inside a table, but not the table itself
UNION	             =>  Combines the result set of two or more SELECT statements (only distinct values)
UNION ALL            =>	 Combines the result set of two or more SELECT statements (allows duplicate values)
UNIQUE	             =>  A constraint that ensures that all values in a column are unique
UPDATE               =>  Updates existing rows in a table
VALUES	             =>  Specifies the values of an INSERT INTO statement
VIEW	             =>  Creates, updates, or deletes a view
WHERE	             =>  Filters a result set to include only records that fulfill a specified condition
"""
#-----------------------------------------------------------------------------------
#builtin functions
"""
abs(x)  #Returns the absolute value of a number x
aiter(i)  #Asynchronous iterator, return an asynchronous iterator
all(i)  #Returns True if all elements in an iterable i are true
any(i)  #Returns True if at least one element in an iterable i is true
anext(ai)  #Retrieve the next item from an asynchronous iteratorai.
ascii(o)  #Returns a string containing a printable representation of an object o
bin(x) #Converts an integer x to a binary string
bool(x)  #Converts a value x into a Boolean
breakpoint()  #Drops the runtime into a python debugging session
bytearray(*args, **kwargs)  #Returns a bytearray object
bytes(*args, **kwargs)  #Returns a bytes object
callable(o)  #Returns True if the object o is callable, False otherwise
chr(c) #Returns a string representing a character c whose Unicode code point is the integer
classmethod(fn)  #Returns a class method for a function fn
compile(s, *args, **kwargs)  #Returns a code object from source s (string, file, etc.)
complex(r, i)  #Returns a complex number where r is real and i is imaginary
delattr(o, n) #Deletes an attribute of name n from an object o
dict()  #Returns a new dictionary
dir(o)  #Returns a list of names in the namespace of object o
divmod(a, b)  #Takes two numbers a and b and returns a pair of numbers (a tuple) consisting of their quotient and remainder
enumerate(o[, s])  #Returns an enumerate object, which can be used to iterate over an iterable o and get the index of each element. Optional start value starts the enumeration at value s
eval(s, *args) #Evaluates a string s as a Python expression
exec(s, *args, **kwargs) #Used for the dynamic execution of source s which is a valid Python programs
filter(fn, i)  #Returns an iterator from elements of an iterable i for which a function fn returns True. Uses lazy evaluation.
float(x) #Converts a value x to a float
format(o)  #Returns a formatted string version of an object o
frozenset()  #Returns an immutable frozenset object
getattr(o, n[, d]) #Returns the value of a named attribute n from object o. Optional default d is returned if attribute does not exist.
globals()  #Returns the current global symbol table as a dictionary
hasattr(o, n) - #Returns True if the object o has the given named attribute n, False otherwise
hash(o) # Returns the hash value of an object o
help(o)  #Invokes the built-in help system for object o
hex(i)  #Converts an integer i to a hexadecimal string
id(o)  #Returns the identity of an object o
input(p)  #Reads a line from input, after printing the optional prompt p
int(x)  #Converts a value x to an integer
isinstance(o, t)  #Returns True if the object o is an instance of the specified type t, False otherwise. If t is tuple or union, checks against all types in t.
issubclass(c, s) #Returns True if a class c is a subclass of a specified superclass s, False otherwise
iter(o)  #Returns an iterator of object o
len(o)  #Returns the length of an object o
list() #Returns a new list
locals()  #Returns an updated dictionary of the current namespace
map(fn, i)  #Returns an iterator which applies a function fn to all items in an iterable i. Uses lazy evaluation.
max(*args[, key=fn])  #Returns the largest item of two or more arguments, optional key is a function fn to apply to each item
memoryview(o)  #Returns a memory view object of the given objecto
min(*args[, key=fn]) #Returns the smallest item of two or more arguments, optional key is a function fn to apply to each item
next(i)  #Retrieves the next item from an iterator i
object()  #Returns a new featureless object
oct(i)  #Converts an integer i to an octal string
open(p, m, *args, **kwargs)  #Opens a file and returns a file object
ord(c) #Given a string representing one Unicode character c,returns an integer representing the Unicode code point of thatcharacter
pow(x, y)  #Returns the value of x to the power of y (x**y)
print(*args, **kwargs)  #Prints the specified messages args tothe screen
property(fg[, fs, fd, d])  #Gets, sets, or deletes a property ofan object
range(*args, **kwargs)  #Returns a sequence of numbers
repr(o) #Returns a string containing a printable representation ofan object o
reversed(s)  #Returns a reversed iterator of a sequence s
round(n, d)  #Rounds a number n to the nearest integer, or to thespecified number of decimals d.
set()  #Returns a new set object
setattr(o, n, v)  #Sets the value v of a named attribute n of an
object o
slice(*args, **kwargs) - #Returns a slice object
sorted(i[, key=fn, reversed=False]) #Returns a sorted list from the specified iterable i, optional key is a function fn to apply to each item, and is reversed if keword reversed is truthy.
staticmethod(fn) - #Returns a static method for a function fn
str() #Returns a string object
sum(i)  #Sums the items of an iterable i
super() #Returns a temporary object of the superclass
tuple()  #Returns a new tuple object
type(o) #Returns the type of an object o
vars(o)  #Returns the dict attribute of an object o
zip(*args[, strict=False])  #Returns an iterator of tuples
"""