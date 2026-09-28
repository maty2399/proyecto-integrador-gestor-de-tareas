import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

import main
from persistencia import json_manager


class JsonManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.json_path = os.path.join(self.temp_dir.name, "tareas.json")
        self.json_file_patch = patch.object(json_manager, "JSON_FILE", self.json_path)
        self.json_file_patch.start()

    def tearDown(self):
        self.json_file_patch.stop()
        self.temp_dir.cleanup()

    def test_invalid_json_is_not_replaced_with_empty_data(self):
        original_content = "{invalido"
        with open(self.json_path, "w", encoding="utf-8") as file:
            file.write(original_content)

        with patch.object(json_manager, "escribir_log"):
            with self.assertRaises(ValueError):
                json_manager.cargar_json()

        with open(self.json_path, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), original_content)

    def test_missing_file_returns_empty_structures(self):
        with patch.object(json_manager, "escribir_log"):
            self.assertEqual(json_manager.cargar_json(), ([], [], []))

    def test_save_creates_parent_directory(self):
        nested_path = os.path.join(self.temp_dir.name, "nested", "tareas.json")
        with patch.object(json_manager, "JSON_FILE", nested_path):
            with patch.object(json_manager, "escribir_log"):
                json_manager.guardar_json([[1]], [[1]], [])

        self.assertTrue(os.path.exists(nested_path))


class TaskManagerTests(unittest.TestCase):
    def test_generated_id_accounts_for_completed_tasks(self):
        self.assertEqual(main.generar_id([[2]], [[1], [7]]), 8)

    def test_invalid_id_does_not_raise_or_change_data(self):
        tasks = [[1, "Tarea", "Alta", "pendiente", "", "", "", "", None]]
        history = []
        with patch("builtins.input", return_value="abc"):
            with redirect_stdout(StringIO()):
                changed = main.cambiar_estado(tasks, history, [])

        self.assertFalse(changed)
        self.assertEqual(tasks[0][3], "pendiente")
        self.assertEqual(history, [])

    def test_invalid_state_does_not_change_task_or_history(self):
        tasks = [[1, "Tarea", "Alta", "pendiente", "", "", "", "", None]]
        history = []
        with patch("builtins.input", side_effect=["1", "bloqueada"]):
            with redirect_stdout(StringIO()):
                changed = main.cambiar_estado(tasks, history, [])

        self.assertFalse(changed)
        self.assertEqual(tasks[0][3], "pendiente")
        self.assertEqual(history, [])

    def test_valid_state_change_returns_success(self):
        tasks = [[1, "Tarea", "Alta", "pendiente", "", "", "", "", None]]
        history = []
        with patch("builtins.input", side_effect=["1", "en curso"]):
            with patch.object(main, "escribir_log"):
                with redirect_stdout(StringIO()):
                    changed = main.cambiar_estado(tasks, history, [])

        self.assertTrue(changed)
        self.assertEqual(tasks[0][3], "en curso")
        self.assertEqual(history[0][1], "en curso")

    def test_menu_saves_after_adding_task(self):
        tasks, history, completed = [], [], []
        answers = ["1", "Tarea", "Media", "01-01-2027", "Personal", "Ana", "5"]
        with patch.object(main, "cargar_json", return_value=(tasks, history, completed)):
            with patch.object(main, "guardar_json") as save:
                with patch.object(main, "escribir_log"):
                    with patch("builtins.input", side_effect=answers):
                        with redirect_stdout(StringIO()):
                            main.menu()

        self.assertEqual(save.call_count, 2)
        self.assertEqual(save.call_args_list[0].args[0][0][1], "Tarea")

    def test_menu_does_not_save_when_json_cannot_be_loaded(self):
        with patch.object(main, "cargar_json", side_effect=ValueError("JSON inválido")):
            with patch.object(main, "guardar_json") as save:
                with redirect_stdout(StringIO()):
                    main.menu()

        save.assert_not_called()


if __name__ == "__main__":
    unittest.main()