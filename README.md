# TIinfo

一款数据来源于AlienVault开源威胁情报的信息收集工具。

可收集目标域名相关的子域名、IP地址、敏感url地址、网站状态响应码等，同时支持单域名查询、多域名查询以及输出xlsx文件。

# 主要功能
1.收集目标域名的敏感信息例如api、后台登录地址、敏感文件等信息。

![1](https://github.com/Cx000/TIinfo/assets/54984768/6426d333-1528-4929-ba00-72349a4a9b3f)

2.收集目标域的子域名信息。

![2](https://github.com/Cx000/TIinfo/assets/54984768/2101f329-0ac7-4431-8426-6d28a4d69625)

3.收集目标域名的子域名和网站响应状态码。

![3](https://github.com/Cx000/TIinfo/assets/54984768/cfac5239-e0c2-46fc-88f9-a1ac248f2e6b)

4.其他功能

- 单域名/批量域名信息收集
- 自定义输出信息条数
- 文件保存
# 使用方法
1.单域名查询：

python3 TIinfo.py

![4](https://github.com/Cx000/TIinfo/assets/54984768/2b24bcb7-34bf-4b27-9521-0065560bc5a2)

输入想查询的domain信息

![5](https://github.com/Cx000/TIinfo/assets/54984768/4c4096c1-e6a5-45e0-a32b-6d70fc53d85b)

默认查询5000条数据，如果目标域名信息大于5000条将会提示是否继续查询，继续可能需要大量时间，根据使用者使用情况自行输入。

![6](https://github.com/Cx000/TIinfo/assets/54984768/b8b848a7-f275-443e-a979-74efb2fef4ee)

2.批量域名查询

将目标域名填写至domain.txt文件中。


![7](https://github.com/Cx000/TIinfo/assets/54984768/2e15772a-9c1a-499f-bb16-506f408e2ed8)

执行python3 TIinfo.py，脚本将会查询完资产信息之后输出到resource.xlsx文件中。

![8](https://github.com/Cx000/TIinfo/assets/54984768/9f62bd6e-d1c2-410c-85e0-eb78c4e6976a)
