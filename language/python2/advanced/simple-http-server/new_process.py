import SimpleHTTPServer
import SocketServer
import subprocess

print("Hello from before subprocess call")
# subprocess.call() waits for the process to return
#subprocess.call(["python", "-m", "SimpleHTTPServer", "8000"])

# subprocess.Popen does NOT wait for the executable to return. It is difficult to shut the process down after it has been started since there is no shell
subprocess.Popen(["python", "-m", "SimpleHTTPServer", "8000"])

# Setting shell=True does not make the process any easier to shut down, so don't do it
#subprocess.Popen("python -m SimpleHTTPServer 8000", shell=True)
print("Hello from after subprocess call")