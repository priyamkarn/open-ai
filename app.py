#team member:Priyam,Lohit
import openai
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API key
openai.api_key = "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"

# Function to generate summary
def generate_summary(url):
    # Scrape abstract from URL
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    abstract = soup.find('blockquote', class_='abstract mathjax').get_text().strip()

    # Generate summary using GPT-3
    prompt = f"Please summarize the following research paper: {abstract}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()

    return summary

# Test the function
url = "https://arxiv.org/abs/1606.04801"  # replace with your desired paper's URL
summary = generate_summary(url)
print(summary)
