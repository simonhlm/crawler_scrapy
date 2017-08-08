#! /usr/bin/env python

import scrapy
import re

from bs4 import BeautifulSoup
from scrapy.http import Request
from recurit.items import RecuritItem, Jobdetail

class RecuritSpider(scrapy.Spider):
    """docstring fRecuritSpider"""
    name = 'recurit'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=成都&bj=160000&p=0']

    def parse(self, response):

        bsobj = BeautifulSoup(response.body,'html.parser')
        r_item = RecuritItem()

        job_href=[]
        job_name=[]
        company_name=[]
        company_href=[]
        company_location=[]
        job_salary=[]
        last_update_time=[]

        job_details = bsobj.find_all('a',{'href':re.compile(r'http://jobs.zhaopin.com/.*.htm')})

        for item in job_details: # for the post content
            #thread_href.append(item['href'])
            #thread_id.append(re.search(r'thread-(\d*)-',item['href']).group(1))
            job_href.append(item['href'])
            job_name.append(item.text)
            yield Request(url = item['href'] , callback = self.parse_details)

        company_details = bsobj.find_all('a',{'href':re.compile(r'http://company.zhaopin.com/.*.htm')})
        for item in company_details:
            company_href.append(item['href'])
            if item.text != '':
                company_name.append(item.text)

        salary_details = bsobj.find_all('td',{'class':'zwyx'})
        for item in salary_details:
            job_salary.append(item.text)

        company_location_details = bsobj.find_all('td',{'class':'gzdd'})
        for item in company_location_details:
            company_location.append(item.text)

        last_update = bsobj.find_all('td',{'class':'gxsj'})
        for item in last_update:
            last_update_time.append(item.text)

    def parse_details(self, response):

        bsobj = BeautifulSoup(response.body,'html.parser')
        job_info = bsobj.find_all('ul',{'class':'terminal-ul clearfix'})
        job_description = re.split(r'\n',job_info[0].text)

        item = Jobdetail()

        item['job_salary'] = re.split(r'：',job_description[1])[1]
        item['job_location'] = re.split(r'：',job_description[2])[1]
        item['job_publish_date'] = re.split(r'：',job_description[3])[1]
        item['job_attribution'] = re.split(r'：',job_description[4])[1]
        item['job_experience'] =re.split(r'：',job_description[5])[1]
        item['job_education'] = re.split(r'：',job_description[6])[1]
        item['job_hire_amount'] = re.split(r'：',job_description[7])[1]
        item['job_classify'] = re.split(r'：',job_description[8])[1]

        company_info = bsobj.find_all('ul',{'class':'terminal-ul clearfix terminal-company mt20'}) 

        job_require = bsobj.find_all('div',{'class':'tab-inner-cont'}) #,'style':'display: block;'})
        # To remove the address information from the job requirement
        job_require = re.split('工作地址',job_require[0].text)[0]
        item['job_requirement'] = re.sub(r'\n',' ',job_require)

        return item


