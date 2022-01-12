import requests
from bs4 import BeautifulSoup

def count_nested(soup, count_dict):
    if hasattr(soup, 'children'):
        for child in soup.children:
            if hasattr(child, 'find_all'):
                if child.name in count_dict:
                    count_dict[child.name]['nested'] += len(child.find_all(recursive=False))
                    count_dict[child.name]['count'] += 1
                else:
                    count_dict[child.name] = {'nested': len(child.find_all(recursive=False)), 'count': 1}
            count_nested(child, count_dict)
        
    return count_dict

def parse_response(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    count_dict = {}
    count_dict = count_nested(soup, count_dict)
    return count_dict