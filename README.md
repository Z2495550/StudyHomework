测试实战（一）课后作业

1、补全计算器（加减乘除）的测试用例

2、使用数据驱动完成测试用例的自动生成

3、conftest.py中创建fixture 完成setup和teardown

4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】



测试实战（二）课后作业

课后作业1

1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例

课后作业2

控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
减法依赖加法， 除法依赖乘法

课后作业3

注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。

理解
测试数据的数据驱动
测试步骤的数据驱动
思考应用场景
