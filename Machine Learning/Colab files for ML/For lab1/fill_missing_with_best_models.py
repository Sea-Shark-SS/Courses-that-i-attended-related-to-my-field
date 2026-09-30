A more robust version could additionally:

use MAE as a tie-breaker,
automatically skip models that were unavailable (e.g., LightGBM/XGBoost not installed),
iterate until no missing values remain rather than a fixed 3 passes,
print every predicted value together with its row index and algorithm used.

That version is generally what I'd use for a research project or publication-quality preprocessing pipeline