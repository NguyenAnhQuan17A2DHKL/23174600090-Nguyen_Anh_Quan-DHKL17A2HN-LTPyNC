import feedparser
import csv

#URL RSS feed:
rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

#Tải và phân tích cú pháp RSS feed:
news_feed = feedparser.parse(rss_url)

#Lưu RSS feed dưới dạng tệp XML:
with open("rss_feed.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(news_feed["feed"]["title"] + "\n")
    for entry in news_feed.entries:
        xml_file.write(entry.title + "\n")
        xml_file.write(entry.link + "\n")
        xml_file.write(entry.published + "\n")
        xml_file.write(entry.summary + "\n\n")

#Tạo danh sách từ điển cho các mục tin tức:
news_items = []
for entry in news_feed.entries:
    news_item = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.published,
        "summary": entry.summary
    }
    news_items.append(news_item)

#Lưu các mục tin tức vào tệp CSV:
csv_file = "news_items.csv"
csv_columns = ["title", "link", "published", "summary"]

try:
    with open(csv_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in news_items:
            writer.writerow(data)
except IOError:
    print("I/O error")

print("RSS feed đã được tải và lưu thành công.")