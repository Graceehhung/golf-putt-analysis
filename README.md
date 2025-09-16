# Golf Putting Video Analysis with MediaPipe

This project analyzes golf putting videos using [MediaPipe](https://mediapipe.dev/). It is designed for **offline, non-real-time** analysis: you provide a video, and the pipeline extracts body landmarks, computes golf-specific angles, and visualizes results to help improve your putting technique.

## Project Structure

```

golf-putt-analysis
│
├── data/                         # raw data folder
│
├── output/                       # annotated video outputs
│
├── videos/                        # input putting videos
│   └── my\_putt\_video.mp4
│
├── .gitignore                     # files to ignore in git
├── LICENSE                        # project license
├── README.md                      # this documentation
├── requirements.txt               # dependencies
└── run\_golf\_skeleton.py           # main analysis script

````

## Features

- **Video Upload:** Place your golf putting videos in `videos/`.
- **Skeleton Extraction:** Uses MediaPipe to extract body landmarks and overlay skeleton on video.
- **Angle Metrics:** Computes basic golf-related angles (shoulders, elbows, wrists) per frame.
- **Visualization:** Saves annotated video to `output/`.
- **Lightweight:** Minimal setup; just Python dependencies in `requirements.txt`.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/<username>/golf-putt-analysis.git
cd golf-putt-analysis
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your putting video(s) to `videos/`.

4. Run the skeleton analysis:

```bash
python run_golf_skeleton.py --video "videos/my_putt_video.mp4" --output "output/skeleton_video.mp4"
```

## Dependencies

* `mediapipe`
* `opencv-python`
* `numpy`

(See `requirements.txt` for the full list.)

## Notes

* This tool is for **offline analysis** (not real-time).
* For best results, use high-quality, well-lit videos with a clear view of the golfer and putter.
* Annotated videos will be saved in `output/`.

## License

This project is for **educational and research purposes**. See [LICENSE](LICENSE).

```

This is **entirely Markdown**, bullet points, code blocks, and all headings included—ready to be pushed as your `README.md`.  

If you want, I can also **embed `.gitignore` and `requirements.txt` inside this same Markdown file** so anyone reading the README can copy all files from one place. Do you want me to do that?
```
