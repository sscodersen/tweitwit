#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#


def usage():
    """
    usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s STATS | -oc OUTPUT_CSV | -oj OUTPUT_JSON | -oh OUTPUT_HTML]

    Twitterbot v2

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         Show the version of this program.
      -t, --timeline        Search for tweets in the bot and user's timeline.
      -k KEYWORD, --keyword KEYWORD
                            Search for tweets with a defined keyword.
      -s STATS, --stats STATS
                            Show the statistics of the inputted bot (username).
      -oc OUTPUT_CSV, --output-csv OUTPUT_CSV
                            Produce a csv file containing the stats for the inputted used (ALL for anyone).
      -oj OUTPUT_JSON, --output-json OUTPUT_JSON
                            Produce a json file containing the stats for the inputted used (ALL for anyone).
      -oh OUTPUT_HTML, --output-html OUTPUT_HTML
                            Produce a html file containing the stats for the inputted used (ALL for anyone).
    """
    print("usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s]")
    print("")
    print("Twitterbot v2")
    print("")
    print("optional arguments:")
    print("  -h, --help     show this help message and exit")
    print("  -v, --version  Show the version of this program.")
    print("  -t, --timeline  Search for tweets in the bot and user's timeline.")
    print("  -k KEYWORD, --keyword KEYWORD")
    print("                        Search for tweets with a defined keyword.")
    print("  -s STATS, --stats STATS")
    print("                        Show the statistics of the inputted bot (username).")
    print("  -oc OUTPUT_CSV, --output-csv OUTPUT_CSV")
    print(
        "                        Produce a csv file containing the stats for the inputted used (ALL for anyone)."
    )
    print("  -oj OUTPUT_JSON, --output-json OUTPUT_JSON")
    print(
        "                        Produce a json file containing the stats for the inputted used (ALL for anyone)."
    )
    print("  -oh OUTPUT_HTML, --output-html OUTPUT_HTML")
    print(
        "                        Produce a html file containing the stats for the inputted used (ALL for anyone)."
    )


usage()
