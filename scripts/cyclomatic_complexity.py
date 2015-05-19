import os
from sets import Set

def cyclonmatic_complexity(function_ea):
    f_start = function_ea
    f_end = FindFuncEnd(f_start)

    edges = Set()
    boundaries = Set((f_start,))

    for head in Heads(f_start,f_end):
        if isCode(GetFlags(head)):
            refs = CodeRefsFrom(head, 0)
            refs = Set(filter(lambda x: x >= f_start and x <= f_end, refs))

            if refs:
                next_head = NextHead(head, f_end)
                if isFlow(GetFlags(next_head)):
                    refs.add(next_head)

                boundaries.union_update(refs)

                for r in refs:
                    if isFlow(GetFlags(r)):
                        edges.add((PrevHead(r,f_start), r))
                    edges.add((head,r))
    return len(edges) - len(boundaries) + 2
    return 1

def do_functions():
    cc_dict = dict()
    for seg_ea in Segments():
        for function_ea in Functions(seg_ea,SegEnd(seg_ea)):
            cc_dict[GetFunctionName(function_ea)] = cyclonmatic_complexity(function_ea)

    return cc_dict

# Wait until IDA has done all the analysis tasks
# autoWait()

cc_dict = do_functions()
functions = cc_dict.keys()
functions.sort()
ccs = cc_dict.values()

if os.getenv("IDAPYTHON") == 'auto':
    results = file("cc.dat", 'a+')
    results.write("%3.4f,%03d,%03d %s\n" % (sum(ccs)/float(len(ccs)), max(ccs), min(ccs), GetInputFile()))
    results.close()
    Exit(0)
else:
    for f in functions:
        print f, cc_dict[f]

    print 'Max:%d, Min:%d,Avg:%f' % (max(ccs), min(ccs), sum(ccs)/float(len(ccs)))
