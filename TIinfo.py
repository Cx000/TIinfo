import requests
from openpyxl import Workbook
import os

def get_domains():
    domains = []
    if os.path.isfile('domain.txt'):
        with open('domain.txt', 'r') as file:
            for line in file:
                domain = line.strip()
                if domain:
                    domains.append(domain)
    return domains

def get_website_content():
    try:
        domains = get_domains()
        if not domains:
            print('domain.txt 文件为空')
            domain = input("请输入 domain：")
            if not domain:
                print('domain 不能为空')
                return
            domains.append(domain)

        wb = Workbook()
        ws = wb.active
        ws.append(['URL', 'Domain', 'IP', 'HTTP Code'])

        for domain in domains:
            page = 1
            total_count = 0
            choice = ''  # Initialize choice outside the while loop

            while True:
                url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list?limit=100&page={page}"
                response = requests.get(url)
                response.raise_for_status()

                data = response.json()
                urls = data.get('url_list', [])
                if not urls:
                    break

                for url_data in urls:
                    url = url_data.get('url')
                    hostname = url_data.get('hostname')
                    result = url_data.get('result', {})
                    urlworker = result.get('urlworker', {})
                    ip = urlworker.get('ip', '')
                    http_code = urlworker.get('http_code', '')

                    ws.append([url, hostname, ip, http_code])
                    total_count += 1

                page += 1

                if page > 50:
                    print('当前获取数据已经达到5000条')
                    choice = input('是否继续？继续可能会需要大量时间（y/n）: ')
                    if choice.lower() in ['y', 'yes']:
                        continue
                    else:
                        break

            if page > 50 and choice.lower() not in ['y', 'yes']:
                break

        wb.save('resource.xlsx')
        print('数据已保存到 resource.xlsx 文件中。')
        print(f'总共获取数据条数：{total_count}')
    except requests.exceptions.RequestException as e:
        print('请求出现异常:', e)
    except Exception as e:
        print('保存文件时出现异常:', e)

if __name__ == '__main__':
    get_website_content()
