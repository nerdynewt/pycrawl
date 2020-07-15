#!/bin/env python3

import lists
import re
# print(lists.exclude.raw_list)

def validate(url):
    reg = re.compile(r'https?://(?:[a-z]+?\.)?(?:www\.)?([a-zA-Z0-9]+?\.[a-z]+)')
    if reg.match(url):
        domain = reg.findall(url)[0]
    else:
        domain = url
    if url in lists.indexed:
        return False, "Already Indexed"
    if lists.domains.count(domain) > 15:
        return False, "Domain capped"
    if re.findall(lists.exclude.regex_string, url):
        return False, "URL found in exclude"
    elif re.findall(lists.sinners.regex_string, url):
        return False, "URL found in sinners"
    elif re.findall(lists.corporates.regex_string, url):
        return False, "URL found in corporates"
    elif '?' in url:
        return False, "PHP query in URL"
    else:
        lists.domains.append(domain)
        return True, "URL is valid"

if __name__ == '__main__':
    import sys
    print(validate(sys.argv[1]))
