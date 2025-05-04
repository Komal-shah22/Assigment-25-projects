import requests
from bs4 import BeautifulSoup

def get_profile_image_url(github_url):
    try:
        response = requests.get(github_url)
        if response.status_code != 200:
            print("Failed to retrieve page. Please check the URL.")
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tag = soup.find('img', {'alt': 'Avatar'})
        if img_tag:
            return img_tag['src']
        else:
            print("Profile image not found.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def welcome_message():
    print("\n\t~~~~~~~~~~ WELCOME TO THE GITHUB PROFILE SCRAPER ~~~~~~~~~~")
    print("Paste a GitHub profile link and get the profile image URL instantly!\n")

while True:
    welcome_message()
    github_link = input("Enter GitHub profile link (e.g., https://github.com/torvalds): ").strip()
    
    image_url = get_profile_image_url(github_link)
    
    if image_url:
        print(f"\n✅ Profile image URL: {image_url}")
    else:
        print("❌ Could not retrieve image URL.")

    again = input("\nDo you want to scrape another profile? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n👋 Goodbye! Thanks for using the scraper.")
        break
