from io import StringIO


def bullet(text):
    return '- ' + text


def make_link(text: str, link: str) -> str:
    return '[%s](%s)' % (text, link)


class MarkdownPoet:
    def __init__(self, indentation=None):
        self._contents = StringIO()
        self.indentation = indentation if indentation else '    '

    def text(self, text: str):
        self._contents.write(text)
        self._contents.write('\n')

    def text_indented(self, text: str, depth: int):
        text = (depth * self.indentation) + text
        self.text(text)

    def code(self, code: str, lang: str = ""):
        self._contents.write(f"```{lang}\n{code}\n```\n")

    def link(self, text: str, link, depth: int = 0):
        self.text_indented(make_link(text, link), depth)

    def bulleted_link(self, text: str, link: str, depth: int = 0):
        self.text_indented(bullet(make_link(text, link)), depth)

    def bullet(self, text: str, depth=0):
        self.text_indented(bullet(text), depth)

    def heading(self, text, level=1):
        self.text(level * '#' + ' ' + text)

    def image_link(self, node_text, location, decoration):
        self.text('\n\n![%s](%s)%s\n\n' % (node_text, location, decoration))

    def new_page(self):
        self.text('\n\n\\newpage\n\n')

    def close(self):
        self._contents.close()

    def contents(self):
        return self._contents.getvalue()

    def __str__(self):
        return self.contents()
