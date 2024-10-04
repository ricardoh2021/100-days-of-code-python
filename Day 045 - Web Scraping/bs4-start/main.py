from bs4 import BeautifulSoup
import requests
# import lxml

# with open("website.html", mode="r") as file:
#     contents = file.read()
#
# print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
#
# all_anchor_tags = soup.find_all(name="a")
#
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
#
# company_url = soup.select(selector=".heading")
#
# print(company_url)

# res = requests.get("https://news.ycombinator.com/news")
res = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
ycp_page = res.text

soup = BeautifulSoup(ycp_page, "html.parser")
print(soup.title)

titles = []
article_links = []

articles = soup.find_all(name="a", class_="storylink")

for article in articles:
    title_text = article.getText()
    titles.append(title_text)
    link = article.get("href")
    article_links.append(link)

article_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_votes)

highest_upvotes = max(article_votes)

index_of_max = article_votes.index(highest_upvotes)

best_article = titles[index_of_max]
link_of_best_article = article_links[index_of_max]
print(best_article, link_of_best_article, highest_upvotes)






# print(titles)

# print(res.text)

