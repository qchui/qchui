# 异常处理
from rest_framework.views import exception_handler
from django.db import DatabaseError
import logging
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger('django')


def custom_exception_handler(exc, contex):
    """
    自定义异常处理
    :param exc: 异常类
    :param contex: 抛出异常的上下文
    :return: Response相应对象
    """
    response = exception_handler(exc, contex)
    if response is None:
        if isinstance(exc, DatabaseError):
            view = contex('view')
            # 数据库异常
            logger.error('[%s]%s' % (view, exc))
            response = Response('服务器内部错误！', status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response
