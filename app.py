
import os
import sys
import shutil
import subprocess
import threading
import datetime
import locale
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

STRINGS = {
    "tr": {
        "win_title": "Android TV Hızlandırıcı & Debloat Aracı (Çoklu Marka Destekli)",
        "header_title": "📺 Android TV Hızlandırıcı & Debloat",
        "header_sub": "Philips • TCL • Xiaomi • Sony • Vestel • Google TV",
        "ip_label": "TV IP Adresi:",
        "connect_btn": "🔌 TV'ye Bağlan",
        "connecting": "TV'ye bağlanılıyor ({ip}:5555)...",
        "status_connected": "● Bağlı (Aktif)",
        "status_disconnected": "● Bağlantı Yok",
        "status_rebooting": "● Yeniden Başlatılıyor...",
        "dev_info_default": "Marka: -- | Model: -- | Android: -- | Boş RAM: --",
        "dev_info_fmt": "Marka: {brand} | Model: {model} | Android: {android} | Kullanılabilir RAM: {ram}",
        "profile_waiting": "Aktif Profil: Bekleniyor...",
        "profile_fmt": "Aktif Profil: {profile}",
        "sec_speed": "⚡ Hızlandırma & Akıllı Temizlik",
        "btn_debloat": "🚀 Akıllı Temizlik (Marka + Evrensel Çöpleri Kapat)",
        "btn_anim": "⚡ Animasyonları 0.5x Yap (Hızlandır)",
        "btn_cache": "🧹 RAM & Önbellek Temizle (Trim Caches)",
        "sec_launcher": "🏠 Ana Ekran & Geri Yükleme",
        "btn_launcher": "🎯 FLauncher'ı Aktif Et (Reklamlı Ekranı Kapat)",
        "btn_restore": "⏪ Tüm Paketleri Geri Aç (Fabrika Haline Dön)",
        "btn_reboot": "🔄 TV'yi Yeniden Başlat (Reboot)",
        "log_title": "📋 İşlem Günlüğü & Terminal",
        "btn_clear": "Temizle",
        "app_ready": "Uygulama hazır. TV IP adresini girip 'Bağlan' butonuna basın.",
        "enter_ip_err": "Lütfen bir IP adresi girin.",
        "adb_path": "ADB Yolu: {path}",
        "conn_success": "✅ Cihaz bağlandı ve yetkilendirildi.",
        "conn_fail": "⚠️ Cihaza bağlanılamadı. TV ekranındaki 'Bu bilgisayara izin verilsin mi?' onayını verin.",
        "need_connect": "Önce TV'ye bağlanmalısınız.",
        "debloat_confirm": "Bu televizyondaki güvenli çöp ve reklam servisleri 'pm disable-user --user 0' ile kapatılacak.\n\nHiçbir dosya silinmeyecektir. Devam edilsin mi?",
        "debloat_start": "=== AKILLI TEMİZLİK (DEBLOAT) BAŞLATILIYOR ===",
        "scanning_pkgs": "TV'de yüklü paketler taranıyor...",
        "found_pkgs": "TV'de toplam {count} paket tespit edildi.",
        "no_debloat": "Bu televizyonda kapatılacak yeni bir çöp paket bulunamadı.",
        "debloat_done": "İşlem tamamlandı!\n\nToplam {count} paket 'pm disable-user' ile güvenle kapatıldı.",
        "anim_start": "Pencere ve geçiş animasyonları 0.5x yapılıyor...",
        "anim_done": "⚡ Animasyon hızları 0.5x yapıldı! Menü geçişleri iki kat hızlandı.",
        "cache_start": "Sistem önbelleği temizleniyor (pm trim-caches)...",
        "cache_done": "🧹 Önbellek temizlendi.",
        "flauncher_missing": "Güvenliğiniz gereği orijinal ana ekran kapatılmadı.\n\nLütfen önce TV'deki Google Play Store'dan 'FLauncher' uygulamasını kurun.",
        "flauncher_done": "FLauncher başarıyla varsayılan ana ekran yapıldı!",
        "restore_confirm": "Bu televizyonda kapatılan TÜM paketler (reklam servisleri ve orijinal ana ekran dahil) yeniden açılacaktır ('pm enable').\n\nTelevizyon fabrika ayarlarına döndürülsün mü?",
        "restore_start": "=== GERİ YÜKLEME (RESTORE) BAŞLADI ===",
        "restore_done": "Tüm paketler başarıyla geri açıldı! TV orijinal yazılım haline döndü.",
        "reboot_confirm": "Televizyon şimdi uzaktan yeniden başlatılsın mı?",
        "reboot_start": "TV yeniden başlatılıyor (adb reboot)..."
    },
    "en": {
        "win_title": "Android TV Optimizer & Debloat Tool (Multi-Brand Support)",
        "header_title": "📺 Android TV Optimizer & Debloat",
        "header_sub": "Philips • TCL • Xiaomi • Sony • Vestel • Google TV",
        "ip_label": "TV IP Address:",
        "connect_btn": "🔌 Connect to TV",
        "connecting": "Connecting to TV ({ip}:5555)...",
        "status_connected": "● Connected (Active)",
        "status_disconnected": "● Disconnected",
        "status_rebooting": "● Rebooting...",
        "dev_info_default": "Brand: -- | Model: -- | Android: -- | Free RAM: --",
        "dev_info_fmt": "Brand: {brand} | Model: {model} | Android: {android} | Available RAM: {ram}",
        "profile_waiting": "Active Profile: Waiting...",
        "profile_fmt": "Active Profile: {profile}",
        "sec_speed": "⚡ Optimization & Smart Debloat",
        "btn_debloat": "🚀 Smart Debloat (Disable Brand + Universal Bloat)",
        "btn_anim": "⚡ Set Animations to 0.5x (Speed Up UI)",
        "btn_cache": "🧹 Clean RAM & Cache (Trim Caches)",
        "sec_launcher": "🏠 Home Launcher & Restore",
        "btn_launcher": "🎯 Enable FLauncher (Disable Ad-filled Stock Launcher)",
        "btn_restore": "⏪ Restore All Packages (Factory State)",
        "btn_reboot": "🔄 Reboot TV",
        "log_title": "📋 Operation Log & Terminal",
        "btn_clear": "Clear",
        "app_ready": "Application ready. Enter TV IP address and click 'Connect to TV'.",
        "enter_ip_err": "Please enter a valid IP address.",
        "adb_path": "ADB Path: {path}",
        "conn_success": "✅ Device connected and authorized.",
        "conn_fail": "⚠️ Could not connect. Please accept 'Allow USB debugging from this computer?' on TV screen.",
        "need_connect": "Please connect to the TV first.",
        "debloat_confirm": "Safe bloatware, ad and telemetry services will be disabled via 'pm disable-user --user 0'.\n\nNo files will be uninstalled or deleted. Proceed?",
        "debloat_start": "=== SMART DEBLOAT STARTED ===",
        "scanning_pkgs": "Scanning installed packages on TV...",
        "found_pkgs": "Total of {count} packages detected on TV.",
        "no_debloat": "No bloatware packages found to disable on this TV.",
        "debloat_done": "Operation completed!\n\nA total of {count} packages safely disabled with 'pm disable-user'.",
        "anim_start": "Setting window and transition animation scales to 0.5x...",
        "anim_done": "⚡ Animation scales set to 0.5x! Menu transitions are now 2x faster.",
        "cache_start": "Trimming system memory caches (pm trim-caches)...",
        "cache_done": "🧹 Memory caches trimmed.",
        "flauncher_missing": "Stock launcher was NOT disabled for your safety.\n\nPlease install 'FLauncher' from Google Play Store on your TV first.",
        "flauncher_done": "FLauncher is now successfully set as the default launcher!",
        "restore_confirm": "ALL previously disabled packages (including stock launcher) will be re-enabled via 'pm enable'.\n\nRestore TV to factory software state?",
        "restore_start": "=== RESTORING PACKAGES STARTED ===",
        "restore_done": "All packages successfully restored! TV is back to stock state.",
        "reboot_confirm": "Reboot TV remotely now?",
        "reboot_start": "Rebooting TV (adb reboot)..."
    }
}
UNIVERSAL_SAFE_DEBLOAT = [
    ("com.google.android.tvrecommendations", "Google TV ads and recommendation channels"),
    ("com.google.android.feedback", "Google feedback crash reporter"),
    ("com.android.printspooler", "Print spooler service"),
    ("com.google.android.syncadapters.calendar", "Calendar sync adapter"),
    ("com.android.providers.calendar", "Calendar provider"),
    ("com.android.providers.contacts", "Contacts provider"),
    ("com.android.providers.userdictionary", "User dictionary provider"),
    ("com.google.android.play.games", "Google Play Games"),
    ("com.google.android.videos", "Google TV / Play Movies & TV"),
    ("com.google.android.marvin.talkback", "TalkBack screen reader"),
    ("com.vewd.core.browserui", "Vewd Opera TV browser engine"),
]

BRAND_DEBLOAT_PACKAGES = {
    "philips": [
        ("org.droidtv.demome", "Philips retail demo mode"),
        ("org.droidtv.sticker", "Store retail sticker overlays"),
        ("org.droidtv.candeebug", "Philips hardware debug service"),
        ("org.droidtv.usagelogger", "Philips usage telemetry logger"),
        ("org.droidtv.tv.frameworklogger", "System framework logger"),
        ("org.droidtv.usbbreakin", "USB factory test tool"),
        ("org.droidtv.recommendation", "Philips TV recommendation channels"),
        ("org.droidtv.nettvrecommender", "NetTV recommender service"),
        ("org.droidtv.nettv.market", "NetTV App Gallery"),
        ("org.droidtv.nettvapps", "NetTV web apps framework"),
        ("org.droidtv.nettvregistration", "NetTV registration"),
        ("org.droidtv.nettvbrowser", "NetTV browser"),
        ("org.droidtv.amazonalexa", "Amazon Alexa voice client"),
        ("com.phorus.playfi.tv", "DTS Play-Fi multiroom audio"),
        ("com.phorus.playfi.softap", "DTS Play-Fi SoftAP")
    ],
    "tcl": [
        ("com.tcl.browser", "TCL browser bloatware"),
        ("com.tcl.appmarket2", "TCL App Market"),
        ("com.tcl.waterfall.overseas", "TCL waterfall home recommendations"),
        ("com.tcl.usercenter", "TCL user center"),
        ("com.tcl.partner", "TCL partner bloatware"),
        ("com.tcl.channel", "TCL Channel streaming ads"),
        ("com.tcl.guard", "TCL Safety Guard bloat"),
        ("com.tcl.messagebox", "TCL push ads and notifications"),
        ("com.tcl.tvmanager", "TCL background manager"),
        ("com.tcl.bi", "TCL Business Intelligence telemetry"),
        ("com.tcl.logman", "TCL log manager")
    ],
    "xiaomi": [
        ("com.xiaomi.mitv.advertise", "Xiaomi boot and home ads"),
        ("com.xiaomi.mitv.upgrade", "Xiaomi background upgrade service"),
        ("com.miui.tv.analytics", "Mi TV analytics telemetry"),
        ("com.xiaomi.statistic", "Xiaomi statistics telemetry"),
        ("com.xiaomi.mitv.tvpush.tvpushservice", "Mi TV push notifications"),
        ("com.xiaomi.mitv.shop", "Mi TV Shop"),
        ("com.xiaomi.mitv.payment", "Mi Pay service"),
        ("com.xiaomi.mitv.mediaexplorer", "Mi Media Explorer background")
    ],
    "sony": [
        ("com.sony.dtv.braviasync", "Sony Bravia Sync demo"),
        ("com.sony.dtv.demomode", "Sony demo mode"),
        ("com.sony.dtv.smarthelp", "Sony smart guide"),
        ("com.sony.dtv.browser.ceb", "Sony browser"),
        ("com.sony.dtv.customersupport", "Sony customer support telemetry")
    ],
    "vestel": [
        ("com.vestel.telemetry", "Vestel telemetry"),
        ("com.vestel.demomode", "Vestel demo mode"),
        ("com.vestel.browser", "Vestel TV browser")
    ]
}

UNIVERSAL_PROTECTED = [
    "com.google.android.gms",
    "com.google.android.gsf",
    "com.android.vending",
    "com.android.location.fused",
    "com.google.android.tv.remote.service",
    "com.google.android.inputmethod.latin",
    "com.android.bluetooth",
    "com.google.android.apps.mediashell",
    "com.google.android.webview",
    "com.google.android.katniss",
    "com.google.android.youtube.tvmusic",
    "org.droidtv.dropboxprovider",
    "org.droidtv.dlna",
    "org.droidtv.GlobalKey",
    "org.droidtv.devicesetup",
    "org.droidtv.contentexplorer",
    "org.droidtv.settings",
    "org.droidtv.channels",
    "org.droidtv.playtv",
    "org.droidtv.ambiair",
    "org.droidtv.ambihuecommon",
    "org.droidtv.alhuewizard",
    "org.droidtv.sunrise",
    "com.tcl.suspension",
    "com.tcl.tv",
    "com.tcl.tvinput",
    "com.tcl.tcl_bt_rcu_service",
    "com.tcl.autopair",
    "com.tcl.settings",
    "com.xiaomi.mitv.tvinput",
    "com.xiaomi.mitv.bluetooth",
    "com.xiaomi.mitv.settings",
    "com.mediatek.tvinput",
    "com.mediatek.tunerservice",
    "com.mediatek.tv.agent"
]

def detect_system_language():
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.lower().startswith("tr"):
            return "tr"
    except Exception:
        pass
    return "en"

def find_adb():
    if shutil.which("adb"):
        return "adb"
    candidates = [
        os.path.join(os.path.dirname(sys.executable), "adb.exe"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "adb.exe"),
        r"C:\platform-tools\adb.exe",
        os.path.join(os.getcwd(), "adb.exe")
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return "adb"
class AndroidTVOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.lang = detect_system_language()
        self.adb_bin = find_adb()
        self.connected_ip = ""
        self.is_connected = False
        self.detected_brand = "Bilinmiyor"
        self.detected_model = "Bilinmiyor"
        self.detected_brand_key = "generic"

        self.geometry("930x760")
        self.minsize(840, 680)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self._build_ui()
        self.apply_language()

        self.log(self.t("adb_path").format(path=self.adb_bin))
        self.log(self.t("app_ready"))

    def t(self, key):
        return STRINGS.get(self.lang, STRINGS["en"]).get(key, key)

    def _build_ui(self):
        header_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#1f2937")
        header_frame.pack(fill="x", padx=16, pady=(16, 8))

        self.title_label = ctk.CTkLabel(
            header_frame,
            text="",
            font=ctk.CTkFont(size=21, weight="bold"),
            text_color="#60a5fa"
        )
        self.title_label.pack(side="left", padx=16, pady=12)

        lang_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        lang_container.pack(side="right", padx=16, pady=12)

        ctk.CTkLabel(lang_container, text="🌐", font=ctk.CTkFont(size=14)).pack(side="left", padx=(0, 4))
        self.lang_switch = ctk.CTkSegmentedButton(
            lang_container,
            values=["Türkçe", "English"],
            command=self.on_lang_changed,
            width=140
        )
        self.lang_switch.set("Türkçe" if self.lang == "tr" else "English")
        self.lang_switch.pack(side="left")

        conn_frame = ctk.CTkFrame(self, corner_radius=10)
        conn_frame.pack(fill="x", padx=16, pady=8)

        self.ip_lbl = ctk.CTkLabel(conn_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.ip_lbl.grid(row=0, column=0, padx=(16, 8), pady=12, sticky="w")

        self.ip_entry = ctk.CTkEntry(conn_frame, width=180, placeholder_text="192.168.1.100")
        self.ip_entry.insert(0, "192.168.1.100")
        self.ip_entry.grid(row=0, column=1, padx=8, pady=12, sticky="w")

        self.btn_connect = ctk.CTkButton(
            conn_frame,
            text="",
            command=self.on_connect_clicked,
            width=140,
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )
        self.btn_connect.grid(row=0, column=2, padx=8, pady=12)

        self.status_badge = ctk.CTkLabel(
            conn_frame,
            text="",
            text_color="#ef4444",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.status_badge.grid(row=0, column=3, padx=16, pady=12, sticky="w")

        self.lbl_device_info = ctk.CTkLabel(
            conn_frame,
            text="",
            text_color="#9ca3af",
            font=ctk.CTkFont(size=12)
        )
        self.lbl_device_info.grid(row=1, column=0, columnspan=4, padx=16, pady=(0, 4), sticky="w")

        self.lbl_profile_badge = ctk.CTkLabel(
            conn_frame,
            text="",
            text_color="#38bdf8",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.lbl_profile_badge.grid(row=2, column=0, columnspan=4, padx=16, pady=(0, 12), sticky="w")

        action_container = ctk.CTkFrame(self, corner_radius=10)
        action_container.pack(fill="x", padx=16, pady=8)

        col1 = ctk.CTkFrame(action_container, fg_color="transparent")
        col1.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        self.lbl_sec_speed = ctk.CTkLabel(col1, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_sec_speed.pack(anchor="w", pady=(0, 6))

        self.btn_debloat = ctk.CTkButton(
            col1,
            text="",
            command=self.on_debloat_clicked,
            fg_color="#059669",
            hover_color="#047857"
        )
        self.btn_debloat.pack(fill="x", pady=4)

        self.btn_anim = ctk.CTkButton(
            col1,
            text="",
            command=self.on_anim_clicked,
            fg_color="#0284c7",
            hover_color="#0369a1"
        )
        self.btn_anim.pack(fill="x", pady=4)

        self.btn_cache = ctk.CTkButton(
            col1,
            text="",
            command=self.on_cache_clicked,
            fg_color="#d97706",
            hover_color="#b45309"
        )
        self.btn_cache.pack(fill="x", pady=4)

        col2 = ctk.CTkFrame(action_container, fg_color="transparent")
        col2.pack(side="right", fill="both", expand=True, padx=8, pady=8)

        self.lbl_sec_launcher = ctk.CTkLabel(col2, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_sec_launcher.pack(anchor="w", pady=(0, 6))

        self.btn_launcher_switch = ctk.CTkButton(
            col2,
            text="",
            command=self.on_switch_launcher_clicked,
            fg_color="#7c3aed",
            hover_color="#6d28d9"
        )
        self.btn_launcher_switch.pack(fill="x", pady=4)

        self.btn_revert = ctk.CTkButton(
            col2,
            text="",
            command=self.on_restore_clicked,
            fg_color="#dc2626",
            hover_color="#b91c1c"
        )
        self.btn_revert.pack(fill="x", pady=4)

        self.btn_reboot = ctk.CTkButton(
            col2,
            text="",
            command=self.on_reboot_clicked,
            fg_color="#4b5563",
            hover_color="#374151"
        )
        self.btn_reboot.pack(fill="x", pady=4)

        log_header = ctk.CTkFrame(self, fg_color="transparent")
        log_header.pack(fill="x", padx=16, pady=(8, 0))

        self.lbl_log_title = ctk.CTkLabel(log_header, text="", font=ctk.CTkFont(size=13, weight="bold"))
        self.lbl_log_title.pack(side="left")

        self.btn_clear_log = ctk.CTkButton(log_header, text="", width=60, height=24, command=self.clear_log)
        self.btn_clear_log.pack(side="right")

        self.log_textbox = ctk.CTkTextbox(self, corner_radius=10, font=ctk.CTkFont(family="Consolas", size=11))
        self.log_textbox.pack(fill="both", expand=True, padx=16, pady=(4, 16))
    def on_lang_changed(self, choice):
        self.lang = "tr" if choice == "Türkçe" else "en"
        self.apply_language()
        self.log(f"Dil değiştirildi: {choice} / Language changed: {choice}")

    def apply_language(self):
        self.title(self.t("win_title"))
        self.title_label.configure(text=self.t("header_title"))
        self.ip_lbl.configure(text=self.t("ip_label"))
        self.btn_connect.configure(text=self.t("connect_btn"))

        if not self.is_connected:
            self.status_badge.configure(text=self.t("status_disconnected"))
            self.lbl_device_info.configure(text=self.t("dev_info_default"))
            self.lbl_profile_badge.configure(text=self.t("profile_waiting"))
        else:
            self.status_badge.configure(text=self.t("status_connected"))
            self.update_device_info_labels()

        self.lbl_sec_speed.configure(text=self.t("sec_speed"))
        self.btn_debloat.configure(text=self.t("btn_debloat"))
        self.btn_anim.configure(text=self.t("btn_anim"))
        self.btn_cache.configure(text=self.t("btn_cache"))

        self.lbl_sec_launcher.configure(text=self.t("sec_launcher"))
        self.btn_launcher_switch.configure(text=self.t("btn_launcher"))
        self.btn_revert.configure(text=self.t("btn_restore"))
        self.btn_reboot.configure(text=self.t("btn_reboot"))

        self.lbl_log_title.configure(text=self.t("log_title"))
        self.btn_clear_log.configure(text=self.t("btn_clear"))

    def update_device_info_labels(self):
        if not self.is_connected:
            return
        profiles = {
            "philips": "Philips Smart Profile (Ambilight & TV Inputs Protected)" if self.lang == "en" else "Philips Akıllı Profili (Ambilight ve Girişler Korumalı)",
            "tcl": "TCL Smart Profile (Suspension/Source & HDMI Protected)" if self.lang == "en" else "TCL Akıllı Profili (Suspension/Source & HDMI Korumalı)",
            "xiaomi": "Xiaomi / Mi TV Profile (Remote & TV Input Protected)" if self.lang == "en" else "Xiaomi / Mi TV Profili (Kumanda & TV Girişi Korumalı)",
            "sony": "Sony Bravia Profile (Picture/Audio Engines Protected)" if self.lang == "en" else "Sony Bravia Profili (Görüntü/Ses Motorları Korumalı)",
            "vestel": "Vestel / Toshiba Profile (Tuner Protected)" if self.lang == "en" else "Vestel / Toshiba Profili (Tuner Korumalı)",
            "generic": "Universal Android TV Profile (Safe Mode)" if self.lang == "en" else "Genel Android TV Güvenli Profili"
        }
        p_name = profiles.get(self.detected_brand_key, profiles["generic"])
        self.lbl_profile_badge.configure(text=self.t("profile_fmt").format(profile=p_name))

    def log(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        formatted = f"[{now}] {message}\n"
        self.log_textbox.insert("end", formatted)
        self.log_textbox.see("end")

    def clear_log(self):
        self.log_textbox.delete("1.0", "end")

    def run_adb(self, cmd_args):
        full_cmd = [self.adb_bin]
        if self.connected_ip:
            full_cmd.extend(["-s", f"{self.connected_ip}:5555"])
        full_cmd.extend(cmd_args)
        try:
            res = subprocess.run(full_cmd, capture_output=True, text=True, timeout=20)
            return res.stdout.strip(), res.stderr.strip()
        except subprocess.TimeoutExpired:
            return "", "Timeout"
        except Exception as e:
            return "", str(e)

    def run_in_thread(self, target_func):
        threading.Thread(target=target_func, daemon=True).start()

    def get_installed_packages(self):
        out, _ = self.run_adb(["shell", "pm", "list", "packages"])
        pkgs = set()
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("package:"):
                pkgs.add(line.replace("package:", "").strip())
        return pkgs

    def on_connect_clicked(self):
        ip = self.ip_entry.get().strip()
        if not ip:
            messagebox.showerror("Error", self.t("enter_ip_err"))
            return

        def _worker():
            self.log(self.t("connecting").format(ip=ip))
            self.btn_connect.configure(state="disabled")

            cmd = [self.adb_bin, "connect", f"{ip}:5555"]
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                self.log(f"ADB: {res.stdout.strip()}")
            except Exception as e:
                self.log(f"Error: {e}")

            self.connected_ip = ip
            state, _ = self.run_adb(["get-state"])
            if state == "device":
                self.is_connected = True
                self.status_badge.configure(text=self.t("status_connected"), text_color="#10b981")
                self.log(self.t("conn_success"))

                brand, _ = self.run_adb(["shell", "getprop", "ro.product.brand"])
                mfg, _ = self.run_adb(["shell", "getprop", "ro.product.manufacturer"])
                model, _ = self.run_adb(["shell", "getprop", "ro.product.model"])
                android_ver, _ = self.run_adb(["shell", "getprop", "ro.build.version.release"])

                self.detected_brand = brand or mfg or "Unknown"
                self.detected_model = model or "Unknown"

                b_lower = f"{brand.lower()} {mfg.lower()} {model.lower()}"
                if "philips" in b_lower or "tpv" in b_lower:
                    self.detected_brand_key = "philips"
                elif "tcl" in b_lower:
                    self.detected_brand_key = "tcl"
                elif "xiaomi" in b_lower or "redmi" in b_lower or "mitv" in b_lower:
                    self.detected_brand_key = "xiaomi"
                elif "sony" in b_lower:
                    self.detected_brand_key = "sony"
                elif "vestel" in b_lower or "toshiba" in b_lower or "regal" in b_lower:
                    self.detected_brand_key = "vestel"
                else:
                    self.detected_brand_key = "generic"

                mem, _ = self.run_adb(["shell", "cat", "/proc/meminfo"])
                avail_ram = "Unknown"
                for line in mem.splitlines():
                    if "MemAvailable:" in line:
                        parts = line.split()
                        if len(parts) >= 2:
                            avail_kb = int(parts[1])
                            avail_ram = f"{round(avail_kb / 1024, 1)} MB"
                        break

                self.lbl_device_info.configure(
                    text=self.t("dev_info_fmt").format(
                        brand=self.detected_brand.upper(),
                        model=self.detected_model,
                        android=android_ver,
                        ram=avail_ram
                    )
                )
                self.update_device_info_labels()
            else:
                self.is_connected = False
                self.status_badge.configure(text=self.t("status_disconnected"), text_color="#ef4444")
                self.lbl_profile_badge.configure(text=self.t("profile_waiting"))
                self.log(self.t("conn_fail"))

            self.btn_connect.configure(state="normal")

        self.run_in_thread(_worker)

    def on_debloat_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        if not messagebox.askyesno("Confirm", self.t("debloat_confirm")):
            return

        def _worker():
            self.log(self.t("debloat_start"))
            self.log(self.t("scanning_pkgs"))
            installed_pkgs = self.get_installed_packages()
            self.log(self.t("found_pkgs").format(count=len(installed_pkgs)))

            target_list = list(UNIVERSAL_SAFE_DEBLOAT)
            target_list.extend(BRAND_DEBLOAT_PACKAGES.get(self.detected_brand_key, []))

            to_disable = []
            for pkg, desc in target_list:
                if pkg in UNIVERSAL_PROTECTED:
                    self.log(f"🛡️ PROTECTED: {pkg}")
                    continue
                if pkg in installed_pkgs:
                    to_disable.append((pkg, desc))

            if not to_disable:
                self.log(self.t("no_debloat"))
                messagebox.showinfo("Info", self.t("no_debloat"))
                return

            success_count = 0
            for pkg, desc in to_disable:
                out, err = self.run_adb(["shell", "pm", "disable-user", "--user", "0", pkg])
                if "disabled-user" in out or "new state" in out:
                    self.log(f"✅ Disabled: {pkg} ({desc})")
                    success_count += 1
                else:
                    self.log(f"ℹ️ {pkg} -> {out or err}")

            self.log(f"=== COMPLETED: {success_count} packages disabled ===")
            messagebox.showinfo("Success", self.t("debloat_done").format(count=success_count))

        self.run_in_thread(_worker)

    def on_anim_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        def _worker():
            self.log(self.t("anim_start"))
            self.run_adb(["shell", "settings", "put", "global", "window_animation_scale", "0.5"])
            self.run_adb(["shell", "settings", "put", "global", "transition_animation_scale", "0.5"])
            self.run_adb(["shell", "settings", "put", "global", "animator_duration_scale", "0.5"])
            self.log(self.t("anim_done"))
            messagebox.showinfo("Success", self.t("anim_done"))

        self.run_in_thread(_worker)

    def on_cache_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        def _worker():
            self.log(self.t("cache_start"))
            out, _ = self.run_adb(["shell", "pm", "trim-caches", "1000M"])
            self.log(f"{self.t('cache_done')} -> {out or 'OK'}")
            messagebox.showinfo("Success", self.t("cache_done"))

        self.run_in_thread(_worker)

    def on_switch_launcher_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        def _worker():
            self.log("Checking FLauncher...")
            installed_pkgs = self.get_installed_packages()

            if "me.efesser.flauncher" not in installed_pkgs:
                self.log("❌ FLauncher is NOT installed on TV!")
                messagebox.showerror("Error", self.t("flauncher_missing"))
                return

            self.log("✅ FLauncher found. Disabling stock launcher...")
            stock_launchers = ["com.google.android.tvlauncher", "com.google.android.apps.tv.launcherx"]
            for sl in stock_launchers:
                if sl in installed_pkgs:
                    out, _ = self.run_adb(["shell", "pm", "disable-user", "--user", "0", sl])
                    self.log(f"Disabled: {sl} -> {out}")

            self.run_adb(["shell", "am", "start", "-a", "android.intent.action.MAIN", "-c", "android.intent.category.HOME"])
            self.log("🎯 FLauncher activated!")
            messagebox.showinfo("Success", self.t("flauncher_done"))

        self.run_in_thread(_worker)

    def on_restore_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        if not messagebox.askyesno("Confirm", self.t("restore_confirm")):
            return

        def _worker():
            self.log(self.t("restore_start"))
            all_pkgs = set([pkg for pkg, _ in UNIVERSAL_SAFE_DEBLOAT])
            for brand_list in BRAND_DEBLOAT_PACKAGES.values():
                for pkg, _ in brand_list:
                    all_pkgs.add(pkg)
            all_pkgs.add("com.google.android.tvlauncher")
            all_pkgs.add("com.google.android.apps.tv.launcherx")

            count = 0
            for pkg in sorted(all_pkgs):
                out, _ = self.run_adb(["shell", "pm", "enable", pkg])
                if "new state" in out or "enabled" in out:
                    self.log(f"Restored: {pkg}")
                    count += 1

            self.log(f"=== RESTORE COMPLETED: {count} packages restored ===")
            messagebox.showinfo("Success", self.t("restore_done"))

        self.run_in_thread(_worker)

    def on_reboot_clicked(self):
        if not self.is_connected:
            messagebox.showwarning("Warning", self.t("need_connect"))
            return

        if not messagebox.askyesno("Reboot", self.t("reboot_confirm")):
            return

        def _worker():
            self.log(self.t("reboot_start"))
            self.run_adb(["reboot"])
            self.is_connected = False
            self.status_badge.configure(text=self.t("status_rebooting"), text_color="#f59e0b")

        self.run_in_thread(_worker)

if __name__ == "__main__":
    app = AndroidTVOptimizerApp()
    app.mainloop()
