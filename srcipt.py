import sys
import binascii
from rich import print

file_magic_numbers = {
  ".jpg": ["ffd8ffdb", "ffd8ffe0", "ffd8ffee", "ffd8ffe1"],
  ".png": ["89504e470d0a1a0a"],
  ".gif": ["474946383761", "474946383961"],
  ".pdf": ["255044462d"],
  ".zip": ["504b0304", "504b0506", "504b0708"],
  ".rar": ["526172211a0700", "526172211a070100"],
  ".7z": ["377abcaf271c"],
  ".tar": ["7573746172202000"],
  ".gz": ["1f8b"],
  ".bz2": ["425a68"],
  ".mp3": ["494433", "fff3", "fff2"],
  ".wav": ["52494646", "57415645"],
  ".avi": ["52494646", "41564920"],
  ".mov": ["000000146674797071742020"],
  ".mp4": ["00000018667479706d703432"],
  ".exe": ["4d5a"],
  ".dll": ["4d5a"],
  ".doc": ["d0cf11e0a1b11ae1"],
  ".xls": ["d0cf11e0a1b11ae1"],
  ".ppt": ["d0cf11e0a1b11ae1"],
  ".docx": ["504b0304"],
  ".xlsx": ["504b0304"],
  ".pptx": ["504b0304"],
  ".iso": ["4344303031"],
  ".flv": ["464c5601"],
  ".swf": ["435753", "465753"],
  ".rtf": ["7b5c72746631"],
  ".bmp": ["424d"],
  ".ico": ["00000100"],
  ".psd": ["38425053"],
  ".sqlite": ["53514c69746520666f726d6174203300"],
  ".nes": ["4e45531a"],
  ".crx": ["43724f6d"],
  ".deb": ["213c617263683e0a"],
  ".rpm": ["edabeedb"],
  ".cab": ["4d534346"],
  ".dmg": ["7801730d626260"],
  ".xml": ["3c3f786d6c20"],
  ".wasm": ["0061736d"],
  ".lepton": ["cf8401"],
  ".flif": ["464c4946"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
  ".lep": ["cf8401"],
  ".swf": ["435753", "465753"],
  ".deb": ["213c617263683e0a"],
  ".webp": ["52494646", "57454250"],
  ".jxl": ["0000000c4a584c200d0a870a"],
  ".wasm": ["0061736d"],
}

if len(sys.argv) < 2:
    print("Usage: [bold][blue]magicid[/blue] [red]<filename>[/red][/bold]")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'rb') as f:
        content = f.read()
        hex_string = binascii.hexlify(content).decode()

    for extension, magic_list in file_magic_numbers.items():
        for magic in magic_list:
            if hex_string.startswith(magic):
                print(f"{filename} is in [bold blue]{extension}[/bold blue] format")
                exit(0)

    print(f"[bold red]could not detemine the type of {filename}[/bold red]")
    exit(1)

except FileNotFoundError:
    print(f"[bold][red]Error[/red]: {filename} not found.[/bold]") 

