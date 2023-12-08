import json

class DataHandler:
    """Handles data storage and retrieval."""

    def load_scores(self, filename: str) -> list:
        """Load scores from a file."""
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("File is not in the correct format.")

    def save_scores(self, filename: str, scores: list):
        """Save scores to a file."""
        with open(filename, 'w') as file:
            json.dump(scores, file)
