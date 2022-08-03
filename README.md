# Geometry Dash Texture Extractor
An automated tool made with Python, that separates and extracts every single texture on Geometry Dash. In total it extracts 14.765 different textures!

![image](https://cdn.discordapp.com/attachments/667421252423516197/1004492529439342632/unknown.png)

# Usage

First you will need Pillow. Download it with pip:

```sh
pip install pillow
```
Now download the ``main.py`` file that is on this repo, or just copy and paste the code, and run it.

(If it says that it couldn't find an import, download it with pip accordingly.)

When you run the script, it will automatically check your operating system and use the default path for Geometry Dash downloaded via Steam.

But if you have installed Geometry Dash elsewhere, you can change it by putting the path on the command line arguments:

```sh
python3 main.py path/to/your/geometry/dash/directory
```



**READ THIS BEFORE EXECUTING THE SCRIPT!**

After running, it will IMEDIATELLY create a new folder called "extracted" on the same directory where the executed file is, and then start extracing and copying all the textures to that folder.

In the console, will appear every texture file name, and their properties.

This can take a while, depending on the power of your computer.

After completing, there should be 14.765 .png files on the "extracted" folder.

# What I haven't tested

- I haven't tested this script in Linux and MacOS. Only on Windows 10.
- I only tested with Geometry Dash with vanilla textures. If you have a texture pack, maybe it will also work?

If you encounter an bug, please report it!
