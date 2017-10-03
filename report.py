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
    for listing in report:
        # Get the listing's title and content
        title, content = listing[0], listing[1]

        # I learned how to check for a decimal from the following
        # Stack Overflow discussion:
        # https://stackoverflow.com/questions/41036535/python-how-to-test-if-a-users-input-is-a-decimal-number
        if type(content) is int:
            suffix = " views"
        else:
            suffix = "% errors"
        print("    {} — {}{}".format(title, content, suffix))

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

# I built the following SQL query with help from these resources:
# https://dba.stackexchange.com/questions/63506/merge-two-select-queries-with-different-where-clauses
# https://stackoverflow.com/questions/1780242/postgres-math-expression-calculcated-for-each-row-in-table
# https://stackoverflow.com/questions/6133107/extract-date-yyyy-mm-dd-from-a-timestamp-in-postgresql
error_percentage = (
    "3. On which days did more than 1% of requests lead to errors?",
    "SELECT TO_CHAR(first.date, 'FMMonth DD, YYYY') AS date, "
    "TRUNC((errors / requests::float * 100)::DECIMAL, 2) AS error_percentage "
    "FROM (SELECT time::DATE as date, COUNT(*) AS errors FROM log "
    "WHERE status != '200 OK' GROUP BY date ORDER BY date) AS first "
    "JOIN (SELECT time::DATE as date, COUNT(*) AS requests FROM log "
    "WHERE status = '200 OK' GROUP BY date ORDER BY date) AS second "
    "ON first.date = second.date "
    "WHERE TRUNC((errors / requests::float * 100)::DECIMAL, 2) >= 1;")

# Add the question/query sets to a list.
query_sets = [top_articles, top_authors, error_percentage]

# Pass each set's data into the appropriate functions.
for i, query_set in enumerate(query_sets):
    question, query = query_set[0], query_set[1]
    report = get_report(query)

    # Print a newline before every report after the first one.
    if i > 0:
        print()
    print_report(question, report)
