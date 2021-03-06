
------

# 需求规格说明书

## 1. 引言

## 1.1 系统名称

服务出租系统

## 1.2 项目背景

一家公司提供服务出租，自身有一些员工，另外还有很多自由职业者作为服务商存在。公司目前使用Excel工作表来管理他们的客户（自由职业者），时间表等。Excel解决方案无法很好地进行扩展。它无法应对多用户使用的场景，也不提供安全和审计日志。因此他们决定构建一个新的基于Web的解决方案。

## 2. 系统需求

### 2.1 功能需求

1. 用户可以创建账户,默认成为客户,可以申请成为服务商
2. 服务商可以对服务商信息进行管理
3. 成为服务商的同时创建生成一个与账户绑定的时间表
4. 服务商可以修改与账户绑定的时间表
5. 客户可以对客户信息进行管理
6. 客户可以按照条件对项目进行查询
7. 客户可以查询服务商的空余时间段
8. 每日定时生成当日的审计表
9. 每日定时刷新全体时间表

### 2.2 数据需求

#### 2.2.1 输入

1. 账号: 账号名, 密码
2. 服务商信息: 名称, 性别, 身份证号码, 电话号码, 邮箱地址, 服务商类型
3. 客户信息: 名称, 性别, 身份证号码, 电话号码, 邮箱地址
4. 项目信息: 名称, 描述, 价格, 开始时间, 时长, 项目状态, 项目类型

#### 2.2.2 输出

1. 审计表: 项目识别码, 项目名称, 项目描述, 项目类型, 项目开始时间, 项目时长, 项目状态, 客户识别码, 客户名称

#### 2.2.3 存储

1. 账号信息: 账号名, 密码, 服务商识别码, 客户识别码, 账号状态
2. 服务商信息: 服务商识别码, 名称, 性别, 身份证号码, 电话号码, 邮箱地址, 服务商类型, 联系方式
3. 客户信息: 客户识别码, 名称, 性别, 身份证号码, 电话号码, 邮箱地址, 联系方式
4. 项目信息: 项目识别码, 名称, 描述, 价格, 开始时间, 时长, 项目状态, 项目类型
5. 时间表: 时间表识别码, 服务商识别码, 时间项
6. 审计记录: 记录识别码, 项目信息, 时间记录， 服务商识别码， 服务商名称， 客户识别码， 客户名称， 服务商联系方式， 客户联系方式

### 2.3 领域驱动设计

#### 2.3.1 基本架构

|层次|描述|
|:---:|:---:|
|User Interface|负责界面展示和用户接口|
|Application|负责定义业务内容但不包含业务逻辑|
|Domain|负责业务逻辑和领域模型的实现,确保业务逻辑不会泄露到其他层次中|
|Infrastructure|负责为其他三层提供技术支持,实现其他各层的技术需求|

#### 2.3.2 实体定义

1. 账户: Account, 负责账户管理有关业务的实体
2. 服务商: Provider， 负责服务商有关业务的实体
3. 客户: Customer， 负责客户有关业务的实体
4. 项目: Project， 负责项目管理有关的实体
5. 时间表: Schedule， 负责时间表管理有关的实体
6. 审计: Audit, 负责审计管理有关的实体

#### 2.3.3 领域模型

![DDDimg]

### 2.4 数据模型

#### 2.4.1 ER图

![ERimg]

#### 2.4.2 类图

![Classimg]

### 2.5 功能模型

#### 2.5.1 数据流图

![Flowimg]

#### 2.5.2 用例图

![UseCaseimg]

### 2.6 数据字典

#### 2.6.1 数据项

|编号|名称|描述|定义|
|:---:|:---:|:---:|:---:|
|1|账户名|用于唯一识别账户的一个字符串|1{字符}32|
|2|密码|用于验证某个账户名是否合法登陆的一个字符串|6{字符}15|
|3|状态|用于描述账户或项目所处状态的一个字符串|0{字符}255|
|4|服务商识别码|用于唯一识别某个服务商的一个字符串|1{字符}32|
|5|服务商名称|用于称呼某个服务商的一个字符串|1{字符}255|
|6|电话号码|用于通信联络的一个字符串|8{字符}32|
|7|邮箱地址|用于邮件联络的一个字符串|8{字符}32|
|8|开始时间|记录某个时间点的一个字符串|{字符}18|
|9|结束时间|记录某个时间点的一个字符串|{字符}18|
|10|项目识别码|用于唯一识别某个项目的一个字符串|1{字符}32|
|11|项目名称|用于称呼某个项目的一个字符串|1{字符}255|
|12|时长|用于记录活动时间长度的一个数字|数字|
|13|客户识别码|用于唯一识别某个客户的一个字符串|1{字符}32|
|14|审计识别码|用于唯一识别某个审计记录的一个字符串|1{字符}32|
|15|时间记录|用于记录某个时间点的一个字符串|{字符}18|
|16|价格|用于表示花费多少的一个浮点数|{浮点数}|
|17|时间表识别码|用于唯一识别某个时间表的一个字符串|1{字符}32|

#### 2.6.2 数据流

|编号|名称|定义|流向|
|:---:|:---:|:---:|:---:|
|1|账户名,密码|账户名+密码|从界面流向账户管理|
|2|账户数据|账户名+密码+状态+服务商识别码+客户识别码+电话号码+邮箱地址|从数据库流向账户管理,从账户管理流向数据库|
|3|服务商登入请求|账户名+状态+服务商识别码|从账户管理流向服务商管理|
|4|客户登入请求|账户名+状态+客户识别码|从账户管理流向客户管理|
|5|管理请求|识别码+状态+电话号码+邮箱地址|从服务商管理流向数据库,从数据库流向服务商管理,从客户管理流向数据库,从数据库流向客户管理|
|6|审计查询请求|客户识别码+项目识别码|从客户管理流向审计管理|
|7|审计数据|客户识别码+服务商识别码+审计识别码+时间记录|从审计管理流向数据库,从数据库流向审计管理|
|8|创建请求|服务商识别码+项目名称+时长+价格|从服务商管理流向项目管理|
|9|购买请求|客户识别码+项目识别码|从客户管理流向项目管理|
|10|项目购买记录|客户识别码+项目识别码+时间记录|从项目管理流向审计管理|
|11|查询要求|服务商识别码|从项目管理流向时间表管理|
|12|项目数据|服务商识别码+项目识别码+时长+价格+电话号码+邮箱地址|从项目管理流向数据库,从数据库流向项目管理|
|13|时间表数据|时间表识别码+时间记录+服务商识别码|从时间表管理流向数据库,从数据库流向时间表管理|
|14|注销请求|账户名+密码|从账户管理流向退出接口|

#### 2.6.3 数据存储

|编号|名称|定义|
|:---:|:---:|:---:|
|1|账户数据|账户名+密码+状态+客户识别码+服务商识别码|
|2|服务商数据|服务商识别码+服务商名称+电话号码+邮箱地址|
|3|项目数据|项目识别码+项目名称+价格+时长+状态|
|4|客户数据|客户识别码+客户名称+电话号码+邮箱地址|
|5|时间表数据|时间表识别码+开始时间+结束时间|
|6|审计数据|审计识别码+数据记录|

## 3. 隐性需求

### 3.1 性能需求

1. 能够同时支持上百名用户的请求
2. 请求响应时间不超过3秒

### 3.2 安全需求

1. 权限控制
2. 数据备份
3. 加密处理

### 3.3 环境需求

1. 客户端:
* 操作系统: Windows
* 浏览器: Microsoft Edge, Chrome, Firefox等主流浏览器

2. 服务器:
* 操作系统: Ubuntu
* 应用服务器: Apache
* web框架: Django
* 数据库系统: MySQL

## 4. 系统设计

### 4.1 总体设计

#### 4.1.1 系统流程图

![Sdesign]

#### 4.1.2 物理清单

1. 服务器一台
2. 打印机一台
3. 计算机一台
4. 数据库一个
5. 程序六个:
* 账户管理系统
* 客户管理系统
* 服务商管理系统
* 项目管理系统
* 审计管理系统
* 时间表管理系统

### 4.2 详细设计

#### 4.2.1 层次图

![HIPOimg]

------

# 项目安排表

## 1. 安排表

|任务名称|预计时长|预计开始时间|预计结束时间|矫正后时长|矫正后开始时间|矫正后结束时间|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|需求获取|5个工作日|2021/4/23|2021/4/27|5个工作日|2021/4/23|2021/4/27|
|需求分析|3个工作日|2021/4/28|2021/4/30|3个工作日|2021/4/28|2021/4/30|
|撰写需求规格说明书|2个工作日|2021/5/1|2021/5/2|2个工作日|2021/5/1|2021/5/2|
|需求验证|2个工作日|2021/5/3|2021/5/4|2个工作日|2021/5/3|2021/5/4|
|总体设计|5个工作日|2021/5/5|2021/5/9|4个工作日|2021/5/5|2021/5/8|
|详细设计|7个工作日|2021/5/10|2021/5/16|6个工作日|2021/5/9|2021/5/14|
|编码|15个工作日|2021/5/17|2021/5/31|12个工作日|2021/5/15|2021/5/26|
|单元测试|5个工作日|2021/6/1|2021/6/5|5个工作日|2021/5/27|2021/5/31|
|集成测试|3个工作日|2021/6/6|2021/6/8|3个工作日|2021/6/1|2021/6/3|
|系统测试|2个工作日|2021/6/9|2021/6/10|2个工作日|2021/6/4|2021/6/5|
|验收测试|2个工作日|2021/6/11|2021/6/12|2个工作日|2021/6/6|2021/6/7|

## 2. 矫正计算方法

1. 需求获取,需求分析,撰写需求规格说明书,需求验证,测试和验收等阶段的所需时间和原计划差异不大,按100%来计算
2. 设计和编码阶段可以套用已有设计模式和开发框架,故花费时间比原计划有所减少

[ClassLink]:https://edu.cnblogs.com/campus/gdgy/2021Softwarecodedevelopmenttechnology
[WorkRequirements]:https://edu.cnblogs.com/campus/gdgy/2021Softwarecodedevelopmenttechnology/homework/11968
[DDDimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210503165906022-666493790.png
[Classimg]:https://user-images.githubusercontent.com/51396619/117522572-cbb66800-afe6-11eb-87ce-a5122d7b8393.png
[ERimg]:https://user-images.githubusercontent.com/51396619/117522502-64001d00-afe6-11eb-8956-98021140ea77.png
[Flowimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210503234413566-1608778624.png
[UseCaseimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210503222923895-1487240816.png
[Sdesign]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210504012523181-1479600557.png
[HIPOimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210504014519155-1823823820.png
[Issuesimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210504105145473-661998412.png
[Backgroundimg]:https://img2020.cnblogs.com/blog/2319277/202105/2319277-20210504105239559-875935780.png
[GitLink]:https://github.com/Get-rid-of-WA/HelloWorld
