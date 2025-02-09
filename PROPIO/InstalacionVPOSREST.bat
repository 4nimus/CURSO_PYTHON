del VposREST.vbs
echo Dim objWSHShell : Set objWSHShell = CreateObject("WScript.Shell") > VposREST.vbs
echo objWSHShell.CurrentDirectory = "%~dp0" >> VposREST.vbs
echo objWSHShell.Run "VposREST",0,True >> VposREST.vbs
copy VposREST.vbs "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
chcp 1252
@echo off
echo .
echo .
echo Fin de la instalacion.
echo Puede cerrar esta ventana si queda abierta.
echo .
VposREST.vbs
