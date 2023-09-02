# Big Data Project

This project involves building a real-time data pipeline to ingest and analyze posts from Iranian social media channels and tweets. The main components are:

## Data Ingestion

- Scrape posts from Iranian social media platforms like Soroush, Bale, Aigp using bots. Posts are published to a Kafka topic.
- For Twitter, use the streaming API to ingest tweets matching certain filters (lang:fa, keywords, etc).
- Extract metadata like hashtags, keywords, links during ingestion.

## Storage and Search

- Store raw post JSON in Elasticsearch using the Persian analyzer.
- Create Kibana dashboards to view recent posts, post frequencies for keywords, top hashtags, etc.
- Build searches to find posts containing specific words or hashtags.
