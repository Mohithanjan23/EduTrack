from feedback_summary import summarize_feedback

def test_feedback_summary():
    data = [
        {"name": "A", "grade": "A", "score": 95},
        {"name": "B", "grade": "B", "score": 85},
        {"name": "C", "grade": "A", "score": 75},
    ]
    result = summarize_feedback(data)
    assert "top_scores" in result
    assert result["grade_count"] == {"A": 2, "B": 1}
