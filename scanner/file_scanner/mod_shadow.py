#!/usr/bin/env python

import requests
import re


def scan_domain(site):
    try:
        if "http://" in site or "https://" in site:
            get_response = requests.get(site)
            return get_response
        else:
            print("[-] MissingSchemaError. Invalid URL: " + str(site) + ". Try http://" + str(site) + " or https://" + str(site))
    except requests.exceptions.ConnectionError:
        pass



def html_content(site):
    if "http://" in site or "https://" in site:
        response = scan_domain(site)
        return response.content
    else:
        print("[-] Incomplete URL. Try http://" + site + " or https://" + site)



def dir_list(site):
    response_content = str(html_content(site))
    url = re.findall('(?:href=\s?)"(.*?)"', response_content)    #   (?:href=\s?) --> ? in the last include space if there exist any space else not
    return url




