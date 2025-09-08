import hashlib

# 定义一个函数来创建哈希加盐值
def create_hash_with_salt(password, salt=None):
    hash_object = hashlib.sha256(password.encode("utf-8") + salt.encode("utf-8"))
    return hash_object.hexdigest()
