import psutil

for p in psutil.process_iter(['pid', 'name']):
    print(p.info)
