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

## Usage

Run the script with an image file as an argument:

```
python main.py path/to/your/image.png
```

or

```
python main.py path/to/your/image.svg
```

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

## Requirements

- Python 3.8+
- Pillow
- numpy
- colorama

See `environment.yml` for specific version requirements.