#
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser


metacount = 0


class MyHTMLParser(HTMLParser):

    # This will be called when the closing '>' of the tag is reached
    def handle_starttag(self, tag: str, attrs: list) -> None:
        global metacount
        if tag == 'meta':
            metacount += 1

        print('Encountered a start tag:', tag)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

        if attrs.__len__() > 0:
            print('\tAttributes:')
            for a in attrs:
                print('\t', a[0], '=', a[1])

    # Function to handle the ending tag
    def handle_endtag(self, tag: str) -> None:
        print('Encountered an end tag:', tag)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

    # Function to handle character and text data (tag contents)
    def handle_data(self, data: str) -> None:
        if data.isspace():
            return
        print('Encountered some text data:', data)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

    # Function to handle the processing of HTML comments
    def handle_comment(self, data: str) -> None:
        print('Encountered comment:', data)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])


def main() -> None:
    # Instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    # Open the sample HTML file and read it
    f = open('sample.html')
    if f.mode == 'r':
        contents = f.read()  # read the entire file
        parser.feed(contents)

    print('%d meta tags encountered' % metacount)


if __name__ == '__main__':
    main()
