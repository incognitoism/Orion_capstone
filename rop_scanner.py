from capstone import *

def scan_rop_gadgets(binary_data):
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    print("\n[🔍 Scanning for ROP Gadgets]")

    for i in md.disasm(binary_data, 0x1000):
        if "ret" in i.mnemonic or "jmp" in i.mnemonic:
            print(f"🚨 Found ROP Gadget at {hex(i.address)}: {i.mnemonic} {i.op_str}")

    print("\n✅ ROP Gadget Scan Complete!")
