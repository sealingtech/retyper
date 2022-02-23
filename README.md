# Re-Typer
Repo for "Re-Typing" scripts.

Re-Typer takes an input file and types it out. This is useful incases where you can't copy and paste or have network access to transfer a file.

## Common Usecase
- Copying code/scripts/data into a vsphere VM console

## Usage
`user@host:~ python3 retyper.py`
1. Configure the script to point to the \*.txt containing your source data.
2. Execute the script and **quickly** click into the active window you want the data re-typed into.

**NOTE:** You can tune the startup and interline delay if you need.

## Issues:
**Win10 (pure-python) --> nano:Ubuntu 16:VMware VM console:Firefox == **👎
- UPPERCASE and "(" or ")" has seen being omitted by the 'pure-python' script, when the receiving window is VMware vsphere VM console open in the browser.

**Win10 (win-api) --> nano:Ubuntu 16:VMware VM console:Firefox == **👍

**Win10 (win-api) --> nano:Ubuntu 20:WSL2 == **👎
- The retyped version inserts many unecessary returns causing many breaks in code.
