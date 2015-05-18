print "Walk functions"
# Get the segment's starting address
ea = ScreenEA()

# Loop through all the functions
for function_ea in Functions(SegStart(ea),SegEnd(ea)):
    print "Function %s at 0x%x" % (GetFunctionName(function_ea),function_ea)
    for ref in CodeRefsTo(function_ea,1):
        print "     called from %s(0x%x)" % (GetFunctionName(ref), ref)