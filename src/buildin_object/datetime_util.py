# time
import time

# ################struct time############
# 为什么叫时间元祖，时间元祖的由来？
# # 起手式222222222222, 不要用该起手式，太难用了，请用datatime的起手式
# 下面的全部报错，，请用datatime的起手式
# print(time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5))
# print(time.struct_time((2011, 10, 1)))
# print(time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=14, tm_sec=50))
# print(time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=3, tm_yday=125, tm_isdst=0))

# 返回结构化时间 time.struct_time(tm_year=2020, tm_mon=7, tm_mday=13, tm_hour=13, tm_min=23, tm_sec=22, tm_wday=0, tm_yday=195, tm_isdst=0)
print(time.localtime())
# timestamp ==>> struct time
print(time.localtime(time.time()))

# 格林威治时间(就是UTC时间) 的 struct time
print(time.gmtime())    # 比当前北京时间倒退8小时，北京时间要大，要超前。时间时间拖后腿
# 将北京时间 =>> UTC时间
print(time.gmtime(time.time()))


# ##############timestamp################
print(time.time())  # 1594617750.025248， 返回的10位，以s为单位
# struct_time =>> timestamp
print(time.mktime(time.localtime()))


# ############Format time##############
# 常用的格式 %
# 起手式111111，自定义任何的时间元祖
# format_time格式化字符串时间 =>> struct_time时间元祖, 这个最重要是，
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
# struct_time =>> 格式化字符串时间
time.strftime("%Y-%m-%d %X", time.localtime())


# datetime
from datetime import datetime, date, time as dtime, timedelta, timezone
# 知道为啥不能用from 到了吧，！！！！！

# 问题：为什么有了time模块，还需要datetime模块?
# 答曰：最重要的时间加减
# ###### date类 datetime.date(year, month, day)

# ###### time类 datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] )

# ##### datetime 类 对象的创建
# 该方法是连接date对象和 time对象 的方法
d = date(year=2016, month=9, day=2)
t = dtime(hour=18, minute=14)
datetime.combine(date=d, time=t)    # 根据date和time，创建一个datetime对象；
# 起手式 1111111111
# datetime从字面意思上看是date和time的结合，而实际上也是包含了这两个对象的全部信息，我们可以手动构造datetime对象，也可以使用系统提供的静态方法，
# 当我们手动构造的时候，必须要传入year、month和day三个参数，他们的取值范围与上面讲到的date对象一致
# datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )
dt = datetime(year=2016, month=9, day=2)    # datetime.datetime(2016, 9, 2, 0, 0)
# datetime.today()：返回一个表示当前本地时间的datetime对象；
# datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
# datetime.utcnow()：返回一个当前utc时间的datetime对象；#格林威治时间


# 时间戳 => datetime对象，注意反过来没有，不能datetime到时间戳吗？可以通过timetuple()方法，它返回一个time.struct_time对象
# datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
# datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个 UTC的 datetime对象；
print(datetime.fromtimestamp(time.time()))

dd = datetime.today()
tt = time.mktime(dd.timetuple())    # datetime先转化为struct_time, 再用time模块的mktime方法，记住这个桥梁方法，不再用字符串了。


# 格式化字符串
# 起手式2222，自定义时间字符串
# datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')：将格式字符串转换为datetime对象；

# datetime.strftime(date_string, '%Y-%m-%d %H:%M:%S'): 将时间格式化转换为字符串格式
    # datetime对象也有strftime方法


# 常用的对象方法,注意是对象方法，模块方法
today = datetime.today()
today.date()
today.time()
next_month = today.replace(month=today.month + 1) # 注意 replace不会考虑跨年和日期超过月份最大值的情况



# ###### tzinfo时区类 ？？？

# ###### timedelta类，时间加减
# 使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。
# datetime.timedelta用来计算两个datetime.datetime或者datetime.date类型之间的时间差。
# def __new__(cls, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
dt = datetime.now()
# 日期减一天
dt1 = dt + timedelta(days=-1)   # 昨天， 既可以加-1，也可以减1
dt2 = dt - timedelta(days=1)    # 昨天
dt3 = dt + timedelta(days=1)    # 明天
#
delta_obj = dt3-dt      # 两个dt格式相减获得也是timedelta对象

# 注意，千万注意，timedelta会自动处理 进1， 但是最好还是用时间戳加减，万无一失
# replace不会处理 进一
print(datetime.now())
print(timedelta(hours=23))
print(datetime(2020, 12, 31, 23, 0, 0) + timedelta(hours=23))



# 时区 astimezone方法和datetime.timezone对象
print(datetime.today().astimezone(timezone(timedelta(hours=8))))
