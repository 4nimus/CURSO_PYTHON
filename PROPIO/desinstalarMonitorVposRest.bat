@echo off
VposTest\winsw stop VposTest\winsw.xml
VposTest\winsw uninstall VposTest\winsw.xml
echo Servicio de monitoreo de VPos Rest desinstalado, el mismo no debe estar presente ni en ejecucion.{line.separator}pause
