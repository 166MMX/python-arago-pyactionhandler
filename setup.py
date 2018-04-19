#!/usr/bin/env python
import os
import distutils.core

if os.environ.get('USER', '') == 'vagrant':
	del os.link

name = 'arago-pyactionhandler'

distutils.core.setup(
	name = "arago-pyactionhandler",
	version = "2.5",
	author = "Marcus Klemm",
	author_email = "mklemm@arago.de",
	description = ("Python module for Arago HIRO ActionHandlers"),
	license = "MIT",
	url = "http://www.arago.de",
	long_description="""\
pyactionhandler is a python module to develop external
ActionHandlers for the arago HIRO automation engine.

An ActionHandler is used to access target systems in
order to execute commands. This is not limited to
shell commands but can be anything that provides some
kind of command line or API, e.g. SQL.
	""",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT License",
	],
	packages=['arago.pyactionhandler',
			  'arago.pyactionhandler.protobuf'
	],
	install_requires=['gevent', 'docopt', 'zmq', 'protobuf'],
	scripts=['bin/ah-client.py', 'bin/create-zmq-keypair.sh'],
)
