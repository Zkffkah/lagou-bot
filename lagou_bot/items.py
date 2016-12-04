# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouJobInfo(scrapy.Item):
    """docstring for LagouJobInfo"""
    keyword = scrapy.Field()
    companyId = scrapy.Field()
    formatCreateTime = scrapy.Field()
    score = scrapy.Field()
    positionId = scrapy.Field()
    positionName = scrapy.Field()
    createTime = scrapy.Field()
    positionAdvantage = scrapy.Field()
    salary = scrapy.Field()
    approve = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    companyLogo = scrapy.Field()
    jobNature = scrapy.Field()
    industryField = scrapy.Field()
    companyShortName = scrapy.Field()
    financeStage = scrapy.Field()
    companySize = scrapy.Field()
    district = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyFullName = scrapy.Field()
    adWord = scrapy.Field()
    businessZones = scrapy.Field()
    imState = scrapy.Field()
    lastLogin = scrapy.Field()
    publisherId = scrapy.Field()
    explain = scrapy.Field()
    plus = scrapy.Field()
    pcShow = scrapy.Field()
    appShow = scrapy.Field()
    deliver = scrapy.Field()
    gradeDescription = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    positionLabels = scrapy.Field()
