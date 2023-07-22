import flet as ft
from js import XMLHttpRequest

webhook_url = "https://maker.ifttt.com/trigger"
ifttt_image_url = "https://play-lh.googleusercontent.com/XFBZEhuA1CdMM4WRd2G9ahWL5SUhIV6MgE0ZKEqtsd3jChyhABQB7-rEjkvnhLt8Als=w240-h480-rw"


def trigger_web_hook(page_route: str):
    try:
        req = XMLHttpRequest.new()
        req.open("GET", f'{webhook_url}{page_route}', False)
        req.send()
    except Exception as e:
        pass


def main(page: ft.Page):

    if(page.route == "/"):
        title_container = ft.Container(ft.Row([ft.Image(src=ifttt_image_url, border_radius=ft.border_radius.all(10), width=100, height=100, fit=ft.ImageFit.CONTAIN),
                                               ft.Icon(name=ft.icons.ADD_CIRCLE_ROUNDED, color=ft.colors.WHITE, size=30),
                                               ft.Icon(name=ft.icons.NFC_ROUNDED, color=ft.colors.RED, size=100)],alignment=page.vertical_alignment.CENTER), image_fit=ft.ImageFit.CONTAIN)
        page.add(ft.Row([]))
        page.add(title_container)
        page.add(ft.Row(
            [
                ft.Text("NFC IFTTT Webhook trigger",
                        size=20, weight=ft.FontWeight.W_900)
            ], alignment=page.vertical_alignment.CENTER)
        )

    else:
        trigger_web_hook(page_route=page.route)
        page.add(ft.Row(
            [
                ft.Icon(name=ft.icons.CHECK_CIRCLE_ROUNDED,
                        color=ft.colors.GREEN, size=200)
            ], alignment=page.vertical_alignment.CENTER)
        )

        page.add(ft.Row(
            [
                ft.Text("Webhook triggered successfully",
                        size=20, weight=ft.FontWeight.W_900)
            ], alignment=page.vertical_alignment.CENTER)
        )
    page.update()


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
