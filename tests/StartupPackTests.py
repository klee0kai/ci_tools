from unittest import TestCase

from ci_tools import StartupToolsPack


class StartupPackTests(TestCase):

    def test_hello_world(self):
        tool = StartupToolsPack()
        md = tool.hello_world()
        print(md)

        with(open("sum.md", "w")) as f:
            f.write(md)
