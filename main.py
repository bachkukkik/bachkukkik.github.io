from pyscript import display
import datetime
now = datetime.datetime.now()
display(f"Hello from PyScript! The current time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")