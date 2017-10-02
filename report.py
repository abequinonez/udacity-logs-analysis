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


def print_report(report):
    """Prints the report retrieved from the database."""
    for article in report:
        # Get the article's title and views
        title, views = article[0], article[1]
        print("\"{}\" — {} views".format(title, views))
