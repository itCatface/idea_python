# -sql alchemy[ORM将关系数据库的表结构映射到对象上]
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义User对象[一个表一个对象]
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化mysql数据库连接['数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名']
# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/mybatis')
# 初始化sqlite数据库连接
engine = create_engine('sqlite:///../../introduction_dir/test.db')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


def insert():
    session = DBSession()
    user_1 = User(id=77, name='ashe')
    session.add(user_1)
    session.commit()
    session.close()


def query():
    session = DBSession()
    user = session.query(User).filter(User.id == 77).one()
    print('type of user:', type(user))
    print('name of user:', user.name)


insert()
query()
