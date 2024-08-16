# ascii-art-generator
Personal Project for making thumbnail and some character for my personal blog and youtube(made by claude)
- This project converts SVG and PNG images to ASCII art.

## Installation

### Using Conda (Recommended)

1. Clone this repository
2. Create and activate the Conda environment:
   ```
   conda env create -f environment.yml
   conda activate ascii_art_converter
   ```

### Manual Installation

If you prefer not to use Conda, you can install the required packages manually:

1. Clone this repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with an image file as an argument:

```
python main.py path/to/your/image.png
```

This will display the ASCII art on the screen and save two versions in the "outputs" folder:
1. A plain text version (without colors) as 'outputs/image_ascii.txt'
2. A colored version (with ANSI color codes) as 'outputs/image_ascii_color.txt'

To specify a custom output file name:

```
python main.py path/to/your/image.png custom_name.txt
```

This will display the ASCII art on the screen and save in the "outputs" folder:
1. The plain text version to 'outputs/custom_name.txt'
2. The colored version to 'outputs/custom_name_color.txt'

## Viewing Colored ASCII Art

The colored version contains ANSI escape codes and may not display correctly in all text editors. Here are some ways to view the colored ASCII art:

1. On Unix-like systems (Linux, macOS), use the `cat` command in the terminal:
   ```
   cat outputs/image_ascii_color.txt
   ```

2. On Windows, use the `type` command in Command Prompt:
   ```
   type outputs\image_ascii_color.txt
   ```
   Or use `Get-Content` in PowerShell:
   ```
   Get-Content outputs\image_ascii_color.txt
   ```

3. Use a text editor that supports ANSI colors, such as Visual Studio Code with the "ANSI Colors" extension.

4. Use specialized ASCII art viewers that support ANSI colors.

Note: The plain text version (without '_color' in the filename) can be opened with any standard text editor.

## Requirements

- Python 3.8+
- Pillow
- numpy
- colorama

See `environment.yml` for specific version requirements.

## Development

If you're developing this project and need to update the environment, you can do so by installing new packages with Conda and then updating the environment file:

```
conda install <package_name>
conda env export > environment.yml
```

To recreate the environment on another machine:

```
conda env create -f environment.yml
```