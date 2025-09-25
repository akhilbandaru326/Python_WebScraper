import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        # Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # raise error if request fails

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (adjust tags based on website structure)
        headlines = []
        for tag in soup.find_all(["h1", "h2", "h3", "title"]):  
            text = tag.get_text(strip=True)
            if text and text not in headlines:
                headlines.append(text)

        # Save to text file
        with open(output_file, "w", encoding="utf-8") as f:
            for idx, line in enumerate(headlines, 1):
                f.write(f"{idx}. {line}\n")

        print(f"✅ {len(headlines)} headlines saved to '{output_file}'")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    # Example: scraping BBC News (can replace with another news site)
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
