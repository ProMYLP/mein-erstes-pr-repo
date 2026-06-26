from PIL import Image, ImageDraw, ImageFont
import math

# ---- Settings ----
SS = 2
W0, H0 = 3360, 840          # Etsy big banner (4:1)
W, H = W0 * SS, H0 * SS
BG = (13, 13, 14)
GOLD = (201, 169, 110)
GOLD_SOFT = (170, 140, 90)
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts/"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)
cx, cy = W // 2, H // 2

# ---- soft golden glow center ----
glow = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(glow)
maxr = int(W * 0.32)
for i in range(maxr, 0, -3):
    a = int(20 * (1 - i / maxr))
    gd.ellipse([cx - i*2, cy - i, cx + i*2, cy + i], fill=a)
img = Image.composite(Image.new("RGB", (W, H), (60, 48, 26)), img, glow)
draw = ImageDraw.Draw(img)

lw = max(2, 2 * SS)

def petal(length, width, color, lw):
    pad = lw * 4
    p = Image.new("RGBA", (width + pad*2, length + pad*2), (0, 0, 0, 0))
    ImageDraw.Draw(p).ellipse([pad, pad, pad + width, pad + length],
                              outline=color + (255,), width=lw)
    return p

def flower(center_x, center_y, plen, pwid, n=6, color=GOLD):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    base = petal(plen, pwid, color, lw)
    for k in range(n):
        ang = 360 / n * k
        rot = base.rotate(ang, expand=True, resample=Image.BICUBIC)
        off = int(plen * 0.46)
        dx = math.sin(math.radians(ang)) * off
        dy = -math.cos(math.radians(ang)) * off
        layer.alpha_composite(rot, (int(center_x + dx - rot.width/2),
                                    int(center_y + dy - rot.height/2)))
    return layer

def draw_sprig(anchor_x, direction):
    """Curved floral sprig sweeping inward toward the center text."""
    global img, draw
    layer = flower(anchor_x, cy, int(70*SS), int(30*SS))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    draw = ImageDraw.Draw(img)
    r = int(9*SS)
    draw.ellipse([anchor_x-r, cy-r, anchor_x+r, cy+r], outline=GOLD, width=lw)
    # two curved stems with little leaves, going up and down
    for vdir in (-1, 1):
        pts = []
        for t in [i/40 for i in range(41)]:
            x = anchor_x + direction * (t * 230 * SS)
            y = cy + vdir * (t * 150 * SS) + direction*0  # arc
            y = cy + vdir * math.sin(t*math.pi*0.5) * 150 * SS
            pts.append((x, y))
        draw.line(pts, fill=GOLD_SOFT, width=lw, joint="curve")
        for tt in (0.5, 0.8):
            x = anchor_x + direction * (tt * 230 * SS)
            y = cy + vdir * math.sin(tt*math.pi*0.5) * 150 * SS
            lf = petal(int(34*SS), int(13*SS), GOLD_SOFT, lw).rotate(
                direction*40*vdir, expand=True, resample=Image.BICUBIC)
            base = Image.new("RGBA", (W, H), (0,0,0,0))
            base.alpha_composite(lf, (int(x-lf.width/2), int(y-lf.height/2)))
            img = Image.alpha_composite(img.convert("RGBA"), base).convert("RGB")
    draw = ImageDraw.Draw(img)

# place a floral sprig left and right of the title
draw_sprig(int(W*0.30), -1)
draw_sprig(int(W*0.70), 1)

def load(p, s):
    return ImageFont.truetype(FONT_DIR + p, s)

# ---- Title AEVORI ----
name_font = load("Italiana-Regular.ttf", int(165 * SS))
name = "AEVORI"
tracking = int(40 * SS)
widths = []
for ch in name:
    b = draw.textbbox((0,0), ch, font=name_font); widths.append(b[2]-b[0])
total = sum(widths) + tracking*(len(name)-1)
ny = int(H*0.30)
x = cx - total//2
for ch, wch in zip(name, widths):
    b = draw.textbbox((0,0), ch, font=name_font)
    draw.text((x - b[0], ny), ch, font=name_font, fill=GOLD)
    x += wch + tracking

# ---- Tagline ----
sub_font = load("Italiana-Regular.ttf", int(52 * SS))
sub = "P O S I T I V E   A F F I R M A T I O N   W A L L   A R T   &   G I F T S"
sb = draw.textbbox((0,0), sub, font=sub_font)
sw = sb[2]-sb[0]
sy = int(H*0.62)
draw.text((cx - sw//2 - sb[0], sy), sub, font=sub_font, fill=GOLD_SOFT)
# rules around tagline
ly = sy + (sb[3]-sb[1])//2
gap = int(45*SS); rl = int(110*SS)
draw.line([(cx-sw//2-gap-rl, ly),(cx-sw//2-gap, ly)], fill=GOLD_SOFT, width=lw)
draw.line([(cx+sw//2+gap, ly),(cx+sw//2+gap+rl, ly)], fill=GOLD_SOFT, width=lw)

final = img.resize((W0, H0), Image.LANCZOS)
final.save("/home/user/mein-erstes-pr-repo/aevori_banner.png", "PNG")
print("saved", final.size)
