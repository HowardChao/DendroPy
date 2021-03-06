#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dendropy

trees = dendropy.TreeList()
for tree_file in ['pythonidae.mb.run1.t',
        'pythonidae.mb.run2.t',
        'pythonidae.mb.run3.t',
        'pythonidae.mb.run4.t']:
    trees.read(
            path=tree_file,
            schema='nexus',
            tree_offset=20)
split_leaves = ['Morelia amethistina', 'Morelia tracyae']
f = trees.frequency_of_bipartition(labels=split_leaves)
print('Frequency of split %s: %s' % (split_leaves, f))
