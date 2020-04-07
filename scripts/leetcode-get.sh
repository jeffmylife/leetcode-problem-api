#!/bin/bash
leetcode_path="/Users/jeffreylemoine/Education/LeetCode/"
python leetcode_problem_scrape.py $1 | python create_problem_directory.py $1 $leetcode_path
