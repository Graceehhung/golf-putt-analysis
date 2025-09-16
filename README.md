<<<<<<< HEAD
# Golf Putting Video Analysis with MediaPipe

This project analyzes golf putting videos using [MediaPipe](https://mediapipe.dev/). It is designed for **offline, non-real-time** analysis: you provide a video, and the pipeline extracts body/club landmarks, computes golf-specific metrics, and visualizes results to help improve your putting technique.

## Project Structure

```
golf-putt-analysis
│
├── data/                         # raw + processed data
│   ├── videos/                   # putting videos (input)
│   │   └── sample_putt.mp4
│   ├── landmarks/                # extracted pose landmarks (CSV/json)
│   │   └── sample_putt_landmarks.csv
│   └── plots/                    # visual outputs
│       ├── head_stability.png
│       └── shoulder_rotation.png
│
├── src/                          # source code
│   ├── __init__.py
│   ├── capture_landmarks.py      # runs MediaPipe, saves landmarks to CSV
│   ├── compute_metrics.py        # golf-specific angles & metrics
│   ├── visualize.py              # plots + annotated videos
│   └── utils.py                  # helper functions
│
├── notebooks/                    # for experiments, debugging
│   └── putting_demo.ipynb
│
├── main.py                       # entry point: runs full pipeline
├── requirements.txt              # dependencies (mediapipe, opencv, pandas, matplotlib)
└── README.md                     # documentation
```

## Features

- **Video Upload:** Place your golf putting videos in `data/videos/`.
- **Landmark Extraction:** Uses MediaPipe to extract pose/club landmarks, saved as CSV/JSON in `data/landmarks/`.
- **Golf Metrics:** Computes golf-specific metrics (e.g., head stability, shoulder rotation) via `src/compute_metrics.py`.
- **Visualization:** Generates annotated videos and plots in `data/plots/`.
- **Jupyter Notebooks:** For experiments and debugging in `notebooks/`.

## Setup Instructions

1. Clone this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Place your putting videos in `data/videos/`.
4. Run the full pipeline:
    ```bash
    python main.py
    ```

## Dependencies

- mediapipe
- opencv-python
- pandas
- matplotlib

(See `requirements.txt` for the full list.)

## Usage

1. Add your video(s) to `data/videos/`.
2. Run `main.py` to process videos, extract landmarks, compute metrics, and generate plots.
3. Review results in `data/landmarks/` and `data/plots/`.

## Notes

- This tool is for **offline analysis** (not real-time).
- For best results, use high-quality, well-lit videos with a clear view of the golfer and putter.

## License

This project is for educational and research purposes. See [LICENSE](LICENSE)
=======
# golf-putt-analysis
Golf putt analysis project with MediaPipe skeleton overlay and body motion metrics.
>>>>>>> a9c356e5d535227d35f0a8ec945f88adc1fb7b0e
