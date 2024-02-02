import flet as ft
import pdf_to_csv
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)

plik = ""

def main(page: Page):
    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        global plik
        print(e.files)
        plik = e.files[0].path
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()



    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Convert",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: pdf_to_csv.main(plik),

                ),
                selected_files,
            ]
        ),
    )


if __name__ == '__main__':
    ft.app(target=main)
