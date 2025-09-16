import cv2
import mediapipe as mp
import os
import argparse

def run_skeleton(video_path, output_path):
    """Process video and overlay MediaPipe pose skeleton."""

    if not os.path.exists(video_path):
        print(f"❌ ERROR: Video not found at {video_path}")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ ERROR: Could not open video {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    pose = mp_pose.Pose(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    print("🟢 Processing video for skeleton overlay...")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        out.write(frame)

        if frame_count % 30 == 0:
            print(f"[DEBUG] Processed {frame_count} frames...")

    cap.release()
    out.release()
    print(f"✅ Done! Annotated video saved to {output_path}")
    print(f"[DEBUG] Total frames processed: {frame_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True, help="Path to input video")
    parser.add_argument("--output", default="data/output/skeleton_video.mp4", help="Path to save annotated video")
    args = parser.parse_args()

    # ✅ Make sure the correct function is called
    run_skeleton(args.video, args.output)
