archivo = open("test.txt", "w", encoding="utf-8")
archivo.write("a" * 1048576)
archivo.close()