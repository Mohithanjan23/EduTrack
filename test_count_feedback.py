from count_feedback import count_feedback

def test_count():
    feedback = [{"name": "X"}, {"name": "Y"}]
    assert count_feedback(feedback) == 2
