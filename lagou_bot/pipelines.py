# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from lagou_bot.create_db import Base, Job
from slackclient import SlackClient
from lagou_bot import settings
from lagou_bot.util import post_listing_to_slack


class LagouJobInfoDbPipeline(object):
    """将item保存到数据库"""

    def __init__(self):
        engine = create_engine('sqlite:///lagou.db')
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def process_item(self, item, spider):
        job = self.session.query(Job).filter_by(position_id=item["positionId"]).first()

        if job is None:
            job = Job()
            job.keyword = item["keyword"]
            job.company_id = item["companyId"]
            job.format_create_time = item["formatCreateTime"]
            job.score = item["score"]
            job.position_id = item["positionId"]
            job.position_name = item["positionName"]
            job.create_time = item["createTime"]
            job.position_advantage = item["positionAdvantage"]
            job.salary = item["salary"]
            job.approve = item["approve"]
            job.work_year = item["workYear"]
            job.education = item["education"]
            job.city = item["city"]
            job.company_logo = item["companyLogo"]
            job.job_nature = item["jobNature"]
            job.industry_field = item["industryField"]
            job.company_short_name = item["companyShortName"]
            job.finance_stage = item["financeStage"]
            job.company_size = item["companySize"]
            job.district = item["district"]
            job.company_label_list = item["companyLabelList"]
            job.company_full_name = item["companyFullName"]
            job.ad_word = item["adWord"]
            job.business_zones = item["businessZones"]
            job.im_state = item["imState"]
            job.last_login = item["lastLogin"]
            job.publisher_id = item["publisherId"]
            job.explain = item["explain"]
            job.plus = item["plus"]
            job.pc_show = item["pcShow"]
            job.app_show = item["appShow"]
            job.deliver = item["deliver"]
            job.grade_description = item["gradeDescription"]
            job.promotion_score_explain = item["promotionScoreExplain"]
            job.first_type = item["firstType"]
            job.second_type = item["secondType"]
            job.position_labels = item["positionLabels"]

            # Save the listing so we don't grab it again.
            self.session.add(job)
            self.session.commit()
            return item
        else:
            raise DropItem("Job already exists %s" % item)


class LagouJobSendMsgPipeline(object):
    """将item保存到数据库"""

    def __init__(self):
        self.slackClient = SlackClient(settings.SLACK_TOKEN)

    def process_item(self, item, spider):
        # Create a slack client.

        # Post each result to slack.
        post_listing_to_slack(self.slackClient, item)
        return item
