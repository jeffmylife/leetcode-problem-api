import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("problemSlug", help="Put the \'title slug\' for the LeetCode problem. \
                    You can find it in the url of the problem page. Example: \"network-delay-time\".")
args = parser.parse_args()
titleSlug = args.problemSlug

query_string = """query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    content
    difficulty
    stats
    hints
    sampleTestCase
    envInfo
  }
}
"""

data = {"operationName": "questionData",
        "variables": {"titleSlug":titleSlug},
        "query": query_string}

rq_json = requests.post('https://leetcode.com/graphql', json = data).text

print(rq_json)