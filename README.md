# Facebook Scraper

Scraper for posts in Facebook user profiles, pages and groups.

Extracts list of dicts with:

| params         | description |
| -------------- | ----------- |
| published      | Formatted datetime of published |
| description    | Post text content |
| images         | List of images in posts |
| post_url       | The unique post url |
| external_links | External links found in description |
| like_url       | The Like url |

## Installation

1.Clone or download this repository: git clone https://github.com/iyed-01/web_scrapping

2.build image: docker build -t image .

3.Run the FastAPI application with: python3 -m uvicorn main:app --reload

## P.S: 
requirements can be also installed with: pip install -r requirements.txt

## Questions

Please be free to ask about anything in the code.
