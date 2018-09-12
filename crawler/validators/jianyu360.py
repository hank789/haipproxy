"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from config.settings import (
    TEMP_JIANYU360_QUEUE, VALIDATED_JIANYU360_QUEUE,
    TTL_JIANYU360_QUEUE, SPEED_JIANYU360_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class JianyuValidator(BaseValidator, ValidatorRedisSpider):
    """This validator check the liveness of zhihu proxy resources"""
    name = 'jianyu360'
    urls = [
        'https://www.jianyu360.com/jylab/supsearch/index.html'
    ]
    task_queue = TEMP_JIANYU360_QUEUE
    score_queue = VALIDATED_JIANYU360_QUEUE
    ttl_queue = TTL_JIANYU360_QUEUE
    speed_queue = SPEED_JIANYU360_QUEUE
    success_key = '最新招标信息'

