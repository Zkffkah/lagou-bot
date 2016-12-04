import logging

from lagou_bot import settings


def post_listing_to_slack(sc, job):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = "{0} | {1} | {2} | {3} | {4} | <{5}>".format(job["companyShortName"], job["workYear"], job["salary"],
                                                        job["financeStage"], job["positionName"],
                                                        "https://www.lagou.com/jobs/" + str(job["positionId"]) + ".html")
    result = sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL, text=desc,
        username='lagou-bot', icon_emoji=':robot_face:'
    )

    logging.log(logging.DEBUG,result)
