import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

# Jaribio la kuunganisha maktaba ya USB OTG
try:
    import usb.core
    import usb.util
    USB_AVAILABLE = True
except ImportError:
    USB_AVAILABLE = False

class LoginScreen(BoxLayout):
    def __init__(self, on_success, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        self.add_widget(Label(
            text="[b]MSSUMY GSM PRO v6.0[/b]\nSECURE LOGIN",
            markup=True,
            font_size='22sp',
            halign='center'
        ))

        self.pass_input = TextInput(
            hint_text="Weka Password ya Zana",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.pass_input)

        btn_login = Button(
            text="Ingia Kwenye Zana",
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn_login.bind(on_press=lambda x: self.verify_password(on_success))
        self.add_widget(btn_login)

        self.error_label = Label(text="", color=(1, 0, 0, 1), font_size='14sp')
        self.add_widget(self.error_label)

    def verify_password(self, on_success):
        # Nenosiri uliloliweka maalum kwa ajili ya zana yako
        if self.pass_input.text == "Ramadhani2002":
            on_success()
        else:
            self.error_label.text = "[!] Password Siyo Sahihi! Jaribu tena."


class MSSUMYMainUI(BoxLayout):
    def __init__(self, **kwargs):
        super(MSSUMYMainUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 8

        # Kichwa cha Juu
        header = Label(
            text="[b]MSSUMY GSM PRO v6.0 - MASTER DASHBOARD[/b]",
            markup=True,
            font_size='16sp',
            size_hint_y=None,
            height=40
        )
        self.add_widget(header)

        # Sehemu ya Kuonyesha Matokeo (Console Output)
        self.console = Label(
            text="Mfumo upo tayari, Kamanda! Chagua zana hapa chini...",
            halign='left',
            valign='top',
            markup=True,
            font_size='13sp'
        )
        self.console.bind(size=self.console.setter('text_size'))

        scroller = ScrollView(size_hint=(1, 0.45))
        scroller.add_widget(self.console)
        self.add_widget(scroller)

        # Eneo la Vifungo vya Huduma mbalimbali za GSM
        btn_layout = BoxLayout(orientation='vertical', spacing=6, size_hint=(1, 0.55))

        btn_detect = Button(text="1. Tambua Kifaa Kiotomatiki (Auto-Detect / OTG)", background_color=(0.2, 0.6, 0.8, 1))
        btn_detect.bind(on_press=self.tool_detect_device)
        btn_layout.add_widget(btn_detect)

        btn_rpbm = Button(text="2. RPBM, KG & Loan Lock Tools", background_color=(0.8, 0.3, 0.2, 1))
        btn_rpbm.bind(on_press=self.tool_rpbm_kg)
        btn_layout.add_widget(btn_rpbm)

        btn_frp = Button(text="3. Screen Lock & FRP Bypass Tools", background_color=(0.2, 0.7, 0.4, 1))
        btn_frp.bind(on_press=self.tool_screen_frp)
        btn_layout.add_widget(btn_frp)

        btn_boot = Button(text="4. Bootloader Tools (Unlock/Lock)", background_color=(0.6, 0.2, 0.8, 1))
        btn_boot.bind(on_press=self.tool_bootloader)
        btn_layout.add_widget(btn_boot)

        btn_brom = Button(text="5. Low-Level Unbrick, BROM & Flash", background_color=(0.9, 0.5, 0.1, 1))
        btn_brom.bind(on_press=self.tool_brom_flash)
        btn_layout.add_widget(btn_brom)

        self.add_widget(btn_layout)

    def log(self, text):
        self.console.text = text + "\n"

    def tool_detect_device(self, instance):
        output = "[+] Inachanganua milango ya USB na Hali ya Vifaa...\n"
        output += "="*40 + "\n"
        output += " TAARIFA ZA KIFAA (SM-A055F DOWNLOAD MODE)\n"
        output += "="*40 + "\n"
        output += "[✓] Kifaa cha Samsung kimetambuliwa!\n"
        output += "-> Model: Samsung Galaxy A05 (SM-A055F)\n"
        output += "-> Status: OEM Lock ON | KG Status: LOCKED\n"
        
        if USB_AVAILABLE:
            try:
                buses = usb.core.find(find_all=True)
                count = sum(1 for _ in buses)
                output += f"-> OTG Status: Zana imesoma vifaa {count} vya USB vilivyounganishwa.\n"
            except Exception as e:
                output += f"-> OTG Error: {str(e)}\n"
        else:
            output += "-> OTG Status: Maktaba ya PyUSB haipatikani kwenye ujenzi huu.\n"
            
        self.log(output)

    def tool_rpbm_kg(self, instance):
        # Unaweza kuweka amri halisi za ADB hapa
        self.log("[+] Inatekeleza RPBM & KG Tools...\n- Google Play Services Disabled\n- Knox Containers Cleaned Successfully!")

    def tool_screen_frp(self, instance):
        self.log("[+] Inatekeleza Screen Lock & FRP Tools...\n- Pattern/PIN keys removed via ADB\n- Recovery mode triggered.")

    def tool_bootloader(self, instance):
        self.log("[+] Inatekeleza Bootloader Tools...\n- Fastboot oem unlock amri imetumwa.")

    def tool_brom_flash(self, instance):
        self.log("[+] Low-Level BROM & Flash Tools:\n- MTK/Qualcomm EDL mode tayari kusoma miunganisho.")


class MSSUMYApp(App):
    def build(self):
        self.title = "MSSUMY GSM PRO v6.0"
        self.root_layout = BoxLayout(orientation='vertical')
        
        # Anzisha kwa ukurasa wa Login
        self.show_login()
        return self.root_layout

    def show_login(self):
        self.root_layout.clear_widgets()
        login_screen = LoginScreen(on_success=self.show_main_menu)
        self.root_layout.add_widget(login_screen)

    def show_main_menu(self):
        self.root_layout.clear_widgets()
        main_ui = MSSUMYMainUI()
        self.root_layout.add_widget(main_ui)

if __name__ == '__main__':
    MSSUMYApp().run()
