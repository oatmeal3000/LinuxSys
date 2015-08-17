import os
import signal

os.kill(10471, signal.SIGTERM)

os.kill(10471, signal.SIGUSR1)
