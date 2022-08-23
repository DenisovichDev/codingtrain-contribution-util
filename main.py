"""
Author: DenisovichDev (https://DenisovichDev.github.io/link-tree/)
This python scripts converts a txt file with old contribution metadata
from the markdown files to individual json files in the new website format
"""

import json

title_iden = "  - title: "
author_iden = "    author:"
name_iden = "      name: "
name_url_iden = "      url: "
url_iden = "    url: "

# Checks if the string has quotes around it
def hasQuotes(string):
    if string[0] == '"':
        return True

# Cleans the strings (quotes and return chars)
def cleanString(string):
    # Removing quotes
    if (hasQuotes(string)):
        string = string[1:-2]
    # Removing potential return chars
    return_char_idx = string.find('\n')
    if return_char_idx != -1:
        string = string[:return_char_idx]
    return string

def main():
    contrib_dicts = []

    with open("contrib.txt", "r") as file:
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
                    name_url = name_url_line[len(name_url_iden):]
                    name_url = cleanString(name_url)
                    auth_dict = {
                        "name" : name,
                        "url" : name_url
                    }
                    contrib_dict["author"] = auth_dict
                    index += 2
                    continue
                author_name = line[len(author_iden) + 1:]
                author_name = cleanString(author_name)
                contrib_dict["author"] = author_name
                index += 1
                continue
            # URL to preview
            if line.find(url_iden) != -1:
                url = line[len(url_iden):]
                url = cleanString(url)
                contrib_dict["url"] = url
                index += 1
                continue
                
            index += 1
        contrib_dicts.append(contrib_dict.copy())
                    
    print(contrib_dicts)

    for idx in range(len(contrib_dicts)):
        contribution = contrib_dicts[idx]
        jsonObj = json.dumps(contribution, indent=4)

        # Writing to sample.json
        with open("contribution" + str(idx + 1) + ".json", "w") as outfile:
            outfile.write(jsonObj + '\n')
                


if __name__=="__main__":
    main()