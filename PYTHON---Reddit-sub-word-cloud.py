import praw

# Reddit API credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID', 
    client_secret='YOUR_CLIENT_SECRET', 
    user_agent='YOUR_USER_AGENT'
)

# Fetch the top 100 posts from a subreddit
subreddit_name = 'YOUR_SUBREDDIT'
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=100)

# Collect the titles of the top 100 posts
post_titles = []
for post in top_posts:
    post_titles.append(post.title)
