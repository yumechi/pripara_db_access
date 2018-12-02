#!/bin/sh
# for download shell for pripara team to charactor
curl -s -O https://raw.githubusercontent.com/prickathon/webapi-mock-up/master/_data/pripara-team-characters.csv
curl -s -O https://raw.githubusercontent.com/prickathon/webapi-mock-up/master/_data/pripara-teams.csv
python teams-characters-map.py