"""
YT_PC_OFF: Automatic PC Shutdown on YouTube Video Completion

Purpose:
YT_PC_OFF is a handy tool that monitors YouTube video playback in your browser and automatically shuts down your PC when the video finishes. 
This script is ideal for those late-night viewing sessions when you want your computer to power off after your video ends.

How to Use:
1. Ensure you have Python and Flask installed on your system. If not, you can install Flask using pip:
   pip install flask

2. Create a Python script (flask_yt.py) with the following content to set up a local server that listens for the signal from the browser:
    from flask import Flask
    import os

    app = Flask(__name__)

    @app.route('/video-ended', methods=['GET'])
    def video_ended():
        # Print a message and shutdown the PC
        print("Video has ended. Shutting down the PC...")
        os.system('shutdown /s /t 1')
        return 'Shutting down...', 200

    if __name__ == '__main__':
        app.run(port=5000)

3. Start the local server by running the Python script:
   python flask_yt.py

4. Create a bookmarklet in your browser with the following JavaScript code:
    javascript:(function(){function%20onVideoEnd(){fetch('http://localhost:5000/video-ended');}function%20addVideoEndListener(){const%20video=document.querySelector('video');if(video){video.addEventListener('ended',onVideoEnd);console.log('Listener%20added%20to%20video');}else{console.log('No%20video%20element%20found');}}const%20observer=new%20MutationObserver((mutations)=>{mutations.forEach((mutation)=>{if(mutation.addedNodes.length){addVideoEndListener();}});});observer.observe(document.body,{childList:true,subtree:true});addVideoEndListener();})();

5. Navigate and play a YouTube video in your browser and click the bookmarklet to inject the monitoring script.

6. When the YouTube video ends, the script will send a signal to the local server, triggering the PC shutdown command.

NOTE: Use this tool with caution, as it will automatically shut down your computer when a YouTube video finishes playing.
"""
