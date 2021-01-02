import os
import html
import requests
from difflib import SequenceMatcher
from dotenv import load_dotenv
import praw
from bs4 import BeautifulSoup

def main():
    # todos
    # think of a good way to get feedback?

    load_dotenv()
    reddit = praw.Reddit(
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASS'),
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent="Randy"
    )

    print("Checking for new submissions to convert...")
    for submission in reddit.subreddit("recipes").new(limit=20):
        if not submission.saved:
            submission.save()
            metric_recipe = convert_US_to_metric(submission.selftext)

            similarity = SequenceMatcher(None, submission.selftext, metric_recipe).ratio()
            if similarity < 0.95:
                print("Posting with recipe in metric units", submission.permalink)
                reddit_reply = """**Copy of original post in metric units**  ^([more info](https://github.com/b3ting/reddit-metric-recipe))\n\n%s
                """ % metric_recipe

                print(reddit_reply)
                submission.reply(body=str(reddit_reply))

def convert_US_to_metric(recipe_us):
    response = requests.post('https://convertrecipe.com/convert_US_to_metric.php', data=dict(recipe=recipe_us))
    soup = BeautifulSoup(response.text, features='html.parser')
    metric_recipe = soup.find("textarea", {"id": "recipe_in_metric"})

    metric_recipe_text = metric_recipe.contents

    if metric_recipe_text == []:
        return ''
    else:
        return metric_recipe_text[0]

if __name__ == "__main__":
    main()
