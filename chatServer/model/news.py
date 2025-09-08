from db import db


class News(db.Model):
    __tablename__ = "t_news"  # 设置表名, 表名默认为类名小写
    _id = db.Column("id",
        db.Integer, primary_key=True, autoincrement=True
    )  # 设置主键, 默认自增
    roomid = db.Column(db.String(200))
    senderId = db.Column(db.Integer)
    senderName = db.Column(db.String(200))
    senderNickname = db.Column(db.String(200))
    senderAvatar = db.Column(db.String(200))
    time = db.Column(db.DateTime)
    message = db.Column(db.String(200))
    messageType = db.Column(db.String(200))
    isReadUser = db.Column(db.String(200))

    
    def keys(self):
        return ('_id','roomid','senderId','senderName', 'senderNickname', 'senderAvatar','time','message','messageType', 'isReadUser')
 
    def __getitem__(self, item):
        return getattr(self, item)