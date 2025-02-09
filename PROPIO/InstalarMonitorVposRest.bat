@echo off
powershell -Command "(gc VposTest\basewinsw.xml) -replace '@path@', '%~dp0' | Out-File -encoding ASCII VposTest\winsw.xml"
VposTest\winsw install VposTest\winsw.xml
VposTest\winsw start VposTest\winsw.xml
VposTest\winsw status VposTest\winsw.xml
echo Servicio de monitoreo de VPos Rest instalado, el mismo debe estar en ejecucion.{line.separator}pause
