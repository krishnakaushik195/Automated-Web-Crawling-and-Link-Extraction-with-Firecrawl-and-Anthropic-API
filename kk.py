import os
import datetime
import time
from firecrawl import FirecrawlApp
import json
import anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY") or ""
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY") or ""

# Define the blog URL
blog_url = "https://mendable.ai/blog"

# Initialize Anthropics client and Firecrawl app
client = anthropic.Anthropic(api_key=anthropic_api_key)

app = FirecrawlApp(api_key=firecrawl_api_key)

# Perform the crawl with the updated API structure
crawl_result = app.crawl_url(blog_url)

# Initialize a list to store potential links
potential_links = []

# Check if crawl_result is valid
if crawl_result:
    print("Collecting potential links from crawl_result:")
    
    # Iterate through the crawl results
    for item in crawl_result.get('data', []):
        metadata = item.get("metadata", {})
        og_url = metadata.get("ogUrl")
        title = metadata.get("title")
        
        # Ensure we don't include the blog_url itself
        if og_url and title and og_url != blog_url:
            potential_links.append({"url": og_url, "title": title})
    
    # Display collected links
    print(f"Collected {len(potential_links)} potential links:")
    for link in potential_links:
        print(f"URL: {link['url']}, Title: {link['title']}")
else:
    print("crawl_result is empty or None")
