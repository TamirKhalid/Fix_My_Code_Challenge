def is_valid_password(self, pwd):
    """
    Valid password:
    - `False` if `pwd` is `None`
    - `False` if `pwd` is not a string
    - `False` if `__password` is `None`
    - Compare `__password` and the MD5 value of `pwd`
    """
    if pwd is None or type(pwd) is not str:
        return False
    if self.__password is None:
        return False
    return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password
