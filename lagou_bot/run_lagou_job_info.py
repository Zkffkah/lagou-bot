from scrapy import cmdline


def do_scrape():
    cmd = 'scrapy crawl lagou_job_info -s JOBDIR=crawls/somespider-1'
    cmdline.execute(cmd.split(' '))


if __name__ == '__main__':
    do_scrape()
