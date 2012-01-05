#!/usr/bin/env python
# coding: utf-8
# title = Other `Table` methods
#A `Table` is implemented as a list of rows, with some methods to use plugins
#, ordering and do other things. `Table` objects have all the methods other
#Python mutable objects
#have (except for `sort`), so you can use `Table.extend`, `Table.index`,
#`Table.count` and so on. You can also use slices and
#[all mutable sequence operations](http://docs.python.org/library/stdtypes.html#mutable-sequence-types)
#(except for `sort`, because we have `Table.order_by`).
#> Note: all these methods support `tuple`, `list` or `dict` notations of row.

from outputty import Table

table = Table(headers=['City', 'State', 'Country'])
table.append(['Três Rios', 'Rio de Janeiro', 'Brazil'])
table.append(['Niterói', 'Rio de Janeiro', 'Brazil'])
table.append(['Rio de Janeiro', 'Rio de Janeiro', 'Brazil'])
table.append(['Porto Alegre', 'Rio Grande do Sul', 'Brazil'])
table.append(['São Paulo', 'São Paulo', 'Brazil'])

print 'First 3 rows:'
for row in table[:3]:
    print row
#Insert a row in the first position, using dict notation:
table.insert(0, {'City': 'La Paz', 'State': 'La Paz', 'Country': 'Bolivia'})
print 'New table:'
print table
table.reverse()
print 'And the table in the reversed order:'
print table

popped_row = table.pop()
rio = ['Rio de Janeiro', 'Rio de Janeiro', 'Brazil']
table.append(rio) #repeated row
number_of_rios = table.count(rio)
index_of_first_rio = table.index(rio)
table.remove(rio) #remove the first occurrence of this row
number_of_rows = len(table)
print 'Popped row:', popped_row
print 'Number of rows:', number_of_rows
print 'Count of Rios rows (before remove):', number_of_rios
print 'Table after pop and remove:'
print table
