# py2app

1. open the path of your programe
2. create init files 
   py2applet --make-setup   

3. if dist build path has been created ,your can delete them before your mission.
4. run 
   python setup.py py2app


# pyinstall 

-F, -onefile 打包成一个exe文件

-D, -onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）

-c, -console, -nowindowed 使用控制台，无界面（默认）

-w, -windowed, -noconsole 使用窗口，无控制台

python pyinstaller.py [option] yourprograme.py
  usually you can use -F [/option]
