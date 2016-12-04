from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Job(Base):
    """
    A table to store data on job info.
    """

    __tablename__ = 'jobs'

    keyword = Column(String)
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    format_create_time = Column(String)
    score = Column(Integer)
    position_id = Column(Integer, unique=True)
    position_name = Column(String)
    create_time = Column(String)
    position_advantage = Column(String)
    salary = Column(String)
    approve = Column(Integer)
    work_year = Column(String)
    education = Column(String)
    city = Column(String)
    company_logo = Column(String)
    job_nature = Column(String)
    industry_field = Column(String)
    company_short_name = Column(String)
    finance_stage = Column(String)
    company_size = Column(String)
    district = Column(String)
    company_label_list = Column(String)
    company_full_name = Column(String)
    ad_word = Column(String)
    business_zones = Column(String)
    im_state = Column(String)
    last_login = Column(Integer)
    publisher_id = Column(Integer)
    explain = Column(String)
    plus = Column(String)
    pc_show = Column(String)
    app_show = Column(String)
    deliver = Column(String)
    grade_description = Column(String)
    promotion_score_explain = Column(String)
    first_type = Column(String)
    second_type = Column(String)
    position_labels = Column(String)


engine = create_engine('sqlite:///lagou.db', echo=False)
Base.metadata.create_all(engine)
