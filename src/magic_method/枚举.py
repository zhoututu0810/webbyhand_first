from enum import Enum

t = (1, 2, 3)
print(t[1])

print(type(Enum))       # <class 'enum.EnumMeta'>

Month = Enum("Month", ("mon", "tus"))   # 返回的是一个类
print(type(Month))      # <class 'enum.EnumMeta'>  说明是类，因为是元类产生的
print(type(Month.mon))  # <enum 'Month'> 这个称谓标签   说明是个实例，实例的类是Month
print(Month.mon)    # Month.mon
print(Month.mon.name)   # mon 标签名
print(Month.mon.value == 1)  # 标签值  True
print(Month.__members__)    # OrderedDict([('mon', <Month.mon: 1>), ('tus', <Month.tus: 2>)])
print(Month.__members__.values())



abc = Enum("Month", ("mon", "tus"))
print(abc.mon)  # Month.mon
print(abc.mon.value)


print()
print('测试枚举类')
# 自定义类
class VIP(Enum):
    YELLOW = 1, 2
    GREEN = 2, 3
    BLACK = 3, 4
    RED = 4, 5

print(VIP.__members__.values())

print(type(VIP.YELLOW))     # <enum 'VIP'>
print(VIP.YELLOW)           # VIP.YELLOW
