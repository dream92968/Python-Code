# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了

import urllib.request
import time
'nid%22%'
url = ['https://blog.csdn.net/yzy_1996/article/details/82916940',
        'https://blog.csdn.net/yzy_1996/article/details/84482107',
        'https://blog.csdn.net/yzy_1996/article/details/84618536',
        'https://blog.csdn.net/yzy_1996/article/details/83756198',
        'https://blog.csdn.net/yzy_1996/article/details/80223053',
        'https://blog.csdn.net/yzy_1996/article/details/83756357',
        'https://blog.csdn.net/yzy_1996/article/details/81951189',]

countUrl = len(url)
count = 0
count1 = 0

# 加入请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

# 让程序一直执行
while True:  
    if count1 < 1000:
        try:  # 正常运行
            count = count + 1
            print(count, 'times')  # 监视程序是否在正常运行，输出运行了多少次         
            for i in range(countUrl):  # 遍历所有url
                req = urllib.request.Request(url[i] ,headers=headers)
                urllib.request.urlopen(req)  # 访问网页
            time.sleep(70)  # 间隔执行

        except urllib.error.HTTPError:  # 服务器异常
            print('HTTPError')
            count1 = count1 + 1
            time.sleep(10)
            
        except urllib.error.URLError:  # 链接异常
            print('URLError')
            count1 = count1 + 1
            time.sleep(10)
        
        except Exception:  # 其他异常
            print('Retry')
            count1 = count1 + 1
            time.sleep(10)