from elftools.elf.elffile import ELFFile

def analyze_elf(file_path):
    with open(file_path, "rb") as f:
        elf = ELFFile(f)
        print("\n[🔍 ELF Sections]")
        for section in elf.iter_sections():
            print(f"📂 {section.name} - Address: {hex(section['sh_addr'])} - Flags: {section['sh_flags']}")

    print("\n✅ ELF Analysis Complete!")

