import warnings
warnings.filterwarnings("ignore")

import streamlit as st
st.set_option('client.showErrorDetails', False)
import streamlit as st
import cv2
import tempfile
import ExerciseAiTrainer as exercise
import time

def main():
    # Page config
    st.set_page_config(page_title='Fitness AI Coach', layout='centered')

    # Title
    st.title('Fitness AI Coach')

    # Sidebar option
    options = st.sidebar.selectbox(
        'Select Option', ('Video', 'WebCam', 'Auto Classify', 'chatbot')
    )

    # ---------------- CHATBOT ----------------
    if options == 'chatbot':
        st.markdown('-------')
        st.markdown("Chatbot feature is under development.")

    # ---------------- VIDEO ----------------
    elif options == 'Video':
        st.markdown('-------')

        st.write('## Upload your video and select the exercise')
        st.write('Ensure full body is visible for accurate detection.')

        st.sidebar.markdown('-------')

        exercise_options = st.sidebar.selectbox(
            'Select Exercise', ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
        )

        st.sidebar.markdown('-------')

        video_file_buffer = st.sidebar.file_uploader(
            "Upload a video", type=["mp4", "mov", "avi", "asf", "m4v"]
        )

        if video_file_buffer is not None:
            # Save uploaded video
            tfflie = tempfile.NamedTemporaryFile(delete=False)
            tfflie.write(video_file_buffer.read())

            cap = cv2.VideoCapture(tfflie.name)

            # Show input video
            st.sidebar.text('Input Video')
            st.sidebar.video(video_file_buffer)

            st.markdown('## Input Video')
            st.video(video_file_buffer)

            st.markdown('-------')
            st.markdown('## Output Video')

            exer = exercise.Exercise()

            if exercise_options == 'Bicept Curl':
                counter, stage_right, stage_left = 0, None, None
                exer.bicept_curl(cap, is_video=True, counter=counter,
                                 stage_right=stage_right, stage_left=stage_left)

            elif exercise_options == 'Push Up':
                st.write("Stand sideways or face camera")
                counter, stage = 0, None
                exer.push_up(cap, is_video=True, counter=counter, stage=stage)

            elif exercise_options == 'Squat':
                counter, stage = 0, None
                exer.squat(cap, is_video=True, counter=counter, stage=stage)

            elif exercise_options == 'Shoulder Press':
                counter, stage = 0, None
                exer.shoulder_press(cap, is_video=True, counter=counter, stage=stage)

        else:
            st.warning("Please upload a video first")

    # ---------------- AUTO CLASSIFY ----------------
    elif options == 'Auto Classify':
        st.markdown('-------')

        st.write('Click button to start automatic classification')
        st.write('Ensure full body visibility.')

        if st.button('Start Auto Classification'):
            time.sleep(2)
            exer = exercise.Exercise()
            exer.auto_classify_and_count()

    # ---------------- WEBCAM ----------------
    elif options == 'WebCam':
        st.markdown('-------')

        exercise_general = st.sidebar.selectbox(
            'Select Exercise', ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
        )

        st.write('Click button to start training')
        start_button = st.button('Start Exercise')

        if start_button:
            time.sleep(2)

            cap = cv2.VideoCapture(0)
            exer = exercise.Exercise()

            if exercise_general == 'Bicept Curl':
                counter, stage_right, stage_left = 0, None, None
                exer.bicept_curl(cap, counter=counter,
                                 stage_right=stage_right, stage_left=stage_left)

            elif exercise_general == 'Push Up':
                counter, stage = 0, None
                exer.push_up(cap, counter=counter, stage=stage)

            elif exercise_general == 'Squat':
                counter, stage = 0, None
                exer.squat(cap, counter=counter, stage=stage)

            elif exercise_general == 'Shoulder Press':
                counter, stage = 0, None
                exer.shoulder_press(cap, counter=counter, stage=stage)


if __name__ == '__main__':
    main()