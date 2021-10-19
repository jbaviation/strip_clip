import cv2 as cv
import numpy as np
import sys
import os


def read_clip(path):
    # Create clip object
    clip = cv.VideoCapture(path)

    # Check if output folder exists
    if not os.path.isdir('VideoClips'):
        os.mkdir('VideoClips')

    if clip.isOpened():
        frame_count = 0  # initialize counter

        # Get clip details
        fps, frame_size, frame_list, tot_frames = get_minute_frames(clip)

        # Initialize new_clip and start loop
        new_clip = None
        while True:
            # Look for new file generation
            if frame_count in frame_list:
                _ = new_clip.release() if new_clip is not None else 0
                filename = f'VideoClips/{frame_count}Frame.mp4'
                new_clip = cv.VideoWriter(filename,
                                          cv.VideoWriter_fourcc(*'mp4v'),
                                          int(fps),
                                          frame_size)

            # Read current frame
            pass_, frame = clip.read()

            # If the next frame exists, track it
            if pass_:
                # Track progress and save frame to new clip
                sys.stdout.write('\rCompleted: {:.2%}'.format(frame_count/tot_frames))
                sys.stdout.flush()
                new_clip.write(frame)

                frame_count += 1
            else:
                break

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
    # seconds = length % 60

    # Get frame size
    frame_width = clip_obj.get(3)
    frame_height = clip_obj.get(4)
    frame_size = int(frame_width), int(frame_height)

    # Find frame at each minute increment
    minute_frames = [0]
    for minute in np.arange(1, minutes+1):
        minute_frames.append(int(fpm*minute))

    return fps, frame_size, minute_frames, number_frames


if __name__ == '__main__':
    if len(sys.argv) > 1:  # if argument is passed, use it
        filepath = os.path.normpath(sys.argv[1])
    else:   # otherwise look for file in the current directory
        filepath = os.path.normpath('3148_56041_1630792151_FishEye.mov')

    # Make sure file exists
    if not os.path.isfile(filepath):
        raise FileExistsError(f'{filepath} DOES NOT EXIST')

    import time
    start = time.time()
    read_clip(filepath)  # read and parse the new files
    print(f'\nTime Elapsed: {(time.time()-start)/60} Minutes')

    # from line_profiler import LineProfiler
    # lp = LineProfiler()
    # lp_wrapper = lp(read_clip)
    # lp_wrapper(filepath)
    # lp.print_stats()
