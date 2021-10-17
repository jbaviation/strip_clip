import cv2 as cv
import numpy as np
import os


def read_clip(path):
    # Create clip object
    clip = cv.VideoCapture(path)

    if clip.isOpened():
        frame_count = 0  # initialize counter

        # Get clip details
        fps, frame_size, frame_list = get_minute_frames(clip)

        # Initialize new_clip and start loop
        new_clip = None
        while True & (frame_count<=300):
            # Look for new file generation
            if frame_count in frame_list:
                _ = new_clip.release() if new_clip is not None else 0
                filename = f'VideoClips/{frame_count}Frame.mov'
                new_clip = cv.VideoWriter(filename,
                                          cv.VideoWriter_fourcc('M','J','P','G'),
                                          int(fps),
                                          frame_size)

            # Read current frame
            pass_, frame = clip.read()

            # If the next frame exists, track it
            if pass_:
                # Save frame to new clip
                print(f'Storing frame {frame_count}')
                new_clip.write(frame)

            frame_count += 1

        clip.release()
        new_clip.release()

    cv.destroyAllWindows()


def get_minute_frames(clip_obj):
    # Get frames/minute
    fps = float(clip_obj.get(cv.CAP_PROP_FPS))
    fpm = fps * 60

    # Find total number of frames
    number_frames = int(clip_obj.get(cv.CAP_PROP_FRAME_COUNT))

    # Find clip length
    length = number_frames / fps
    minutes = int(length/60)
    seconds = length % 60

    print(f'fps = {fps}')
    print(f'frames = {number_frames}')
    print(f'length = {length}')
    print(f'minutes= {minutes}')
    print(f'seconds= {seconds}')

    # Get frame size
    frame_width = clip_obj.get(3)
    frame_height = clip_obj.get(4)
    frame_size = int(frame_width), int(frame_height)

    # Find frame at each minute increment
    minute_frames = [0]
    for minute in np.arange(1, minutes+1):
        minute_frames.append(int(fpm*minute))

    return fps, frame_size, minute_frames


if __name__ == '__main__':
    read_clip(r'C:\Users\jborman\Documents\Data\3148_56041_1630792151_FishEye.mov')

