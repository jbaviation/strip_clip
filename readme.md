# Strip Clip
This project contains a Python script designed to process a video clip into multiple 1-minute clips. When running the script ```strip_clip.py```, the video file will be processed into clips broken down into 1-minute clips.  In order to run this script, follow the installation steps below. 


## Installation & Execution
Required dependencies: <br>
 - [Python (>=3.6)](https://www.python.org/)
 - [Numpy](https://pypi.org/project/numpy/)
 - [OpenCV](https://pypi.org/project/opencv-python/)

Clone this repository, navigate into the directory, either paste the video file into the directory or enter the video filepath as an argument in the python script execution:<br> 
```bash
git clone https://github.com/jbaviation/strip_clip.git
cd strip_clip
python strip_clip.py <path.to.file>  # <path.to.file> is optional
```

And that's it!  The script will run and populate the sub-directory *VideoClips* with minute long clips.
