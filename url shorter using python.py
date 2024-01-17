import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_code(self):
        # Generate a random 6-character code for shortening
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def shorten_url(self, original_url):
        short_code = self.generate_short_code()
        self.url_mapping[short_code] = original_url
        return f"Shortened URL: http://your-shortener-domain/{short_code}"

    def retrieve_url(self, short_code):
        original_url = self.url_mapping.get(short_code)
        if original_url:
            return f"Original URL: {original_url}"
        else:
            return "URL not found."

if __name__ == "__main__":
    shortener = URLShortener()

    # Shorten a URL
    original_url = input("Enter the URL to shorten: ")
    shortened_url = shortener.shorten_url(original_url)
    print(shortened_url)

    # Retrieve the original URL
    short_code = input("Enter the short code to retrieve the original URL: ")
    retrieved_url = shortener.retrieve_url(short_code)
    print(retrieved_url)
