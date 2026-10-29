
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        layout.add_widget(
            Label(text="Mon premier APK Kivy !")
        )

        bouton = Button(text="Bonjour, Bathie !")
        bouton.bind(on_press=self.dire_bonjour)
        layout.add_widget(bouton)

        return layout

    def dire_bonjour(self, instance):
        instance.text = "Ça fonctionne !"


TestApp().run()
