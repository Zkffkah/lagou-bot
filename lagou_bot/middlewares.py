import json
import random
import time
import logging


class ProxyMiddleWare(object):
    """docstring for ProxyMiddleWare"""

    def process_request(self, request, spider):
        """对request对象加上proxy"""
        proxy = self.get_random_proxy()
        request.meta['proxy'] = proxy['http']
        print('use proxy')
        logging.log(logging.DEBUG, '-' * 10)
        logging.log(logging.DEBUG, request.url)
        logging.log(logging.DEBUG, request.body)
        logging.log(logging.DEBUG, proxy)
        logging.log(logging.DEBUG, '-' * 10)

    def process_response(self, request, response, spider):
        """对返回的response处理"""
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            logging.log(logging.DEBUG, '-' * 10)
            logging.log(logging.DEBUG, response.url)
            logging.log(logging.DEBUG, request.body.encode('utf-8'))
            logging.log(logging.DEBUG, response.status)
            logging.log(logging.DEBUG, request.meta['proxy'])
            logging.log(logging.DEBUG, 'proxy block!')
            logging.log(logging.DEBUG, '-' * 10)
            proxy = self.get_random_proxy()
            # 对当前request加上代理
            request.meta['proxy'] = proxy['http']
            return request
        return response

    def get_random_proxy(self):

        """随机从文件中读取proxy"""
        while 1:
            with open('proxies.json', 'r') as f:
                proxies = list(json.loads(f.read()))
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies)
        return proxy
