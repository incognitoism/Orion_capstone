import sys
from pe_scanner import analyze_pe
from elf_scanner import analyze_elf


def identify_file(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(4)
        if magic_bytes.startswith(b'\x7fELF'):
            return 'ELF'
        elif magic_bytes.startswith(b'MZ'):
            return 'PE'
        else:
            return 'Unknown'
        
if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python scanner.py <file_path>')
    sys.exit(1)
    
    file_path = sys.argv[1]
    file_type = identify_file(file_path)
    print(f'File type: {file_type}')
    
    if file_type == 'ELF':
      analyze_elf(file_path)
    elif file_type == "PE":
      analyze_pe(file_path)
    else:
        print("🚨 Unknown file format!")