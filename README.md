# Big Data Hands-On Projects

This repository is a collection of projects covering various aspects of big data technologies and tools. Each project explores a different topic, allowing you to gain practical experience in a variety of areas. Below, we provide a brief overview of the main project folders:

## NoSQL Databases (Cassandra, MongoDB, Neo4j, Elasticsearch)

Explore the world of NoSQL databases with this project, which focuses on MongoDB, Cassandra, Neo4j, and Elasticsearch. Each of these databases represents a different NoSQL paradigm, and the project allows you to work with them hands-on.

### Contents

- **MongoDB**:
  - Collect tweets from the Sahamyab API.
  - Preprocess tweets, extract hashtags, and replace Arabic characters.
  - Perform sample queries and aggregation for tweet analysis.
  - Learn about indexing for performance optimization.

- **Cassandra**:
  - Explore data modeling using a sample music dataset.
  - Create keyspaces and tables.
  - Execute sample queries related to song information and aggregations.

- **Neo4j**:
  - Load sample Lord of the Rings data.
  - Execute Cypher query examples to find character relationships.
  - Visualize graph results to better understand the data.

- **Elasticsearch**:
  - Index tweets using Python.
  - Perform sample searches on tweets.
  - Create visualizations for hashtags and user activity.

The project provides comprehensive explanations, code snippets, and screenshots to help you dive into the world of NoSQL databases.

## Spark

This project is your gateway to Apache Spark, a powerful tool for big data processing. You'll work with Spark in Google Colab notebooks, and the necessary datasets are provided along with the exercise instructions.

### Exercises

- **Basics**:
  - Count words and word frequencies in a text file.
  - Identify words starting with 'M'.
  - Count and filter 5-letter words.
  - Find and remove stop words.
  - Discover frequent bigrams.

- **Log File Analysis**:
  - Analyze a server log file to extract valuable insights, including unique hosts, daily requests per host, GIF request statistics, top domains by request frequency, and HTTP error frequencies.

- **DataFrames and SQL**:
  - Leverage Spark DataFrames and Spark SQL to analyze stock market data, such as expensive and cheapest stocks, trading volumes, price fluctuations, and more.

- **Graph Analysis**:
  - Build a graph from Wikipedia links data and perform analyses on in and out degrees, component sizes, and top pages by in degree.

## Crawler, Kafka, Elasticsearch

This project tackles real-time data pipeline construction, focusing on data ingestion, storage, and search for Iranian social media channels and tweets.

### Main Components

- **Data Ingestion**:
  - Scrape posts from Iranian social media platforms and publish them to a Kafka topic.
  - Use Twitter's streaming API to ingest tweets matching specific criteria, extracting metadata during ingestion.

- **Storage and Search**:
  - Store raw post JSON in Elasticsearch using the Persian analyzer.
  - Create Kibana dashboards to visualize recent posts, post frequencies for keywords, top hashtags, and more.
  - Build searches to find posts containing specific words or hashtags.

Feel free to explore each project folder for detailed READMEs, code, and reports to deepen your understanding of big data technologies. Happy learning and exploring!
