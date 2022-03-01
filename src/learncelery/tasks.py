from learncelery.celery import app as celery_app


# 创建任务函数
@celery_app.task
def my_task1():
    print("任务函数(my_task1)正在执行....")


@celery_app.task
def my_task2():
    print("任务函数(my_task2)正在执行....")


@celery_app.task
def my_task3():
    print("任务函数(my_task3)正在执行....")

