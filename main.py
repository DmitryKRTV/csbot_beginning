import autoit

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)

# autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")

