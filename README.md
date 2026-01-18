[`blend_converter`](https://github.com/unwave/blend_converter) is a Python library for automating Blender's data conversion. Suitable for game development.


#### Features:

* Modular and customizable.
    * Made for programmatic configurations.
* Shader agnostic texture baking.
    * Converting shaders to use a single Principled BSDF.
* Auto UV unwrapping and packing.
    * Optionally using external solutions.
* Simplified deform armature creation and action baking.
    * Bendy bones to normal bones conversion.
* Apply modifiers with shape keys.
    * Handles position sensitive topology modifiers.
* In-engine import handling.
    * Unreal Engine Python remote execution.
* GUI and parallel execution.
    * See the status and reconvert.
* Conversion inspection.
    * Find where things went wrong.


#### Install:

1. Download and Install Python: https://www.python.org/downloads/

    * Preferably enable the Long Paths on Windows during the installation.

2. Ensure you have Blender installed: https://www.blender.org/download/

    * Note the location of the executable file.
        * E.g: `C:\blender\blender-5.0.1-windows-x64\blender.exe`

3. Install `blend_converter`:

    * Use for a stable version: `pip install blend_converter`

        **OR**

    * Use for a newest unstable version: `pip install git+https://github.com/unwave/blend_converter`

4. Ensure the basics are working.

    * Download and run the `hello_world.py` file from this repository.
    * If the script fails to find the Blender executable specify its manually by assigning `blender_executable` variable.


##### Optional, but highly recommended external solutions:

**Windows only.** *(If you know how to make them work on Linux or Mac — let me know)*


* [Legacy UV Packer](https://www.uv-packer.com/) for efficient UV packing.

    * Download http://web.archive.org/web/20240203123438/https://www.uv-packer.com/wp-content/uploads/UV-Packer-Blender_Windows_1.4.0.zip and https://github.com/3d-io/uvpacker-blender-addon/releases/download/1.4.0/UV-Packer-Blender_Add-on_1.4.0.zip and put the files from the both archives into `C:\Users\user\AppData\Local\Programs\Python\Python314\Lib\site-packages\blend_converter\external\uv_packer`
    * For Blender 5.0+ replace `__init__.py` file with: https://gist.github.com/unwave/f37db385e677ea53b45a977d9adf7c79

* [Ministry Of Flat](https://www.quelsolaar.com/ministry_of_flat/) for UV auto unwrapping.

    *  Download https://www.quelsolaar.com/MinistryOfFlat_Release.zip and extract the files into `C:\Users\user\AppData\Local\Programs\Python\Python314\Lib\site-packages\blend_converter\external\ministry_of_flat`.

* [V-HACD](https://github.com/kmammou/v-hacd) convex decomposition for creating optimized collision shapes.

    *  Download https://github.com/kmammou/v-hacd/archive/refs/tags/v4.1.0.zip, locate the `TestVHACD.exe` file and place into `C:\Users\user\AppData\Local\Programs\Python\Python314\Lib\site-packages\blend_converter\external\vhacd`


#### Update:

* Use: `pip install --upgrade blend_converter`

#### Usage:

* See https://github.com/unwave/blend_converter_template.
