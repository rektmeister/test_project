from db import db


class SysUser(db.Model):
    __tablename__ = "sys_user"  # 设置表名, 表名默认为类名小写
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True
    )  # 设置主键, 默认自增
    code = db.Column(db.String(200))
    nickname = db.Column(db.String(200))
    status = db.Column(db.Integer)

    def keys(self):
        return ('_id','code','nickname', "status")
 
    def __getitem__(self, item):
        return getattr(self, item)
