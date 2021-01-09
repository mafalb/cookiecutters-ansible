# Copyright (C) 2021 Markus Falb
#
# This file is part of cookiecutters-ansible.
#
# cookiecutters-ansible is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cookiecutters-ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with cookiecutters-ansible. If not, see <https://www.gnu.org/licenses/>.

"""
split collection into namespace and collection_name
"""

{{ cookiecutter.update({"namespace": cookiecutter.collection.split('.')[0]}) }}        # noqa: E501,F821,E201,E202
{{ cookiecutter.update({"collection_name": cookiecutter.collection.split('.')[1]}) }}  # noqa: E501,F821,E201,E202
