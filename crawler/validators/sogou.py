"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from config.settings import (
    TEMP_SOGOU_QUEUE, VALIDATED_SOGOU_QUEUE,
    TTL_SOGOU_QUEUE, SPEED_SOGOU_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class SoGouValidator(BaseValidator, ValidatorRedisSpider):
    """This validator check the liveness of zhihu proxy resources"""
    name = 'sogou'
    urls = [
        'http://weixin.sogou.com/weixin?type=1&query=yonsuper&ie=utf8&s_from=input&_sug_=y&_sug_type_='
    ]
    task_queue = TEMP_SOGOU_QUEUE
    score_queue = VALIDATED_SOGOU_QUEUE
    ttl_queue = TTL_SOGOU_QUEUE
    speed_queue = SPEED_SOGOU_QUEUE
    success_key = '用友云'

