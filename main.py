mac_path=str(input(""))
target="海外事業推進室"

def remove(mac_path,target):
    if target in mac_path:
      return mac_path.split(target,1)[-1]
    else:
      print(f"---------------------")
      print(f"路徑可能有錯，請檢查")
      return mac_path

new_mac_path =  remove(mac_path,target)

def mac_to_windows_path(new_mac_path):
    windows_path = new_mac_path.replace("/", "\\")
    return windows_path


windows_path = mac_to_windows_path(new_mac_path)
print(f"---------------------")
print(f"Windows路徑: G:\共有ドライブ\海外事業推進室{windows_path}")