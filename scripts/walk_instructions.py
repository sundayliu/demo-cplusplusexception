# -*- coding:utf-8 -*-
# sundayliu
# 2015/05/19

"""
统计每种指令的使用次数
"""

mnemonics = dict()

for seg_ea in Segments():
    for head in Heads(seg_ea, SegEnd(seg_ea)):
        if isCode(GetFlags(head)):
            mnem = GetMnem(head)
            mnemonics[mnem] = mnemonics.get(mnem,0) + 1

sorted = map(lambda x:(x[1],x[0]), mnemonics.items())
sorted.sort()

for count, mnemonic in sorted:
    print count, mnemonic

#print sorted