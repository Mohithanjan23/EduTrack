from score_calculator import calculate_average_score

def test_average_score():
    data = [{"score": 80}, {"score": 90}]
    assert calculate_average_score(data) == 85
