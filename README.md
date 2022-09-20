# Convert_mp3_to_wav
                                      ***Important NOTE: IT CAN ONLY BE FOR PYTHON 2.7 ***
This project has step by step instructions that how to convert "mp3 format to wav format" also has python module by which anyone could use two functions acording to their need.
The file "mp3_ to_wav_step_by_step" contain all the libraries and codes that will use in the program (remember the libraries will only work for python 2.7 module)
The "mp3ConvertWav.ipynb" has a method to make a class and user defined functions.
The "p3ConvertWav.py" is the module file.
You can past this module file in the python built-in package and modules folders:
*****
        /usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python37.zip
        /usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7
        /usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload
        /Users/brettmz-admin/Library/Python/3.7/lib/python/site-packages
        /Users/brettmz-admin/dev_trees/grin
        /Users/brettmz-admin/dev_trees/rmdex
        /usr/local/lib/python3.7/site-packages
*****
if  you are using module you can use following commands:
*****
      from mp3ConvertWav import con
          # for just converting without removing previous files type:
      con.convert(**file path***)
      
          # for converting and deleting the previous files type:
      con.cut(**file path***)
      
 ***** This method will convert whole file of mp3 withing a givin folder ******
