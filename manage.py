#!/usr/bin/python3

import os

from flask_script import Manager, Shell, Command

from app import create_app

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
	return dict(app=app)


# As with the Command class, the docstring you use for the function will appear when you run with the -? or --help option:
class Hello(Command):
	"prints hello world"

	def run(self):
		print("hello world")


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("hello", Hello())

if __name__ == '__main__':
	manager.run()
