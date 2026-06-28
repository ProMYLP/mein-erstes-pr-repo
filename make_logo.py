from PIL import Image, ImageDraw, ImageFont
import math

# ---- Settings ----
SS = 3                      # supersampling for smooth edges
S = 1000                    # final size (square)
W = H = S * SS
BG = (13, 13, 14)           # deep black
GOLD = (201, 169, 110)      # brushed gold
GOLD_SOFT = (175, 144, 92)
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts/"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

cx = W // 2

# ---- Subtle radial golden glow in the center ----
glow = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(glow)
maxr = int(W * 0.55)
for i in range(maxr, 0, -2):
    a = int(22 * (1 - i / maxr))
    gd.ellipse([cx - i, H//2 - i, cx + i, H//2 + i], fill=a)
glow_layer = Image.new("RGB", (W, H), (60, 48, 26))
img = Image.composite(glow_layer, img, glow)
draw = ImageDraw.Draw(img)

# ================= Floral emblem (top center) =================
emblem_cy = int(H * 0.30)
lw = max(2, 3 * SS)

def petal(length, width, color, lw):
    """Return an RGBA petal (thin outlined ellipse) drawn vertically."""
    pad = lw * 4
    pw, ph = width + pad * 2, length + pad * 2
    p = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    pd = ImageDraw.Draw(p)
    pd.ellipse([pad, pad, pad + width, pad + length], outline=color + (255,), width=lw)
    return p

# Flower: petals radiating around the center
n_petals = 6
plen, pwid = int(78 * SS), int(34 * SS)
flower = Image.new("RGBA", (W, H), (0, 0, 0, 0))
base_petal = petal(plen, pwid, GOLD, lw)
for k in range(n_petals):
    ang = 360 / n_petals * k
    rot = base_petal.rotate(ang, expand=True, resample=Image.BICUBIC)
    # position so the petal's inner tip sits near the flower center
    off = int(plen * 0.46)
    dx = math.sin(math.radians(ang)) * off
    dy = -math.cos(math.radians(ang)) * off
    px = int(cx + dx - rot.width / 2)
    py = int(emblem_cy + dy - rot.height / 2)
    flower.alpha_composite(rot, (px, py))
img.paste(Image.alpha_composite(img.convert("RGBA"), flower).convert("RGB"), (0, 0))
draw = ImageDraw.Draw(img)

# small center circle
r = int(12 * SS)
draw.ellipse([cx - r, emblem_cy - r, cx + r, emblem_cy + r], outline=GOLD, width=lw)
draw.ellipse([cx - r//3, emblem_cy - r//3, cx + r//3, emblem_cy + r//3], fill=GOLD)

# Symmetric curved leaf stems sweeping down from the flower
def leaf_stem(direction):
    # quadratic-ish curve via points
    pts = []
    for t in [i / 40 for i in range(41)]:
        x = cx + direction * (t * 150 * SS)
        y = emblem_cy + plen * 0.6 + (t * t) * 120 * SS
        pts.append((x, y))
    draw.line(pts, fill=GOLD_SOFT, width=lw, joint="curve")
    # small leaves along the stem
    for tt in [0.45, 0.75]:
        x = cx + direction * (tt * 150 * SS)
        y = emblem_cy + plen * 0.6 + (tt * tt) * 120 * SS
        lf = petal(int(40 * SS), int(16 * SS), GOLD_SOFT, max(2, 2 * SS))
        lf = lf.rotate(-direction * 55 + (0 if direction > 0 else 0), expand=True, resample=Image.BICUBIC)
        img.paste(img.convert("RGBA").alpha_composite(Image.new("RGBA",(1,1))) or img, (0,0)) if False else None
        img.alpha_composite if False else None
        # paste leaf
        base = Image.new("RGBA", (W, H), (0,0,0,0))
        base.alpha_composite(lf, (int(x - lf.width/2), int(y - lf.height/2)))
        merged = Image.alpha_composite(img.convert("RGBA"), base).convert("RGB")
        img.paste(merged, (0,0))

leaf_stem(1)
leaf_stem(-1)
draw = ImageDraw.Draw(img)

# ================= Brand name "AEVORI" =================
def load(path, size):
    return ImageFont.truetype(FONT_DIR + path, size)

name_font = load("Italiana-Regular.ttf", int(150 * SS))
name = "AEVORI"
tracking = int(34 * SS)   # letter spacing

# measure total width
widths = []
for ch in name:
    bbox = draw.textbbox((0, 0), ch, font=name_font)
    widths.append(bbox[2] - bbox[0])
total = sum(widths) + tracking * (len(name) - 1)

name_y = int(H * 0.56)
x = cx - total // 2
for ch, wch in zip(name, widths):
    bbox = draw.textbbox((0, 0), ch, font=name_font)
    draw.text((x - bbox[0], name_y), ch, font=name_font, fill=GOLD)
    x += wch + tracking

# ================= Subtitle "AFFIRMATION ART" with side rules =================
sub_font = load("Italiana-Regular.ttf", int(40 * SS))
sub = "A R T   P R I N T S   &   G I F T S"
sb = draw.textbbox((0, 0), sub, font=sub_font)
sub_w = sb[2] - sb[0]
sub_y = int(H * 0.75)
draw.text((cx - sub_w // 2 - sb[0], sub_y), sub, font=sub_font, fill=GOLD_SOFT)

# thin gold rules on each side of subtitle
line_y = sub_y + (sb[3] - sb[1]) // 2
gap = int(40 * SS)
rule_len = int(90 * SS)
draw.line([(cx - sub_w//2 - gap - rule_len, line_y), (cx - sub_w//2 - gap, line_y)], fill=GOLD_SOFT, width=max(1, 2*SS))
draw.line([(cx + sub_w//2 + gap, line_y), (cx + sub_w//2 + gap + rule_len, line_y)], fill=GOLD_SOFT, width=max(1, 2*SS))

# ---- Downscale for anti-aliasing ----
final = img.resize((S, S), Image.LANCZOS)
final.save("/home/user/mein-erstes-pr-repo/aevori_logo.png", "PNG")
print("saved aevori_logo.png", final.size)
