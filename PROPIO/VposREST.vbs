Dim objWSHShell : Set objWSHShell = CreateObject("WScript.Shell") 
objWSHShell.CurrentDirectory = "C:\Users\amatute\Documents\GitHub\CURSO_PYTHON\PROPIO\" 
objWSHShell.Run "VposREST",0,True 
