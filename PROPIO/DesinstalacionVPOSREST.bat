@echo off
del /q "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
chcp 1252
taskkill /F /IM javaw.exe
echo .
echo .
echo .
echo Fin de la desinstalacion.
echo .
pause
