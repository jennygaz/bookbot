def get_num_words(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return len(book_text.split())

def get_symbols_usage(filepath):
    with open(filepath) as file:
        book_text = file.read()
    book_text = book_text.lower()
    symbols_usage = {}
    for character in book_text:
        if character in symbols_usage:
            symbols_usage[character] += 1
        else:
            symbols_usage[character] = 1
    return symbols_usage

def make_report(dictionary):
    def sort_on(dictionary):
        return dictionary['count']

    dictionaries =  [{'character': key, 'count': value} for key, value in dictionary.items()]
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries
        