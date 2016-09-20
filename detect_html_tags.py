from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr in attrs:
            print "->"," > ".join(attr)

parser = MyHTMLParser()

html = ""
for i in range(int(raw_input())):
    html += raw_input()
    html += '\n'


parser.feed(html)
