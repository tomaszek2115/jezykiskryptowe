with open("wersaliki.txt", 'r') as input_file:
    content = input_file.read()

content_uppercase = content.upper()

with open("wersaliki.txt", 'w') as output_file:
    output_file.write(content_uppercase)