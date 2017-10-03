#!/usr/bin/env python3
#
# A logs reporting tool that uses database data to answer questions based
# on article readership and user activity.

import psycopg2


def get_report(query):
    """Returns a report based on the query passed in."""
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    report = cursor.fetchall()
    db.close()
    return report


def print_report(question, report):
    """Prints the report retrieved from the database."""
    print(question)
    for article in report:
        # Get the article's title and views
        title, views = article[0], article[1]
        print("    \"{}\" — {} views".format(title, views))

# I learned about implicit string concatenation from the following
# Stack Overflow discussion:
# https://stackoverflow.com/questions/1874592/how-to-write-very-long-string-that-conforms-with-pep8-and-prevent-e501
top_articles = (
    "1. What are the most popular three articles of all time?",
    "SELECT articles.title, COUNT(*) AS views FROM articles, log "
    "WHERE ('/article/' || articles.slug = log.path) AND "
    "(log.status = '200 OK') GROUP BY articles.title "
    "ORDER BY views DESC LIMIT 3;")

top_authors = (
    "2. Who are the most popular article authors of all time?",
    "SELECT authors.name, COUNT(*) AS views FROM authors, articles, log "
    "WHERE (authors.id = articles.author) AND ('/article/' || "
    "articles.slug = log.path) AND (log.status = '200 OK') "
    "GROUP BY authors.name ORDER BY views DESC;")

# Add the question/query sets to a list.
query_sets = [top_articles, top_authors]

# Pass each set's data into the appropriate functions.
for i, query_set in enumerate(query_sets):
    question, query = query_set[0], query_set[1]
    report = get_report(query)

    # Print a newline before every report after the first one.
    if i > 0:
        print()
    print_report(question, report)
