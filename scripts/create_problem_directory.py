import argparse
import sys 
import os 
import json 

# input from leetcode_problem_scrape.py
stdin = sys.stdin.read()
rq_json = json.loads(stdin)

# Parse args 
parser = argparse.ArgumentParser()
parser.add_argument("problem_slug", help="Put the \'title slug\' for the LeetCode problem. \
                    You can find it in the url of the problem page. Example: \"network-delay-time\".")
parser.add_argument("leetcode_path", help="Path to leetcode directories")
args = parser.parse_args()
titleSlug = args.problem_slug
leetcode_path = args.leetcode_path

# Adjust Html 
title = f"<h1>{rq_json['data']['question']['title']}</h1>"
title_slug = rq_json["data"]["question"]["titleSlug"]

content = rq_json["data"]['question']["content"]
content = title + content 

# Configure file structure
leetcode_path += "Problems/"
if not os.path.exists(leetcode_path):
    os.mkdir(leetcode_path)
    
difficulty = rq_json["data"]["question"]["difficulty"]
leetcode_path += f"{difficulty}/" 
if not os.path.exists(leetcode_path):
    os.mkdir(leetcode_path)

# Write html 
with open(f"{leetcode_path}{title_slug}.html","w") as f: 
    f.write(content)

# Write json 
with open(f"{leetcode_path}{title_slug}.json","w") as f: 
    f.write(stdin)

    
# contains lang-specific env info  
#env_info = json.loads(rq_json["data"]["question"]["envInfo"])
