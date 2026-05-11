@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat" -arch=x64 -host_arch=x64
call "C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent\.venv\Scripts\python.exe" -m pip install -r "C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent\requirements.txt"
