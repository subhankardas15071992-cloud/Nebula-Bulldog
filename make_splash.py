#!/usr/bin/env python3
"""Generate Nebula Bulldog splash screen images (oldschool console look).
No Rupert Neve imagery anywhere — purely a dark analog-console aesthetic."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 700, 460          # main splash
SW, SH = 420, 276        # small splash

def load_font(size, bold=True):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except Exception:
            continue
    return ImageFont.load_default()

def brushed_metal(x0, y0, x1, y1, base, direction="v"):
    """Draw a brushed-metal panel with subtle vertical/horizontal streaks."""
    img = Image.new("RGB", (x1 - x0, y1 - y0), base)
    px = img.load()
    w, h = img.size
    import random
    random.seed(42)
    for _ in range(w * h // 4):
        px = img.load()
        rx = random.randrange(w); ry = random.randrange(h)
        r, g, b = base
        dr = random.randint(-18, 18); dg = random.randint(-18, 18); db = random.randint(-18, 18)
        nr = min(255, max(0, r + dr)); ng = min(255, max(0, g + dg)); nb = min(255, max(0, b + db))
        px[rx, ry] = (nr, ng, nb)
    img = img.filter(ImageFilter.GaussianBlur(0.6))
    return img

def make_splash(w, h, out):
    # Dark analog console chassis
    bg = (26, 30, 34)
    panel = (44, 50, 58)
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)

    # Top rack rail
    d.rectangle([0, 0, w, 34], fill=(38, 44, 50))
    d.line([0, 34, w, 34], fill=(110, 120, 130), width=2)

    # Main console panel
    panel_img = brushed_metal(0, 0, w, h - 110, panel, direction="v")
    img.paste(panel_img, (0, 44))

    # Lower section (meter bridge area)
    d.rectangle([0, h - 110, w, h], fill=(34, 38, 44))
    d.line([0, h - 110, w, h - 110], fill=(90, 100, 110), width=2)

    # Decorative rack screws (corners)
    for (cx, cy) in [(24, 24), (w - 24, 24), (24, h - 24), (w - 24, h - 24)]:
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(150, 150, 150))
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(200, 200, 200))

    # VU meter (amber) - center left
    mx, my, mw, mh = 130, h - 90, 200, 70
    d.rounded_rectangle([mx, my, mx + mw, my + mh], 10, fill=(20, 18, 12), outline=(100, 90, 70), width=2)
    d.text((mx + 12, my + 8), "VU", fill=(200, 170, 60), font=load_font(22))
    # meter arc
    d.arc([mx + 30, my + 22, mx + mw - 30, my + mh - 22], 180, 0, fill=(220, 180, 70), width=4)
    d.line([mx + 90, my + mh - 22, mx + 100, my + mh - 32], fill=(220, 180, 70), width=4)  # needle
    d.text((mx + mw - 40, my + 8), "0", fill=(200, 170, 60), font=load_font(20))

    # Big title text - "Nebula Bulldog"
    title_font = load_font(56)
    sub_font = load_font(24)
    t = "Nebula Bulldog"
    tw = d.textlength(t, font=title_font)
    d.text(((w - tw) / 2, 150), t, fill=(232, 232, 224), font=title_font)

    # Subtitle
    sub = "Oldschool Console Edition"
    sw = d.textlength(sub, font=sub_font)
    d.text(((w - sw) / 2, 220), sub, fill=(170, 160, 130), font=sub_font)

    # Loading line
    load_font_small = load_font(16)
    ld = "loading ..."
    lw = d.textlength(ld, font=load_font_small)
    d.text(((w - lw) / 2, h - 48), ld, fill=(140, 150, 160), font=load_font_small)

    img.save(out, "PNG")
    print("wrote", out, img.size)

make_splash(W, H, "gtk2_ardour/resources/Nebula Bulldog-splash.png")
make_splash(SW, SH, "gtk2_ardour/resources/Nebula Bulldog-small-splash.png")
