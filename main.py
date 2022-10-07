"""
Author: DenisovichDev (https://DenisovichDev.github.io/link-tree/)
This python scripts converts a txt file with old contribution metadata
from the markdown files to individual json files in the new website format
"""

import json
import sys

title_iden = "  - title: "
author_iden = "    author:"
name_iden = "      name: "
name_url_iden = "      url: "
url_iden = "    url: "
video_id_iden = "    video_id: "
source_iden = "    source: "

YT_URL_FORMAT = "https://www.youtube.com/watch?v="


def hasQuotes(string):
    """Checks if the string has quotes.
    Sometimes the strings have quotes and
    sometimes they don't. That's why we need
    to check.
    """
    if string[0] == '"':
        return True

# Cleans the strings (quotes and return chars)


def cleanString(string):
    """Cleans the strings
    This function deletes the unwanted
    quotes and return characters in the end.
    """
    # Removing quotes
    if (hasQuotes(string)):
        string = string[1:-2]
    # Removing potential return chars
    return_char_idx = string.find('\n')
    if return_char_idx != -1:
        string = string[:return_char_idx]
    return string


def main():
    args = sys.argv[1:]  # Command line arguments
    argc = len(args)

    input_file = "contrib.txt"
    # If there is the input filename is in the arguments
    # It uses that as the input file stream, otherwise
    # by default contrib.txt is used
    if (argc > 0):
        # Selects the first argument only.
        # Literally no exception handling
        input_file = args[0]

    contrib_dicts = []

    with open(input_file, "r") as file:
        contrib_dict = {}

        # List of individual lines
        data = file.readlines()

        index = 0
        while index < len(data):
            line = data[index]
            # Title
            if line.find(title_iden) != -1:
                # If not the first one, append to the array
                # and reset the dict
                if (index != 0):
                    contrib_dicts.append(contrib_dict.copy())
                    contrib_dict = {}

                title = line[len(title_iden):]
                if (hasQuotes(title)):
                    title = title[1:-2]
                contrib_dict["title"] = title
                index += 1
                continue
            # Author and Author Dict
            if line.find(author_iden) != -1:
                nested_auth = True if line[len(author_iden)] == '\n' else False
                if nested_auth:
                    name_line = data[index+1]
                    name = name_line[len(name_iden):]
                    name = cleanString(name)
                    name_url_line = data[index+2]
                    # Check if the url is there
                    has_name_url = True if (name_url_line.find(
                        name_url_iden) != -1) else False
                    auth_dict = None
                    if has_name_url:
                        name_url = name_url_line[len(name_url_iden):]
                        name_url = cleanString(name_url)
                        auth_dict = {
                            "name": name,
                            "url": name_url
                        }
                    else:
                        auth_dict = {
                            "name": name
                        }
                    contrib_dict["author"] = auth_dict
                    index += 2
                    continue
                author_name = line[len(author_iden) + 1:]
                author_name = cleanString(author_name)
                auth_dict = {
                    "name": author_name,
                }
                contrib_dict["author"] = auth_dict
                index += 1
                continue
            # URL to preview
            if line.find(url_iden) != -1:
                url = line[len(url_iden):]
                url = cleanString(url)
                contrib_dict["url"] = url
                index += 1
                continue
            else:
                url_not_found = True
            # URL property is not found
            if (url_not_found):
                # Video ID
                if line.find(video_id_iden) != -1:
                    video_id = line[len(video_id_iden):]
                    video_id = cleanString(video_id)
                    yt_url = YT_URL_FORMAT + video_id
                    contrib_dict["url"] = yt_url
                    index += 1
                    continue
                # Source Code
                if line.find(source_iden) != -1:
                    source_code = line[len(source_iden):]
                    source_code = cleanString(source_code)
                    contrib_dict["url"] = source_code
                    index += 1
                    continue

            index += 1
        contrib_dicts.append(contrib_dict.copy())

    # print(contrib_dicts)

    for idx in range(len(contrib_dicts)):
        contribution = contrib_dicts[idx]
        jsonObj = json.dumps(contribution, indent=4)

        # Writing to contribution#.json
        with open("./output/contribution" + str(idx + 1) + ".json", "w") as outfile:
            outfile.write(jsonObj + '\n')
        print("\nFinished writing contribution" + str(idx + 1) + ".json")


if __name__ == "__main__":
    main()
