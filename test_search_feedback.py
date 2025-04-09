from search_feedback import search_feedback

def test_search():
    feedback = [{"name": "Alice", "score": 90}]
    result = search_feedback(feedback, "Alice")
    assert len(result) == 1
