from facebook_scraping import FacebookScraper as FS
import json

def scraper():
    # Enter your Facebook email and password
    email = 'amoriyed123@gmail.com'
    password = 'SmegmZ7ZARWjjv3'

    # Instantiate an object
    fcb_post = FS(email, password, post_url_text='Full Story')

    profile = 'https://www.facebook.com/Presidence.tn'
    data = fcb_post.get_posts_from_profile(profile)
    print("___________________________________________________________________________________________________________________________________________________________")
    print(data)
    print("___________________________________________________________________________________________________________________________________________________________")
    fcb_post.posts_to_csv('presidence_posts')  # You can export the posts as CSV document
    fcb_post.posts_to_json('posts')               # You can export the posts as JSON document
    with open('presidence_posts.csv', 'r', encoding='utf8') as f:
        posts = f.read()
        return posts

scrap= scraper()