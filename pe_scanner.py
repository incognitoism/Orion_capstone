import pefile

def analyze_pe(file_path):
    pe = pefile.PE(file_path)
    print("\n[🔍 PE (Windows) Imports]")
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print(f"📂 {entry.dll.decode()}")
        for imp in entry.imports:
            print(f"  - {imp.name.decode() if imp.name else 'Unknown'}")

    print("\n✅ PE Analysis Complete!")
