import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = re.search('.*src="http(s)?://(www\.)?youtube\.com/embed/(.*?)"', s)
    if pattern:
        link = 'https://youtu.be/' + pattern.group(3)
        return link

if __name__ == "__main__":
    main()