# execfile("eh_frame_parser.py")

class ULEB128:
    def encode(self,obj,context):
        obj2 = []
        value = int(obj)
        while True:
            byte = value & 0x7F
            value >>= 7
            if value != 0:
                byte = byte|0x80
            obj2.append(chr(byte))
            if value == 0:
                break
        return obj2
    def decode(self,obj,context):
        value = 0
        for b in reversed(obj):
            value = value * 128 + (ord(b) & 0x7f)
        return value

class SLEB128:
    def encode(self, obj, context):
        obj2 = []
        value = int(obj)
        if value < 0:
            unsignedRefValue = (1-value) * 2
        else:
            unsignedRefValue = value * 2
        while True:
            byte = value & 0x7F
            value >>= 7
            unsignedRefValue >>= 7
            if unsignedRefValue != 0:
                byte = byte|0x80
            obj2.append(chr(byte))
            if unsignedRefValue == 0:
                break
        return obj2

    def decode(self, obj, context):
        value = 0
        for b in reversed(obj):
            value = value * 128 + (ord(b) & 0x7f)
        if (ord(obj[-1]) & 0x40) != 0:
            value = value - (1 << (7*len(obj)))
        return value

def encodeULEB128(value):
    return value
def decodeULEB128(ea):
    value = 0
    offset = 0
    while True:
        byte = Byte(ea+offset)
        offset = offset + 1
        value = value * 128 + byte & 0x7f
        if byte < 128:
            break
       

    return value,offset

def encodeSLEB128(value):
    return value
def decodeSLEB128(ea):
    value = 0
    offset = 0
    while True:
        byte = Byte(ea+offset)
        offset = offset + 1
        value = value * 128 + byte & 0x7f
        if byte < 128:
            break
        
    if byte & 0x40 != 0:
        value = value - (1 << (7 * offset))

    return value,offset

# Common Information Entry
def parse_CIE(cie_address):
    offset = 0
    cie_length = Dword(cie_address + offset)
    cie_extended_length = -1
    offset = offset + 4
    if cie_length == 0xffffffff:
        cie_extended_length = Qword(cie_address + offset)
        offset = offset + 8

    cie_id = Dword(cie_address + offset)
    offset = offset + 4

    cie_version = Byte(cie_address + offset)
    offset = offset + 1

    cie_augmentation = GetString(cie_address + offset, -1, ASCSTR_C)
    offset = offset + len(cie_augmentation) + 1

    cie_eh_data = 0
    if cie_augmentation.find("eh") != -1:
        cie_eh_data = 0

    cie_code_alignment_factor,code_alignment_factor_size = decodeULEB128(cie_address+offset)
    offset = offset + code_alignment_factor_size

    cie_data_alignment_factor,data_alignment_factor_size = decodeSLEB128(cie_address+offset)
    offset = offset + data_alignment_factor_size

    cie_return_address_register = 0
    return_address_register_size = 0

    if cie_version == 1:
        cie_return_address_register = Byte(cie_address + offset)
        return_address_register_size = 1
        offset = offset + 1
    elif cie_version == 3:
        cie_return_address_register,return_address_register_size = decodeULEB128(cie_address+offset)
        offset = offset + return_address_register_size

    cie_augmentation_data_lenght = 1
    cie_augmentation_data = 1
    cie_initial_instructions = 1
    cie_padding = 1

    offset = 0
    print "%08x CIE Length:%d" % (cie_address+offset, cie_length)
    offset = offset  + 4
    if cie_length == 0xffffffff:
        print "%08x CIE Extended Length:" % (cie_address + offset, cie_extended_length)
        offset = offset + 4

    print "%08x CIE Id:%d" % (cie_address + offset, cie_id)
    offset = offset + 4

    print "%08x CIE Version:%d" % (cie_address + offset, cie_version)
    offset = offset + 1

    print "%08x CIE Augmentation:%s" % (cie_address + offset, cie_augmentation)
    offset = offset + len(cie_augmentation) + 1

    print "%08x CIE Code Alignment Factor:%d" % (cie_address + offset, cie_code_alignment_factor)
    offset = offset + code_alignment_factor_size

    print "%08x CIE Data Alignment Factor:%d" % (cie_address + offset, cie_data_alignment_factor)
    offset = offset + data_alignment_factor_size

    print "%08x CIE Return Address Register:%d" % (cie_address + offset, cie_return_address_register)
    offset = offset + return_address_register_size

    return 0

# Frame Description Entry
def parse_FDE(fde_address):
    return 0

class CIEParser:
    def __init__(self, ea):
        self.ea = ea
        self.ci_length = 0
        self.ci_extented_length = -1
        self.ci_id = 0
        self.ci_version = 1
        self.ci_augmentation = ""
        self.ci_code_alignment_factor = 1
        self.ci_data_alignment_factor = 1
        self.cie_initial_instructions = 1
        self.cie_return_address_register = 1

    def parse(self):
        pass
    def dump(self):
        pass

class FDEParser:
    def __init__(self, ea):
        self.ea = ea

    def parse(self):
        pass

    def dump(self):
        pass

class ExceptionFrameParser:
    def __init__(self, eh_frame_section_ea):
        self.eh_frame_ea = eh_frame_section_ea

    def parse(self):
        pass

    def dump(self):
        pass

class ExceptionFrameHdrParser:
    def __init__(self,eh_frame_hdr_section_ea):
        self.ea = eh_frame_hdr_section_ea

    def parse(self):
        pass
        
sel = SegByName(".eh_frame")
if sel == BADADDR:
    print "Not find .eh_frame section!"
else:
    seg_ea = SegByBase(sel)
    print ".eh_frame section address:0x%08x" % seg_ea

    print Dword(seg_ea)
    parse_CIE(seg_ea)