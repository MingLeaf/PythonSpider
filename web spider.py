import requests
import re,time
import threading
headers = {
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9",
        }
semaphore = threading.BoundedSemaphore(50)
d_list = ['上海H型钢','上海中厚板','上海造船板','上海花纹板','上海热轧带钢',
        '北京H型钢','北京中厚板','北京彩涂板卷','北京花纹板','北京热轧板卷']

def get_data(id,semaphore):
    semaphore.acquire()
    url = 'http://www.gtgqw.com/showhz{}.html'.format(id)
    response = requests.get(url,headers=headers)
    text = response.text
    title = re.findall(r"<title>(.*?)</title>",text,re.S)[0]
    try:
        table = re.findall(r'<table.*?>(.*?)</table>',text,re.S)[0]
        if_find = 0
        for t in d_list:
            if title.find(t)>=0:
                d_date = re.findall('<div class="changgui">.*? .*? (.*?)</div>',text,re.S)[0]
                tr=re.findall(r'<tr>(.*?)</tr>',table,re.S)[2]
                list2 = re.findall(r'<td>(.*?)</td>',tr,re.S)
                #替换品名中的特殊字符
                list3 = []
                for l in list2:
                    pattern = re.compile(r'<.*?>',re.S)
                    list3.append(pattern.sub("",l))
                sd = t+','+d_date+','+','.join(list3)+','+title+','+str(id)
                print(id,title)
                if_find=1
                file_name='上海'
                if t.find('北京')>=0:
                    file_name='北京'
                with open(file_name+'.csv','a+') as f:
                    f.write(sd+'\n')
        if(if_find==0):
            print(id,title,'不符合需求')
            with open('log.txt','a+')as f:
                f.write('{},{}\n'.format(id,title))
    except:
        print('匹配异常',id)
    semaphore.release()
#注意事项， 按段爬取，不要一次全爬，爬一段时间之后停止，切换手机热点之后继续爬，可以防止被封IP
#爬取过程中不要动那三个csv文件和txt文件，否则会导致写入失败
for i in range(1551119,1595812):
    t = threading.Thread(target=get_data, args=(i, semaphore))
    t.start()
    time.sleep(0.5)