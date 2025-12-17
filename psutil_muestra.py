import psutil

for p in psutil.process_iter(['pid', 'name', 'nice']):
    try:
        print(f"PID: {p.info['pid']:<6} "
              f"Nombre: {p.info['name']:<25} "
              f"Prioridad (nice): {p.info['nice']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
