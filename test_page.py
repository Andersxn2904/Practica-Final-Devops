import unittest

class TestIndexPage(unittest.TestCase):
    def setUp(self):
        with open("index.html", "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_title_exists(self):
        self.assertIn("<title>Página Interactiva</title>", self.content)

    def test_header_exists(self):
        self.assertIn("<h1>Página Interactiva</h1>", self.content)

    def test_buttons_exist(self):
        self.assertIn("onclick=\"updateContent('¡Hola, Mundo!')\"", self.content)
        self.assertIn("onclick=\"updateContent('¡Bienvenido a la página interactiva!')\"", self.content)
        self.assertIn("onclick=\"updateContent('Gracias por visitarnos.')\"", self.content)

    def test_div_content_exists(self):
        self.assertIn("<div id=\"content\">Aquí aparecerá el contenido...</div>", self.content)

    def test_script_function_exists(self):
        self.assertIn("function updateContent(message)", self.content)
        self.assertIn("document.getElementById('content').innerText = message;", self.content)

if __name__ == "__main__":
    unittest.main()
