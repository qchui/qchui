from functools import wraps
from flask import session, redirect, url_for


def login_check(func):
    #@wraps可以保证装饰器修饰的函数的name的值保持不变
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
