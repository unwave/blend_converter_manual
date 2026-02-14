As the Python code is the configuration, in order to use `blend_converter` features or add yours, you have to use a separate Python package as an entry point.


#### Template

The reference is: https://github.com/unwave/blend_converter_template.

The template guides and utilizes `blend_converter` to create an automation system that finalizes a model and exports it. Converting into meshes, applying modifiers, making UV layouts, baking materials, converting the rigs into deform-bone-only, etc. And then uses the Unreal Engine's Python remote execution to export as an FBX and import into Unreal. Allowing for a stage-less asset creation.

I recommend setting up a repository right away. The template can also be a part of the game's repository.

* Install Git: https://git-scm.com/install
* Choose a folder: `cd /d C:\repo`
* Clone the template: `git clone https://github.com/unwave/blend_converter_template`


#### File hierarchy

An Unreal Engine hierarchy.

```
project_1
    blends
        static
            static_mesh_1
                static_mesh_1.blend
            static_mesh_2
                static_mesh_2.blend
        skeletal
            skeletal_mesh_1
                skeletal_mesh_1.blend
            skeletal_mesh_2
                skeletal_mesh_2.blend
        rigs
            skeletal_mesh_1
                skeletal_mesh_1.blend
            skeletal_mesh_2
                skeletal_mesh_2.blend
        animation
            skeletal_mesh_1
                idle
                    idle.blend
                walk
                    walk.blend
                jump
                    jump.blend
            skeletal_mesh_2
                idle
                    idle.blend
                walk
                    walk.blend
                jump
                    jump.blend
    intermediate
        blends
            static
            skeletal
        unreal
            skeletal
            static
            animation
```

The `intermediate` folder should be excluded from the version control.


#### Sample blends

To test the converter download this `blends` folder and merge with `C:\repo\blend_converter_template\blends`.

First you have to bake the blend files and then export it.


#### A configuration for the configuration

If you want to take advantage of the template repository being updated without modifying it yourself you can hook it up by using another configuration file for the template itself by changing source folders and common settings. See the `bct_starter.py` file.

* Replace paths in `bct_starter.py` and make sure that in the paths `STATIC_BLEND` and `SKELETAL_BLEND` have blend files.

* Create a shortcut (Right Click -> New -> Shortcut on Windows) with the location: `py C:\user_data\project_1\bct_starter.py BAKE_STATIC BAKE_SKELETAL` where `BAKE_STATIC` and `BAKE_SKELETAL` are the names of the programs specified in `bct_starter.py`.
