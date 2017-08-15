# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_href=scrapy.Field()
    job_name=scrapy.Field()
    company_name=scrapy.Field()
    company_href=scrapy.Field()
    company_location=scrapy.Field()
    job_salary=scrapy.Field()
    last_update_time=scrapy.Field()

class Jobdetail(scrapy.Item):

    job_name=scrapy.Field()
    job_href=scrapy.Field()
    job_details=scrapy.Field()
    job_description=scrapy.Field()
    job_salary=scrapy.Field()
    job_location=scrapy.Field()
    job_publish_date=scrapy.Field()
    job_attribution=scrapy.Field()
    job_experience=scrapy.Field()
    job_education=scrapy.Field()
    job_hire_amount=scrapy.Field()
    job_classify=scrapy.Field()
    job_requirement=scrapy.Field()
