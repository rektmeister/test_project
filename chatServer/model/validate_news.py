from db import db


class ValidateNews(db.Model):
    __tablename__ = "t_validate_news"  # 设置表名, 表名默认为类名小写
    _id = db.Column("id",
        db.Integer, primary_key=True, autoincrement=True
    )  # 设置主键, 默认自增
    roomid = db.Column(db.String(200))
    senderId = db.Column(db.Integer)
    senderName = db.Column(db.String(200))
    senderNickname = db.Column(db.String(200))
    senderAvatar = db.Column(db.String(200))
    reveiverId = db.Column(db.Integer)
    time = db.Column(db.String(200))
    additionMessage = db.Column(db.String(200))
    status = db.Column(db.Integer)
    validateType = db.Column(db.Integer)
    groupId = db.Column(db.Integer)

    def keys(self):
        return (
            "_id",
            "roomid",
            "senderId",
            "senderName",
            "senderNickname",
            "senderAvatar",
            "reveiverId",
            "time",
            "additionMessage",
            "status",
            "validateType",
            "groupId",
        )

    def __getitem__(self, item):
        return getattr(self, item)
