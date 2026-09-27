# -*- coding: utf-8 -*-
"""生成小站图标：粉色圆角方块 + 白色爱心 + 蝴蝶结"""
from PIL import Image, ImageDraw

def make(size, path):
    S = size * 4  # 4 倍超采样再缩小，边缘更顺滑
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # 渐变背景（上浅下深）
    grad = Image.new('RGB', (S, S))
    gd = ImageDraw.Draw(grad)
    for y in range(S):
        t = y / S
        r = int(255 * (1 - t) + 255 * t)
        g = int(158 * (1 - t) + 95 * t)
        b = int(196 * (1 - t) + 158 * t)
        gd.line([(0, y), (S, y)], fill=(r, g, b))
    mask = Image.new('L', (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
    img.paste(grad, (0, 0), mask)
    d = ImageDraw.Draw(img)

    # 白色爱心
    cx, cy, k = S * 0.5, S * 0.46, S * 0.22
    d.ellipse([cx - k, cy - k * 0.95, cx, cy + k * 0.15], fill=(255, 255, 255, 255))
    d.ellipse([cx, cy - k * 0.95, cx + k, cy + k * 0.15], fill=(255, 255, 255, 255))
    d.polygon([(cx - k * 0.99, cy - k * 0.12), (cx + k * 0.99, cy - k * 0.12), (cx, cy + k * 1.25)],
              fill=(255, 255, 255, 255))

    # 右上角小蝴蝶结
    bx, by, s2 = S * 0.74, S * 0.24, S * 0.075
    d.polygon([(bx, by), (bx - s2 * 1.5, by - s2), (bx - s2 * 1.5, by + s2)], fill=(255, 95, 158, 255))
    d.polygon([(bx, by), (bx + s2 * 1.5, by - s2), (bx + s2 * 1.5, by + s2)], fill=(255, 95, 158, 255))
    d.ellipse([bx - s2 * 0.55, by - s2 * 0.55, bx + s2 * 0.55, by + s2 * 0.55], fill=(255, 255, 255, 255))

    img.resize((size, size), Image.LANCZOS).save(path, 'PNG')
    print('已生成', path)

base = r'C:\Users\朱景澈\Desktop\love-site'
make(512, base + r'\icon-512.png')
make(192, base + r'\icon-192.png')
make(180, base + r'\apple-touch-icon.png')
