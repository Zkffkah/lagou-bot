from Proxies import Proxies
import time
import requests
import json


def get_proxies():
    p = Proxies()
    p.get_proxies(100, 2)
    # quantity: 数量
    # type: 类型 (1.国内高匿代理 2.国内普通代理 3.国外高匿代 4.国外普通代理)
    proxy_results = p.get_result()
    print(proxy_results)

    with open('proxies.json', 'w+') as file:
        valid_entries = []
        for proxy_result in proxy_results:
            if verify_lagou(proxy_result):
                valid_entries.append(proxy_result)

        json.dump(valid_entries, file)


def verify_lagou(proxy):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    data = {'pn': '1', 'kd': 'python'}
    url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC'
    try:
        response = requests.post(url, data=data, headers=headers, proxies=proxy, timeout=5)
    # print html.content
    except Exception as e:
        print('fail except %s' % e)
        return False
    if response.status_code in [200]:
        try:
            json.loads(response.text)
        except ValueError:
            print('fail ValueError %s' % proxy)
            return False
        if response.url != url:
            print('fail url != url %s %s' % (response.url, url))
            return False
        print('success %s' % proxy)
        return True
    else:
        print('fail status_code %s' % proxy)
        return False


if __name__ == '__main__':
    # time.sleep(3600)
    # while 1:
    #     proxies = []
    #     with open('proxies.txt', 'r') as f:
    #         for line in f:
    #             if verify_lagou(line.strip()):
    #                 proxies.append(line.strip())
    #     with open('proxies.txt', 'w') as f:
    #         if len(proxies) != 0:
    #             for proxy in set(proxies):
    #                 f.write(str(proxy) + '\n')

    get_proxies()
    # time.sleep(3600)

