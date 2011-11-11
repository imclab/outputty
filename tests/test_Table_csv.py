#!/usr/bin/env python
# coding: utf-8

# Copyright 2011 Álvaro Justen
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from textwrap import dedent

import unittest
import tempfile
import os
import sys

sys.path.insert(0, '..')
from outputty import Table


class TestTableCsv(unittest.TestCase):
    def test_output_to_csv_should_create_the_file_correctly_with_headers(self):
        temp_fp = tempfile.NamedTemporaryFile()
        temp_fp.close()

        my_table = Table(headers=['ham', 'spam', 'eggs'])
        my_table.rows.append({'ham': 'ham spam ham', 'spam': 'spam eggs spam',
                              'eggs': 'eggs ham eggs'})
        my_table.to_csv(temp_fp.name)

        fp = open(temp_fp.name)
        contents = fp.read()
        fp.close()
        os.remove(temp_fp.name)

        self.assertEquals(contents, dedent('''\
        "ham","spam","eggs"
        "ham spam ham","spam eggs spam","eggs ham eggs"
        '''))

    def test_should_import_data_from_csv(self):
        temp_fp = tempfile.NamedTemporaryFile(delete=False)
        temp_fp.write(dedent('''\
        "ham","spam","eggs"
        "ham spam ham","spam eggs spam","eggs ham eggs"
        "ham spam","eggs spam","eggs eggs"
        '''))
        temp_fp.close()

        my_table = Table(from_csv=temp_fp.name)
        os.remove(temp_fp.name)
        self.assertEquals(str(my_table), dedent('''
        +--------------+----------------+---------------+
        |     ham      |      spam      |      eggs     |
        +--------------+----------------+---------------+
        | ham spam ham | spam eggs spam | eggs ham eggs |
        |     ham spam |      eggs spam |     eggs eggs |
        +--------------+----------------+---------------+
        ''').strip())

    def test_input_and_output_character_encoding_in_method_to_csv(self):
        temp_fp = tempfile.NamedTemporaryFile(delete=False)
        temp_fp.close()
        my_table = Table(headers=['Álvaro'.decode('utf8').encode('utf16')],
                         input_encoding='utf16', output_encoding='iso-8859-1')
        my_table.rows.append(['Píton'.decode('utf8').encode('utf16')])
        my_table.to_csv(temp_fp.name)

        fp = open(temp_fp.name)
        file_contents = fp.read()
        fp.close()
        os.remove(temp_fp.name)
        output = '"Álvaro"\n"Píton"\n'.decode('utf8').encode('iso-8859-1')
        self.assertEqual(file_contents, output)

    def test_input_and_output_character_encoding_in_parameter_from_csv(self):
        data = '"Álvaro"\n"Píton"'
        temp_fp = tempfile.NamedTemporaryFile(delete=False)
        temp_fp.write(data.decode('utf8').encode('iso-8859-1'))
        temp_fp.close()
        my_table = Table(from_csv=temp_fp.name, input_encoding='iso-8859-1',
                         output_encoding='utf16')
        os.remove(temp_fp.name)
        output = dedent('''
        +--------+
        | Álvaro |
        +--------+
        |  Píton |
        +--------+
        ''').strip().decode('utf8').encode('utf16')
        self.assertEqual(str(my_table), output)