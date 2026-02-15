#### The Python code is the configuration

In order to use `blend_converter` and add yours features, you have to write a separate Python module that serves as an entry point.


#### Template

The reference for the configuration is: https://github.com/unwave/blend_converter_template.

The template utilizes `blend_converter` to create an automation system that finalizes a model and exports it. Converting into meshes non-mesh objects, applying modifiers, creating UV layouts, baking materials, converting armatures into deform-only, etc. And then exports as an FBX or glTF and can use the Unreal Engine's Python remote execution to import into Unreal. This allows for a stage-less asset creation, when you are able to continuously iterate on the blend files.

As you can add your own functionality to the template and monkey patch `blend_converter`, there is no hard distinction between `blend_converter` and your configuration.

It is recommended to set up a version control repository right away. The template can also be a part of the game's repository.

* Install Git: https://git-scm.com/install
* Choose a folder: `cd /d C:\repo`
* Clone the template: `git clone https://github.com/unwave/blend_converter_template`

You can also just download the template repository without cloning and retaining any prior commit history. As your configuration is expected to be incompatible with the upstream.


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

If you want to take advantage of the template repository being updated upstream without modifying it yourself you can hook it up by using another configuration file for the template itself by changing source folders and common settings. See the `bct_starter.py` file.

* Replace paths in `bct_starter.py` and make sure that in the paths `STATIC_BLEND` and `SKELETAL_BLEND` have blend files.

* Create a shortcut (Right Click -> New -> Shortcut on Windows) with the location: `py C:\user_data\project_1\bct_starter.py BAKE_STATIC BAKE_SKELETAL` where `BAKE_STATIC` and `BAKE_SKELETAL` are the names of the programs specified in `bct_starter.py`.
