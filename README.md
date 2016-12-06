Lagou Bot
-------------------

This is a scrapy based bot that will scrape lagou.com for real-time jobs matching specific criteria, then alert you in Slack. 

This will let you quickly see the best new jobs at the first time.  You can adjust the settings to change your job name keywords and cities.

How It Looks
--------------------

<img src="/art/screenshot.png" alt="screenshot" title="screenshot" height="486" />

Settings
--------------------

Look in `settings.py` for a full list of all the configuration options.  Here's a high level overview:

* `CITY_NAMES` -- the city of the jobs you want to look in
* `JOB_NAMES` -- the subsection of Craigslist housing that you want to look in.
* `SLACK_CHANNEL` -- the Slack channel you want the bot to post in.

External Setup
--------------------

Before using this bot, you'll need a Slack team, a channel for the bot to post into, and a Slack API key:

* Create a Slack team, which you can do [here](https://slack.com/create#email).  
* Create a channel for the jobs to be posted into.  [Here's](https://get.slack.help/hc/en-us/articles/201402297-Creating-a-channel) help on this. 
* Get a Slack API token, which you can do [here](https://api.slack.com/docs/oauth-test-tokens).  [Here's](https://get.slack.help/hc/en-us/articles/215770388-Creating-and-regenerating-API-tokens) more information on the process.

Configuration
--------------------

* Create a file called `private.py` in this folder.
    * Add a value called `SLACK_TOKEN` that contains your Slack API token. See 'private.py.example' for example.
    * Add any other values you want to `private.py`.

Installation + Usage
--------------------

* Install Python 3 and other required package.
* Install the Python requirements with `pip3 install -r requirements.txt`.
* Update `proxies.json` with `python3 proxies.py`.
* Run the program with `python main_loop.py`. Results will be posted to your channel if successful.