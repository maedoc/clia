import os
import unittest
from unittest.mock import patch, mock_open
from clia.tools.save_memory import save_memory
from clia.tools.recall_memory import recall_memory
from pathlib import Path

class TestMemoryTools(unittest.TestCase):

    def setUp(self):
        self.config_dir = os.path.expanduser("~/.config/clia")
        self.memories_file = os.path.join(self.config_dir, "MEMORIES.md")

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_memory(self, mock_file, mock_mkdir, mock_home):
        mock_home.return_value = Path("/home/user")
        fact = "Test fact"
        save_memory(fact)
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_file.assert_called_once_with(Path("/home/user/.config/clia/MEMORIES.md"), "w", encoding="utf-8")
        mock_file().write.assert_called_once_with('\n## CLIA Memories\n\n- Test fact\n')

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="## CLIA Memories\n- Test fact 1\n- Test fact 2\n")
    def test_recall_memory_found(self, mock_file, mock_exists, mock_home):
        mock_home.return_value = Path("/home/user")
        mock_exists.return_value = True
        result = recall_memory()
        self.assertEqual(result, "Test fact 1, Test fact 2")

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.exists")
    def test_recall_memory_not_found(self, mock_exists, mock_home):
        mock_home.return_value = Path("/home/user")
        mock_exists.return_value = False
        result = recall_memory()
        self.assertEqual(result, "No memories found.")

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="## Some other heading\n- Not a memory\n")
    def test_recall_memory_no_clia_heading(self, mock_file, mock_exists, mock_home):
        mock_home.return_value = Path("/home/user")
        mock_exists.return_value = True
        result = recall_memory()
        self.assertEqual(result, "No memories found.")

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="## CLIA Memories\nThis is not a list\n")
    def test_recall_memory_no_list(self, mock_file, mock_exists, mock_home):
        mock_home.return_value = Path("/home/user")
        mock_exists.return_value = True
        result = recall_memory()
        self.assertEqual(result, "No memories found.")

    @patch("pathlib.Path.home")
    @patch("pathlib.Path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="## CLIA Memories\n- Fact 1\n## Next Heading\n- Not a memory")
    def test_recall_memory_stops_at_next_heading(self, mock_file, mock_exists, mock_home):
        mock_home.return_value = Path("/home/user")
        mock_exists.return_value = True
        result = recall_memory()
        self.assertEqual(result, "Fact 1")

if __name__ == "__main__":
    unittest.main()
