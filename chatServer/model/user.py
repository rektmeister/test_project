from db import db


class User(db.Model):
    __tablename__ = "t_user"  # 设置表名, 表名默认为类名小写
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True
    )  # 设置主键, 默认自增
    name = db.Column("user_name", db.String(200))  # 设置字段名 和 唯一约束
    nickname = db.Column(db.String(200))
    signature = db.Column(db.String(200))
    password = db.Column(db.String(200))  # 设置默认值约束 和 索引
    status = db.Column(db.Integer)
    photo = db.Column(db.String(200))
    salt = db.Column(db.String(200))

    def keys(self):
        return ('_id','name','nickname','signature', 'password', "status", "photo", "salt")
 
    def __getitem__(self, item):
        return getattr(self, item)
