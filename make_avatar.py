from PIL import Image, ImageDraw, ImageFont
import math

SS = 3
S = 800
W = H = S * SS
BG = (13, 13, 14)
GOLD = (201, 169, 110)
GOLD_SOFT = (175, 144, 92)
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts/"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)
cx, cy = W // 2, H // 2

# soft golden glow
glow = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(glow)
maxr = int(W * 0.55)
for i in range(maxr, 0, -2):
    a = int(26 * (1 - i / maxr))
    gd.ellipse([cx - i, cy - i, cx + i, cy + i], fill=a)
img = Image.composite(Image.new("RGB", (W, H), (60, 48, 26)), img, glow)
draw = ImageDraw.Draw(img)

lw = max(2, 3 * SS)

# thin gold ring near the edge (looks good in Etsy's circular crop)
m = int(40 * SS)
draw.ellipse([m, m, W - m, H - m], outline=GOLD_SOFT, width=max(2, 2 * SS))

# small floral emblem above the monogram
def petal(length, width, color, lw):
    pad = lw * 4
    p = Image.new("RGBA", (width + pad*2, length + pad*2), (0, 0, 0, 0))
    ImageDraw.Draw(p).ellipse([pad, pad, pad + width, pad + length],
                              outline=color + (255,), width=lw)
    return p

emblem_cy = int(H * 0.33)
flower = Image.new("RGBA", (W, H), (0, 0, 0, 0))
base = petal(int(60 * SS), int(26 * SS), GOLD, lw)
for k in range(6):
    ang = 60 * k
    rot = base.rotate(ang, expand=True, resample=Image.BICUBIC)
    off = int(60 * SS * 0.46)
    dx = math.sin(math.radians(ang)) * off
    dy = -math.cos(math.radians(ang)) * off
    flower.alpha_composite(rot, (int(cx + dx - rot.width/2), int(emblem_cy + dy - rot.height/2)))
img = Image.alpha_composite(img.convert("RGBA"), flower).convert("RGB")
draw = ImageDraw.Draw(img)
r = int(8 * SS)
draw.ellipse([cx - r, emblem_cy - r, cx + r, emblem_cy + r], fill=GOLD)

# big "A" monogram
mono = ImageFont.truetype(FONT_DIR + "Italiana-Regular.ttf", int(340 * SS))
b = draw.textbbox((0, 0), "A", font=mono)
aw, ah = b[2]-b[0], b[3]-b[1]
draw.text((cx - aw/2 - b[0], int(H*0.46) - b[1]), "A", font=mono, fill=GOLD)

# tiny AEVORI underneath
sub = ImageFont.truetype(FONT_DIR + "Italiana-Regular.ttf", int(46 * SS))
txt = "A E V O R I"
sb = draw.textbbox((0, 0), txt, font=sub)
draw.text((cx - (sb[2]-sb[0])/2 - sb[0], int(H*0.80)), txt, font=sub, fill=GOLD_SOFT)

final = img.resize((S, S), Image.LANCZOS)
final.save("/home/user/mein-erstes-pr-repo/aevori_avatar.png", "PNG")
print("saved", final.size)
