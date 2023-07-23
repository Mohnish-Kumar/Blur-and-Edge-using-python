# Image Filter Effects

This project provides Python scripts to apply two different image filter effects to an input image using the Python Imaging Library (PIL). The applied filter effects are Box Blur and Find Edges.

## Prerequisites

Before running the scripts, ensure you have the following:

1. Python installed on your system.
2. The Python Imaging Library (PIL), which can be installed using the following command:
   ```
   pip install pillow
   ```

## How to Use

1. Clone or download this repository to your local machine.

2. Place the image you want to apply the filter to in the same directory as the script files (`blur.py` and `edges.py`).

3. Open a terminal or command prompt and navigate to the directory where the scripts are located.

### Applying Box Blur Filter

To apply the Box Blur filter, run the following command:
```
python blur.py
```
The filtered image will be saved as "blurred.bmp" in the same directory.

### Applying Find Edges Filter

To apply the Find Edges filter, run the following command:
```
python edges.py
```
The filtered image will be saved as "edges.bmp" in the same directory.

Please note that the applied filter effects will be different based on whether the input image is in portrait or squared format. If the image is in portrait or squared format, it will be rotated by -90 degrees before applying the filter.

## Example

Suppose you have an input image named "input.jpeg." You would place this image in the same directory as the scripts, then run the desired script (blur.py or edges.py) based on the filter effect you want to apply. The filtered image will be generated and saved in the same directory.

Happy image filtering! 😄
