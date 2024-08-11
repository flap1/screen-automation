# Screen Automation Project

This project automates the process of taking screenshots and clicking specific locations on the screen. It also includes the functionality to convert the captured screenshots into a single PDF file.

## Prerequisites

- [Rye](https://rye-up.com/) is used for environment management. Make sure you have Rye installed.

## Setup

1. **Sync the environment using Rye**:

   ```bash
   rye sync
   ```

   This command installs all necessary dependencies and sets up the environment.

## Usage

### 1. Get Click Position

To obtain the coordinates of a click position on the screen, run:

```bash
rye run python get_click_pos.py
```

This script will allow you to click on a location, and it will output the x and y coordinates.

### 2. Take Screenshots

To take screenshots and save them in the `out` directory, run:

```bash
rye run python repeat_screenshot.py --start_num 1 --count 10
```

- `--start_num`: The starting number for the screenshot filenames (e.g., 1 for `0001.png`).
- `--count`: The number of screenshots to take.

The screenshots will be saved as `0001.png`, `0002.png`, ..., up to `0010.png` in the `out` directory.

### 3. Convert PNGs to PDF

To convert all PNG files in the `out` directory into a single PDF file, run:

```bash
rye run python convert_to_pdf.py
```

This will generate a PDF named `output.pdf` containing all the screenshots.

## Additional Information

- **Environment Management**: Rye is used to manage the Python environment and dependencies.
- **Output Directory**: All screenshots are saved in the `out` directory.
- **PDF Generation**: The generated PDF file is named `output.pdf`.

Feel free to modify the scripts or add additional functionality as needed.
