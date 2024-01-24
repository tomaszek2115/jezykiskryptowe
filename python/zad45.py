from datetime import datetime

def convert(date_text, format):
        datetime_obj = datetime.strptime(date_text, format)
        return datetime_obj


text = input("wprowadz date: ")

print(convert(text, "%Y-%d-%m %H:%M:%S"))
