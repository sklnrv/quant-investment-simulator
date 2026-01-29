Set WshShell = CreateObject("WScript.Shell")
' Obtiene la ruta de la carpeta donde está este script
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
' Cambia el directorio de trabajo a esa carpeta
WshShell.CurrentDirectory = strPath
' Ejecuta el archivo .bat en modo oculto (0)
WshShell.Run chr(34) & "Ejecutar_Analizador.bat" & chr(34), 0
Set WshShell = Nothing