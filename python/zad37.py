import re


def countLinks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        links = re.findall(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\,]|)+', content)
        count = len(links)
        return count


print(str(countLinks("stronainternetowa.txt")))

