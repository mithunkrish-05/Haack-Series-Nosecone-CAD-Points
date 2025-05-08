# Haack-Series-Nosecone-CAD-Points

A simple Python command-line tool to generate axisymmetric body profiles using the Sears‑Haack or advanced Haack series (including Von Karman, LV‑Haack, Tangent series, or custom C parameter), plot the results, and save coordinates to an Excel file.

## Features

* **Interactive CLI**: Prompt for body length, radius, series type, number of points, mirroring, output directory, and filename.
* **Profiles Supported**:

  * **Simple Sears‑Haack**
  * **Advanced Haack Series**:

    * Von Karman (C=0)
    * LV‑Haack (C=1/3)
    * Tangent series (C=2/3)
    * Custom C value
* **Plotting**: View profiles with Matplotlib (`axis('equal')` for true aspect ratio).
* **Data Export**: Saves (x, y, 0) coordinates to an Excel (`.xlsx`) file via `openpyxl`.
* **Environment Assurance**: Auto-installs missing dependencies at runtime.

## Requirements

* Python 3.7+
* Dependencies: `numpy`, `scipy`, `matplotlib`, `openpyxl`

The script will attempt to install any missing package automatically via `pip`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/haack-series-generator.git
   cd haack-series-generator
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .\.venv\Scripts\activate    # Windows
   ```

## Usage

Run the script:

```bash
python generate_body.py
```

You will be prompted for:

1. **Body length (L)** (e.g. `0.28`)
2. **Maximum radius (R)** (e.g. `0.0525`)
3. **Series type**: Simple Sears‑Haack `[S]` or Advanced Haack `[A]`
4. If *Simple*: number of plot points (e.g. `100`)
5. If *Advanced*: choose preset (1–4) or enter custom C
6. *Advanced* only: mirror around midpoint? `[y/N]`
7. number of plot points (e.g. `200`)
8. **Output directory** (relative; default `./output`)
9. **Excel filename** (default `body_points.xlsx`)

After answering, the script will:

* Plot the profile (`plt.show()`).
* Create the output directory if needed.
* Save coordinates to the specified Excel file.
* Print the path:

  ```text
  Data saved to ./output/body_points.xlsx
  ```

## Example

```text
$ python generate_body.py
Please enter the Length of the body [0.28]: 0.5
Please enter the Maximum Radius of the body [0.01]: 0.02
Body Type: Simple Sears-Haack [S] or Advanced Haack Series [A]? s
Number of plot points [100]: 150
Relative output directory (will be created if needed) [./output]: profiles
Excel filename [body_points.xlsx]: haack_profile.xlsx
Data saved to profiles/haack_profile.xlsx
```
