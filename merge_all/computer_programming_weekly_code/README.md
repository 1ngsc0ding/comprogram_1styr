# Computer Programming — weekly code bundle

This bundle was prepared from `merged_file.pdf` (863 pages). The PDF contains selectable text, so the code and slide text were extracted directly rather than re-OCRed. No pages were blank in the text extraction.

## Important about week numbering
The source does not label every section with an official week number. The `week_01`–`week_12` names are **inferred study groups**, based on the source deck boundaries and topic progression, not a claim about the lecturer’s official weekly schedule. Some content repeats across decks and review slides; those repetitions are preserved in `source_slides.md`.

## Contents
- `week_XX/source_slides.md`: extracted text from every source PDF page assigned to that group, with source page numbers. It preserves incremental snippets and original `...` markers.
- `week_XX/runnable_examples/`: completed examples that can be run as standalone Python, Processing Python Mode (`.pyde`), or Processing Java Mode (`.pde`) files.
- `source_page_map.md`: page ranges and topics.

## Running examples
- `.py`: run with `python filename.py` (examples use Python 3).
- `matplotlib_charts.py` and `weekly_temperatures.py`: install Matplotlib first with `python -m pip install matplotlib`.
- `.pyde`: open Processing, install/select **Python Mode**, then paste/open the sketch. These use Processing functions such as `size()`, `ellipse()`, `line()`, `random()`, `mouseX`, and `mouseY`; they are not ordinary CPython scripts.
- `.pde`: open in Processing **Java Mode**.
- `gui_multiplier.py`: requires a desktop Python installation with Tkinter support.

## Fidelity notes
The extracted slide text is the source record. Runnable examples are completed/normalized versions based on the visible lecture examples, with omitted ellipses filled in where needed and small corrections required for execution. They are not represented as verbatim code where the slide itself showed only an incremental fragment. Some slides are explanatory rather than code-based.
