from report_generator import generate_report
import os

def test_generate_report(tmp_path):
    feedback = [{"name": "Test", "grade": "A", "score": 90, "comment": "Good"}]
    report_file = tmp_path / "report.txt"
    generate_report(feedback, report_file)
    assert report_file.exists()
