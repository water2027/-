import requests
import json
import time

timestamp_in_milliseconds = int(time.time() * 1000)#如果位数不一样需要调整
url = f"https://lms.sysu.edu.cn/lib/ajax/service.php?timestamp={timestamp_in_milliseconds}&sesskey="//将sesskey填在等号后面
cookie = ''//这里是cookie，直接复制即可

def body(i):
    return [{
        "index": 0,
        "methodname": "mod_fsresource_set_time",
        "args": {
            "fsresourceid": int(i),#观察网络请求
            "time": 30,#观看的时间。网页请求时是30，实测可以是60或者你喜欢的数字
            "finish": 0,
            "progress": "100"
        }
    }]

def do_it(value, cookie):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Dnt': '1',
        'Host': 'lms.sysu.edu.cn',
        'Origin': 'https://lms.sysu.edu.cn',
        'Referer': 'https://lms.sysu.edu.cn/mod/fsresource/view.php?id=71622&forceview=1',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'X-Kl-Ajax-Request': 'Ajax_Request',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, headers=headers, data=json.dumps(body(value)))
    try:
        response_data = response.json()#有没有完成可以查看response_data[0]['data']['progress']是否为100.如果不是则没有完成
        print(response_data)
    except json.JSONDecodeError:
        print("Response is not in JSON format")

do_it(5084, cookie)#将复制下来的fsresourceid替换掉这里的5084。fsresourceid貌似是逐个+1的，可以写个循环来完成所有视频
