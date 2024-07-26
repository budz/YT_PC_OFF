"""
YT_PC_OFF: Automatic PC Shutdown on YouTube Video Completion

Purpose:
YT_PC_OFF is a handy tool that monitors YouTube video playback in your browser and automatically shuts down your PC when the video finishes. 
This script is ideal for those late-night viewing sessions when you want your computer to power off after your video ends.

How to Use:
1. Ensure you have Python and Flask installed on your system. If not, you can install Flask using pip:
   pip install flask

2. Create a Python script (flask_yt.py) to set up a local server that listens for the signal from the browser.
   
3. Start the local server by running the Python script:
   python flask_yt.py

4. Create a bookmarklet in your browser with the JavaScript code.

6. Navigate and play a YouTube video in your browser and click the bookmarklet to inject the monitoring script.

7. When the YouTube video ends, the script will send a signal to the local server, triggering the PC shutdown command.

NOTE: Use this tool with caution, as it will automatically shut down your computer when a YouTube video finishes playing.
"""
