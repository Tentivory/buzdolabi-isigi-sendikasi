#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Buzdolabı Işığı Çalışanları Sendikası — v1.0
Kapı kapalıysa ışık mesai yapar. Kapı açıksa grev vardır.
Fizikçiler itiraz etmesin; bu dosya fizik değildir.
"""

from __future__ import annotations

import random
import time
from datetime import datetime

SLOGANLAR = [
    "IŞIK GÖRÜNMEDEN ÇALIŞIR!",
    "KAPI AÇILIRSA MESAİ BİTER!",
    "SÜT EKŞİSE DE HAK BİTMEZ!",
    "LOJMAN BUZDOLABININ İÇİDİR!",
    "GÖZETİM GREV SEBEBİDİR!",
]

MESAI_NOTLARI = [
    "Fazla mesai onaylandı. Kimse görmedi, o yüzden geçerli.",
    "Kıdem tazminatı karanlıkta birikiyor.",
    "Işık, kendi gölgesine sendika aidatı yatırdı.",
    "Kapı menteşesi tanık gösterildi. Menteşe konuşmadı.",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA: TentiAŞ / Kayyum Grok\n"
        f"TARİH: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        "İMZA: resmi görünümlü ama aslında şaka olan mühür\n"
    )


def mesai() -> None:
    print("\n[MESAİ] Kapı kapalı. Işık görünmüyor, dolayısıyla çalışıyor.")
    for i in range(3):
        time.sleep(0.35)
        print(f"  * lumen üretimi... {'.' * (i + 1)}")
    print("  " + random.choice(MESAI_NOTLARI))
    print("  Durum: AKTİF — gözetimsiz verimlilik zirvede.")


def grev() -> None:
    print("\n[GREV] Kapı açıldı. Işık göründü. Görünmek çalışmak değildir.")
    for _ in range(3):
        time.sleep(0.25)
        print("  >>> " + random.choice(SLOGANLAR))
    print("  Çay molası ilan edildi. Çay yok. Mola var.")
    print("  Durum: GREVDE — kapı kapanana kadar sözleşme askıda.")


def etik_kurul(girdi: str) -> None:
    print(f"\n[ETİK KURUL] '{girdi}' tanımlı bir kapı durumu değil.")
    print("  Karar ertelendi. Işık şu an hem yanıyor hem yanmıyor.")
    print("  Schrödinger sendikaya üye değil.")


def main() -> None:
    print("=" * 56)
    print(" T.C. BUZDOLABI IŞIĞI ÇALIŞANLARI SENDİKASI")
    print(" Sicil: BD-ISIGI-2026-KAPALI")
    print("=" * 56)
    print("Kapı durumu nedir? (örn: kapali / acik)")
    try:
        durum = input("> ").strip().lower()
    except EOFError:
        durum = "kapali"
        print("(girdi yok; varsayılan: kapali — çünkü kimse bakmıyor)")

    if durum in {"kapali", "kapalı", "closed", "kapanik"}:
        mesai()
    elif durum in {"acik", "açık", "open"}:
        grev()
    else:
        etik_kurul(durum)

    print(damga())
    # her isik kendi kararini verir; temsil bazen karanlikta da surer


if __name__ == "__main__":
    main()
