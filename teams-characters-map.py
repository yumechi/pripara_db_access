#!/bin/python env
# encoding: utf-8

import csv
import json


def get_file_element_list(filename: str) -> list:
    ret = []
    with open(filename, 'r') as f:
        render = csv.reader(f)
        keys = next(render)

        for line in render:
            ret.append(dict(zip(keys, line)))
    return ret


def run() -> None:
    teams = get_file_element_list('pripara-teams.csv')
    characters = get_file_element_list('pripara-team-characters.csv')
    teams_dict = {}
    for team in teams:
        key, name = team['key'], team['name']
        teams_dict[key] = {
            'key': key,
            'name': name,
            'character': []
        }
    for character in characters:
        team, character_name = character['team'], character['character']
        teams_dict[team]['character'].append(character_name)
    with open('teams-characters-map.json', 'w') as f:
        json.dump(teams_dict, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    run()
