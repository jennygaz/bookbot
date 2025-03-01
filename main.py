import sys
from stats import get_num_words, get_symbols_usage, make_report

def main():
    filepath = "books/frankenstein.txt"
    num_words = get_num_words(filepath)
    symbols_usage = get_symbols_usage(filepath)
    symbols_stats = make_report(symbols_usage)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for dictionary in symbols_stats:
        if dictionary['character'].isalpha() == False:
            continue
        print(f'{dictionary['character']}: {dictionary['count']}')
    print('============= END ===============')

main()