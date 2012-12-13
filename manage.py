#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.script import Command, Option, Manager

from myapp import config
from myapp.main import app_factory
from myapp.commands import CreateDB, DropDB, SeedDB

manager = Manager(app_factory)


class Test(Command):
    """Run tests"""

    start_discovery_dir = "tests"

    def get_options(self):
        return [
            Option("--start_discover", "-s", dest="start_discovery",
                help="Pattern to search for features",
                default=self.start_discovery_dir),
        ]

    def run(self, start_discovery):
        import unittest

        if os.path.exists(start_discovery):
            argv = [config.project_name, "discover"]
            argv += ["-s", start_discovery]

            unittest.main(argv=argv)
        else:
            print("Directory \"%s\" was not found in project root." %
                start_discovery)


class Clean(Command):
    """Clean generated binary files"""

    def run(self):
        """Cleans all .pyc files from the source tree"""
        findcmd = 'find %s -name "*.pyc" -print' % '.'
        count = 0
        for f in os.popen(findcmd).readlines():
            count += 1
            print str(f[:-1])
            os.remove(str(f[:-1]))
        print "Removed %d .pyc files" % count


manager.add_option("-c", "--config", dest="config", required=False,
    default=config.Dev)
manager.add_command("test", Test())
manager.add_command("create_db", CreateDB())
manager.add_command("drop_db", DropDB())
manager.add_command("seed_db", SeedDB())
manager.add_command("clean", Clean())


if __name__ == "__main__":
    manager.run()
