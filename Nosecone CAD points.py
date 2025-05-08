# Downloading and Importing libraries
import sys, subprocess

def ensure(pkg):
    try:
        __import__(pkg)
    except ImportError:
        print(f"Installing missing package: {pkg}…")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

for pkg in ("numpy","scipy","matplotlib","openpyxl","os"):
    ensure(pkg)
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import openpyxl
def sears_haack(x, L, R):
    return R * (4 * (x/L) * (1 - x/L))**(3/4)

def haack_series(x, L, R, C):
    t = np.arccos(1 - 2*x/L)
    return (R/np.sqrt(np.pi)) * np.sqrt(t - 0.5*np.sin(2*t) + C*(np.sin(t)**3))

def get_float(prompt, default=None):
    while True:
        s = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ")
        if not s and default is not None:
            return default
        try:
            return float(s)
        except ValueError:
            print(" ↳ please enter a number")

# 1) User inputs
L  = get_float("Please enter the Length of the body")
R  = get_float("Please enter the Maximum Radius of the body")
tp = input("Body Type: Simple Sears-Haack [S] or Advanced Haack Series [A]? ").strip().lower()

# 2) Branch on type
if tp == 's':
    n = int(get_float("Number of plot points"))
    x = np.linspace(0, L, n)
    y = sears_haack(x, L, R)

elif tp == 'a':
    print("Choose advanced profile:")
    print(" 1) Von Karman (C=0)")
    print(" 2) LV-Haack   (C=1/3)")
    print(" 3) Tangent    (C=2/3)")
    print(" 4) Custom C")
    choice = input("Select 1–4: ").strip()
    if choice == '1':
        C = 0.0
    elif choice == '2':
        C = 1/3
    elif choice == '3':
        C = 2/3
    elif choice == '4':
        C = get_float("Enter your custom C value")
    else:
        raise SystemExit("Invalid choice.")

    mirror = input("Replicate around midpoint? [y/N]: ").strip().lower() == 'y'
    n = int(get_float("Number of plot points"))
    
    if mirror:
        n2 = n // 2
        x1 = np.linspace(0, L/2, n2)
        y1 = haack_series(x1, L, R, C)
        x2 = L - x1[::-1]
        y2 = y1[::-1]
        x = np.concatenate([x1, x2[1:]])
        y = np.concatenate([y1, y2[1:]])
    else:
        x = np.linspace(0, L, n)
        y = haack_series(x, L, R, C)

else:
    raise SystemExit("Invalid body type selected.")

# 3) Plot
plt.figure()
plt.plot(x, y, '-o')
plt.axis('equal')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Axisymmetric Body Profile")
plt.grid(True)
plt.show()

# 4) Save to Excel (relative path)
out_dir = input("Relative output directory (will be created if needed) [./output]: ").strip() or "./output"
out_fn = input("Excel filename [body_points.xlsx]: ").strip() or "body_points.xlsx"
if not out_fn.lower().endswith(".xlsx"):
    out_fn += ".xlsx"
os.makedirs(out_dir, exist_ok=True)
full_path = os.path.join(out_dir, out_fn)

# Build workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'x'
sheet['B1'] = 'y'
sheet['C1'] = 'z'
for i, (xi, yi) in enumerate(zip(x, y), start=2):
    sheet[f'A{i}'] = xi
    sheet[f'B{i}'] = yi
    sheet[f'C{i}'] = 0.0

wb.save(full_path)
print(f"Data saved to {full_path}")
