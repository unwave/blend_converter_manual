import os
import sys


## importing the template module
CONVERTER_ROOT = r'C:\repo\blend_converter_template\converter'
""" https://github.com/unwave/blend_converter_template """

sys.path.append(os.path.dirname(CONVERTER_ROOT))

from converter import app  # type: ignore

from blend_converter import common

programs = app.get_program_paths()  # type: ignore

def main(*args):
    app.main(args)


## settings
BLENDER_4_5 = r"C:\blender\blender-4.5.6-windows-x64\blender.exe"
""" https://www.blender.org/download/lts/ """

ROOT = r'C:\user_data\project_1'
""" This is your project's working directly. """

SKELETAL_BLEND = os.path.join(ROOT, 'blends', 'skeletal')
STATIC_BLEND = os.path.join(ROOT, 'blends', 'static')
RIG_BLEND = os.path.join(ROOT, 'blends', 'rigs')
ANIM_BLEND = os.path.join(ROOT, 'blends', 'animation')

INTERMEDIATE_STATIC_BLEND = os.path.join(ROOT, 'intermediate', 'blends', 'static')
INTERMEDIATE_SKELETAL_BLEND = os.path.join(ROOT, 'intermediate', 'blends', 'skeletal')

INTERMEDIATE_UNREAL_STATIC = os.path.join(ROOT, 'intermediate', 'unreal', 'static')
INTERMEDIATE_UNREAL_SKELETAL = os.path.join(ROOT, 'intermediate', 'unreal', 'skeletal')
INTERMEDIATE_UNREAL_ANIM = os.path.join(ROOT, 'intermediate', 'unreal', 'animation')


TEXEL_DENSITY = 256
MAX_RESOLUTION = 1024


## conversion programs definitions
BAKE_STATIC = common.Program_Definition(
    *programs['static'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = STATIC_BLEND,
        texel_density = TEXEL_DENSITY,
        max_resolution = MAX_RESOLUTION,
        result_root = INTERMEDIATE_STATIC_BLEND
    )
)


BAKE_SKELETAL = common.Program_Definition(
    *programs['skeletal'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = SKELETAL_BLEND,
        texel_density = TEXEL_DENSITY,
        max_resolution = MAX_RESOLUTION,
        result_root = INTERMEDIATE_SKELETAL_BLEND
    )
)


UE_STATIC = common.Program_Definition(
    *programs['ue_static'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = INTERMEDIATE_STATIC_BLEND
    )
)


UE_SKELETAL = common.Program_Definition(
    *programs['ue_skeletal'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = INTERMEDIATE_SKELETAL_BLEND
    )
)


MAKE_RIG = common.Program_Definition(
    *programs['rig'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = INTERMEDIATE_SKELETAL_BLEND,
        result_root = RIG_BLEND,
    )
)


UE_ANIMATION = common.Program_Definition(
    *programs['ue_animation'],
    kwargs = dict(
        blender_executable = BLENDER_4_5,
        root = ANIM_BLEND,
        result_root = INTERMEDIATE_UNREAL_ANIM,
    )
)


## entry point
if __name__ == '__main__':
    main(*(globals()[a] for a in sys.argv[1:]))