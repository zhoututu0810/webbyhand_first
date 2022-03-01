from testcelery import add2, app
print(add2)         # <@task: testcelery.add2 of taskinmain at 0x103d74bd0>
print(add2.name)    # testcelery.add2

# 分析为啥函数名不一样咯！？
# 调用该方法会去搜索task
print(app.tasks)    # 'testcelery.add2': <@task: testcelery.add2 of taskinmain at 0x10f559b50>,


