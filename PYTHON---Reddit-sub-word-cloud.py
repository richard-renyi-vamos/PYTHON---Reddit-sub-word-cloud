import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

# Combine the titles into a single text blob
text = ' '.join(post_titles)

# Create the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
