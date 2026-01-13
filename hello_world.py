""" This is a minimal file to test the blend_converter's basics. """


def hello_world():

    import bpy

    print("Hello Blender", bpy.app.version_string)

    from blend_converter.blender import bpy_utils

    print("The scene has the next objects:")

    for object in bpy_utils.get_view_layer_objects():
        print(object.name_full)


def is_using_terminal():
    return not {'PROMPT', 'TERM_PROGRAM', 'TERM', 'TERMINAL_EMULATOR'}.isdisjoint(os.environ)


def pause():

    print()

    if os.name == 'nt':
        os.system('pause')
    else:
        input("Press Enter to exit.")


if __name__ == '__main__':

    import os
    import uuid
    import tempfile

    from blend_converter.blender import Blender
    from blend_converter import common
    from blend_converter import utils

    blender_executable = utils.get_blender_executable()

    if blender_executable is None:

        message = (
            "Blender executable not found."
            "\n" "Set blender_executable to your Blender's executable path."
            "\n" r"E.g.: blender_executable = r'C:\blender\blender-5.0.1-windows-x64\blender.exe'"
        )

        utils.print_in_color(utils.get_color_code(240, 18, 18, 31, 29, 29), message)

        if not is_using_terminal():
            pause()

        raise SystemExit(0)


    blender = Blender(blender_executable)

    program = common.Program(
        blend_path = '',
        result_path = '',
        blender_executable = '',
        report_path = os.path.join(tempfile.tempdir, uuid.uuid1().hex + '.json')
    )

    program.run(blender, hello_world)

    program.execute()


    if not is_using_terminal():
        pause()
