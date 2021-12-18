
----------------------------------------------------------------------------------------------------
                                            MAME BEZEL GENERATOR

Creates directories matching ROM names in MAME artwork directory and populates the new directories
with lay files that point to one single artwork file.

Information:
    A. Please backup your MAME installation before using this program.
    B. Please do not modify the included lay file unless you keep tag <image file> unaltered or you
       know what you are doing.
    C. Please ensure artwork png specified is called "mame_bezel_generator.png".
    D. Creating Theme Directories recommended for almost instantly changing the bezel accross all
       roms. To easily change between themes include the following in a directory and configure
       a configuration file:
        1. default.lay
        2. mame_bezel_generator.png
        3. mame_bezel_generator_configuration.txt (This file can be called anything you like).

Configuration File:
    1. Enter full path to desired .lay file.
    2. Enter full path to desired image file.
    3. Enter MAME installation artwork directory path.
    4. Enter a MAME BIOS directory path that contasins only BIOS files (Crucial for distinguishing
       between ROMs and BIOSs so that artwork is only generated for ROMs).
    5. Finally enter MAME installation ROM directory path.

Example Configuration File:
    LAY: C:\default.lay
    IMG: C:\mame_bezel_generator.png
    DIR_ART: C:\Programs\MAME\artwork
    DIR_BIOS: C:\Archives\MAME\BIOS_v0.237\MAME (bios-devices)\MAME (bios-devices)
    DIR_ROM: D:\Programs\MAME\roms

Create/Change Bezels For all ROMS:
    mame_bezel_generator.exe -c any_configuration_file_name.txt

Command Line Arguments:
    -c                  Specifies configuration file [-c file].
    --make-defalut-lay  Creates the default lay file for this program (Recommended if missing or overwritten).
    -h                  Displays a help message

----------------------------------------------------------------------------------------------------

Compile From Source:
    pyinstaller -F ./mame_bezel_generator.py -i ./anyicon.ico

Compile From Source With UAC For Elevated Privilege:
    pyinstaller --uac-admin -F ./mame_bezel_generator.py -i ./anyicon.ico

