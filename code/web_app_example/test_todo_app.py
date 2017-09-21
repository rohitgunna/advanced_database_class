import unittest
import requests

class TodoApp_TestCase(unittest.TestCase):

    def test_001_html_task_page_exists(self):
        """task page exists"""
        result = requests.get("http://localhost:8080/tasks")
        assert result.status_code == 200
        assert len(result.text) > 0  
        assert 'html' in result.headers['Content-Type']

    def test_002_task_page_refers_to_items(self):
        """there is a page that refers to open items"""
        result = requests.get("http://localhost:8080/tasks")
        assert "open items" in result.text 
    
    def test_003_table_contains_a_list_of_items(self):
        """there is a table that contains a list of items"""
        result = requests.get("http://localhost:8080/tasks")
        assert "<table" in result.text 
        assert "</table>" in result.text 

if __name__ == "__main__":
    unittest.main(verbosity=2)