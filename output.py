#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#

import logging
import os
import db
import csv
import json
import sys

logger = logging.getLogger(__name__)


def create_output_folder():
    """
    This function creates (only if not exists already) the
    `twitterbot2-output` folder.
    """
    directory = "twitterbot2-output"
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(filename):
    """
    This function creates (only if not exists already) the
    output file in the `twitterbot2-output` folder.
    """
    directory = "twitterbot2-output"
    if not os.path.exists(directory + "/" + filename):
        _ = open(directory + "/" + filename, "w+")
    else:
        answer = ask_confirmation()
        if not answer:
            sys.exit()
        else:
            _ = open(directory + "/" + filename, "w+")
    return directory + "/" + filename


def ask_confirmation():
    """
    This function checks if the user wants to override the already
    existing output file.
    """
    answer = str(input("The file already exists. Do you want to override? (Y/n)"))
    if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "":
        return True
    return False


def output_csv(user):
    """
    This function writes in the CSV output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".csv")
        with open(filename, "w", newline="") as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for elem in values:
                wr.writerow(elem)
    logger.info("All data has been written into " + filename)


def output_json(user):
    """
    This function writes in the JSON output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".json")

        dict = {}
        for elem in values:
            if not elem[0] in dict.keys():
                dict[elem[0]] = {}
            dict[elem[0]][elem[1]] = {
                "tweets": elem[2],
                "likes": elem[3],
                "retweets:": elem[4],
            }
        with open(filename, "w") as f:
            json.dump(dict, f)
    logger.info("All data has been written into " + filename)


def banner_html():
    banner = """<html>
    <head>
        <title>Twitterbot2 output</title>
    <style>
    * {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Style the topnav links */
.topnav a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Style the content */
.content {
  background-color: #ddd;
  padding: 10px;
  height: 200px;
}

/* Style the footer */
.footer {
  background-color: #f1f1f1;
  padding: 10px;
  bottom: 0;
  text-align:center;
  width: 100%;
  position: fixed;
}
</style>
    </head>
    <body>
    <div class="topnav">
    <a href="https://github.com/edoardottt/twitterbot2">Twitterbot2</a>
    <a href="https://github.com/edoardottt/twitterbot2">Contribute</a>
    </div>
    """
    return banner


def footer_html():
    footer = """<div class="footer">
        <p>twitterbot2 by <a href='https://github.com/edoardottt/twitterbot2'>edoardottt</a></p>
    </div>
    <br><br><br><br><br><br><br><br>
    </body>
    </html>
    """
    return footer


def output_html(user):
    """
    This function writes in the HTML output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".html")
        with open(filename, "w") as f:
            f.write(banner_html())

            f.write(footer_html())
    logger.info("All data has been written into " + filename)
