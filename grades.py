class GradeCalculator:
    """Class to calculate grades based on scores."""

    def determine_grade(self, score: int, best: int) -> str:
        """Determine the grade based on the score and the best score."""
        if score >= best - 10:
            return 'A'
        elif score >= best - 20:
            return 'B'
        elif score >= best - 30:
            return 'C'
        elif score >= best - 40:
            return 'D'
        else:
            return 'F'
