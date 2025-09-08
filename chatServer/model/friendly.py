from db import db


class Friendly(db.Model):
    __tablename__ = "t_friendly"  # 设置表名, 表名默认为类名小写
    _id = db.Column("id",
        db.Integer, primary_key=True, autoincrement=True
    )  # 设置主键, 默认自增
    user_m = db.Column(db.String(200))
    user_y = db.Column(db.String(200))
    create_date = db.Column(db.DateTime)
