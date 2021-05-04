# 团队/组织名
> Get rid of WA

# 项目名称
> HelloWorld

# 项目结构
> configs：在开发的时候，项目是部署在开发环境中的，所以项目中的一些配置文件，比如：数据库连接配置文件，都是用的开发环境的数据库连接配置，项目要部署上线的时候，我们需要把开发环境的数据库连接配置替换成生产环境的数据库连接配置，所以这个目录可以用来存生产环境的相关配置文件。
之所以将测试环境/开发环境/生产环境分开是因为开发过程中，需要对数据库中的一些数据进行测试或者修改，如果不和生产环境分开，会“污染”生产环境的数据。
> dbscripts：在开发过程中，每次开发过程中涉及到要执行一些脚本，比如：开发过程中，要新建一个表，建表语句就要保存在这个目录里面，待开发完毕上线的时候，就需要在生产环境中执行这个建表语句。
> docs：这里存放项目的相关文档，比如：需求说明书，会议纪要，上线手册等。
> src：这里存放项目源码。
