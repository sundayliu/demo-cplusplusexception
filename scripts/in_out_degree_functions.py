# Unordered collections of unique elements
from sets import Set

ea = ScreenEA()
callers = dict()
callees = dict()

for function_ea in Functions(SegStart(ea),SegEnd(ea)):
    f_name = GetFunctionName(function_ea)
    callers[f_name] = Set(map(GetFunctionName,CodeRefsTo(function_ea,1)))
    for ref_ea in CodeRefsTo(function_ea,1):
        caller_name = GetFunctionName(ref_ea)
        callees[caller_name] = callees.get(caller_name,Set())
        callees[caller_name].add(f_name)

#print callees.keys()
#print callers.keys()
functions = Set(callees.keys()+callers.keys())
print len(functions)
for f in functions:
    print "[caller in]%d:%s:[callee out]%d" % (len(callers.get(f,[])), f , len(callees.get(f,[])))

# ea = 0x052e0
# f_name = GetFunctionName(ea)
# print f_name
# for ref_ea in CodeRefsTo(ea,1):
#     print "    %s" % GetFunctionName(ref_ea) 

# for ref_ea in CodeRefsFrom(ea,1):
#     print "    0x%x" % ref_ea