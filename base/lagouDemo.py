import random
import time

import requests
from openpyxl import Workbook
import pymysql.cursors


#建立链接
def get_conn():
    '''建立数据库连接'''
    conn = pymysql.connect(host='10.16.254.75',
                                user='root',
                                password='1qaz@WS',
                                db='python-demo',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn


#插入输出库数据
def insert(conn, info):
    '''数据写入数据库'''
    with conn.cursor() as cursor:
        sql = "INSERT INTO `python_work` (`shortname`, `fullname`, `industryfield`, `companySize`, `salary`, `city`, `education`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, info)
    conn.commit()


# 获取json字符串
def get_json(url, page, lang_name):
    '''返回当前页面的信息列表'''
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '25',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'JSESSIONID=ABAAAECAAEBABII69D44C508257BFCA665D5739320B83DC; WEBTJ-ID=20211009152847-17c63f44f18925-0f3bc6aa9a1ab8-b7a1a38-2073600-17c63f44f19bc3; RECOMMEND_TIP=true; user_trace_token=20211009152848-e009fbe2-d19b-44a8-9547-ca652f191f82; LGUID=20211009152848-6d0ed3ea-5d56-4f51-89d5-1a6bc294c28f; privacyPolicyPopup=false; _gid=GA1.2.1210510176.1633764529; _ga=GA1.2.513855026.1633764529; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; __lg_stoken__=ccb79fcf05ab519b3bc78d3c84c0aaebf467d05830ab92e95e22de725183162966cfd86ca346e780bf7ebdd63a27075752f8c5c96c4ff525b231e81be0bb47865e0bf5e7f449; X_MIDDLE_TOKEN=cde9d03ee001f8ff18330434125447bf; gate_login_token=61127905e3db709295b349e6a100d4ed774aebdbdd7a38e45249b0faa47bda20; LG_LOGIN_USER_ID=9ead14723262c22dc6fa9e09f764d4564f5f633fb0ee957ea3b22802d975d4c7; LG_HAS_LOGIN=1; _putrc=774DED9A7D603F62123F89F2B170EADC; login=true; unick=%E6%9D%8E%E7%A7%91%E8%83%9C; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=321; index_location_city=%E5%8C%97%E4%BA%AC; __SAFETY_CLOSE_TIME__11859983=1; LGSID=20211009163442-c06b9140-70b3-4054-89a6-549eb569245e; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Furl%3D0f00000uEDLSpLgiC83-vK6a-dHxKrBLbCD-oGBIy45p0KOxGhrAacQCgUh%5FVSnpiJ9RIpk-wB3hKp-vFK0d%5Fl0oU6pO3xYuZEr6YV9Pu3l3Q7hlEWmOM8W91-WxPLxD2I73rvf0VM3aiZ6DGYt65BKU2rzaAoG297oyDI3RbDJ%5FT-fiKi86VSjnbCYhxZ8%5F-1803UoCNOj7kGhjg6efbfKL5AFV.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kstVerQKz33X8M-eXKBqM764mTT5QZst884MgIYtVMH3LFlXgj4qrZul3IhOj4etrOF9q8qHReiM-kl-9h9m3eltMiC.U1Yk0ZDqs2v4%5FsKspynqn0KY5TaV8Un0pyYqnWcd0ATqTZnz0ZNG5yF9pywd0ZKGujYk0APGujY1rjR0UgfqnH0krNtknjDLg1DknjRkg1DsnWn0pvbqn0KzIjYvnjR0mhbqnHR3g1csP7tznHIxPH010AdW5HD3n1n3P1msPW7xnHbknj03nH0sn-tknjFxnfKkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5Hc3n16dnjfsnWD0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdBuAw30A-bm1dcfbD0TA9YXHY0IA7zuvNY5Hm1g1KxnHRs0ZwdT1Y3rHbYnHDLn161rjnvnHR4PHn40ZF-TgfqnHm1n1TvrjfvPW6sn6K1pyfqmyuBrADdPW0snj0zuWnvP0KWTvYqPbR4wj61rHNDPbF7fHK7w0K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg100uA78IyF-gLK%5Fmy4GuZnqn7tsg1fkPWDkPWuxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0K9uAu%5FmyTqnfK%5Fuhnqn0KbmvPb5Hc4nWmsPDDdn1cLrH0sPbwanjDLwWnzf1P7PW-DnjI7wHc3wbfkfHD0IZF9uARqP1msnW0z0AFbpyfqwRwjPjckP1TkPRFAfWR4PRw7nW7KnR7DnbwDfHujnHR0UvnqnfKBIjYs0Aq9IZTqn0KEIjYk0AqzTZfqninsc1nWnBnYrjD3n16kn1RWPj6snanYrj0sQW0snj0snankc1cWnanVc108nj0snj0sc1D8nj0snH0s0Z7xIWYsQWbYg108njKxna3sn7tsQWmvg108PjKxni3sn7tsQWnvg100mMPxTZFEuA-b5H00ThqGuhk9u1Ys0APv5fKGTdqWTADqn0KWTjYs0AN1IjYs0APzm1YdrjDdP6%26us%3Dnewvui%26word%3D%26ck%3D2384.4.116.295.148.493.171.186%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome%5Fpg%26wd%3D%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpc%5Fbaidu%5Fpc%26m%5Fkw%3Dbaidu%5Fcpc%5Fsz%5Ffdafd6%5F067de6%5F%25E6%258B%2589%25E9%2592%25A9%26bd%5Fvid%3D8598842951059219623; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1633764529,1633768482; TG-TRACK-CODE=index_search; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211859983%22%2C%22first_id%22%3A%2217c63f453e0184-0110907f8f430e-b7a1a38-2073600-17c63f453e1d79%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2294.0.4606.61%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c63f453e0184-0110907f8f430e-b7a1a38-2073600-17c63f453e1d79%22%7D; X_HTTP_TOKEN=80f82f0f1acda0068319673361e456a8fe3c6e4f64; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1633769139; LGRID=20211009164539-004ceeaa-a480-4469-a81c-e32fb71bafe9; SEARCH_ID=403fc91dbe57409eac2b96781087a3f0',
        'origin': 'https://www.lagou.com',
        'pragma': 'no-cache',
        'referer': 'https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-76d843c9f3306fb3e734dc68e0346759-81bb177c117195bd-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'x-anit-forge-code': '0',
        'x-anit-forge-token': 'None',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {'first': 'false', 'pn': page, 'kd': lang_name}
    json = requests.post(url, data, headers=headers).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i.get('companyShortName', '无'))
        info.append(i.get('companyFullName', '无'))
        info.append(i.get('industryField', '无'))
        info.append(i.get('companySize', '无'))
        info.append(i.get('salary', '无'))
        info.append(i.get('city', '无'))
        info.append(i.get('education', '无'))
        info_list.append(info)
    return info_list


#查询数据信息
def main():
    lang_name = 'python'
    wb = Workbook()  # 打开 excel 工作簿
    conn = get_conn()  # 建立数据库连接  不存数据库 注释此行
    # 不同的城市获取不同的数据
    for i in ['北京', '上海', '广州', '深圳', '杭州']:   # 五个城市
        page = 12
        ws1 = wb.active
        ws1.title = lang_name
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)
        while page < 31:   # 每个城市30页信息
            info = get_json(url, page, lang_name)
            page += 1
            print(i, 'page', page)
            time.sleep(random.randint(10, 20))
            for row in info:
                print("数据格式%s"%row)
                insert(conn, tuple(row))  # 插入数据库，若不想存入 注释此行
                ws1.append(row)
            time.sleep(1)
    conn.close()  # 关闭数据库连接，不存数据库 注释此行
    wb.save('{}职位信息.xlsx'.format(lang_name))

if __name__ == '__main__':
    main()