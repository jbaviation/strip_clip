import cv2 as cv
import os


def read_clip(path):
    # Create clip object
    clip = cv.VideoCapture(path)

    if clip.isOpened():
        frame_count = 0  # initialize counter

        while True & (frame_count<=5):
            # Read current frame
            pass_, frame = clip.read()

            # If the next frame exists, track it
            if pass_:
                # Generate filename and save frame
                filename = f"VideoClips/{frame_count}.jpg"
                print(f'Creating {filename}')
                cv.imwrite(filename, frame)

            frame_count += 1

        clip.release()

    cv.destroyAllWindows()


def get_minute_frames(clip_obj):
    # Get frames/sec
    fps = clip_obj.get(cv.CAP_PROP_FPS)

    # Find total number of frames
    number_frames = clip_obj.get(cv.CAP_PROP_FRAME_COUNT)

    # Find clip length
    length = float(number_frames) / float(fps)
    minutes = int(length/60)
    seconds = length % 60


if __name__ == '__main__':
    filepath = [r'C:\Users\jborman\Documents\Data\2019-09-21_19-35-59_000.mov',
                r'C:\Users\jborman\Documents\Data\3148_56041_1630792151_FishEye.mov']
    read_clip(filepath[0])

