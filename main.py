from stats import count_characters
import sys


def main():
    if not(len(sys.argv) == 2):
        print("Usage: python3 main.py <path_to_book>")
    else: 
        print(sys.argv)
        count_characters(sys.argv)


main()