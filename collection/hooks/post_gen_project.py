# This file is part of Foobar.
#
#    Foobar is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
This dumps the cookiecutter context into a file for consumption of
subsequent invocation of cookiecutter
"""

import yaml

# cookiecutter imported via jinja2 is an OrderedDict
from collections import OrderedDict  	# noqa: F401

context = {{ cookiecutter }}  		# noqa: F821,E201,E202

default_context = {'default_context': dict(context)}
default_context_file = open("cookiecutter.yaml", "w")
default_context_file.write(yaml.dump(default_context))
