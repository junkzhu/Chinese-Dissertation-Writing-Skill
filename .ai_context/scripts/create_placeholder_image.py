#!/usr/bin/env python3
"""
创建空白占位图片，用于论文写作时预留图片位置。

用法:
  python create_placeholder_image.py <输出路径> [选项]
  python create_placeholder_image.py figures/related_work_lightmap_vlm.png
  python create_placeholder_image.py figures/图1.png -w 800 -H 500 -t "待添加"
  python create_placeholder_image.py figures/placeholder.png --plain  # 纯灰色无文字

示例（批量创建 related_work.tex 中的占位图）:
  python create_placeholder_image.py figures/related_work_lightmap_vlm.png
  python create_placeholder_image.py figures/related_work_neural.png
  python create_placeholder_image.py figures/related_work_lsvb.png
  ...

依赖: Pillow (pip install Pillow)
"""
import sys
import os
import argparse

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: 'Pillow' 未安装，请运行 'pip install Pillow'")
    sys.exit(1)


def create_placeholder(
    output_path: str,
    width: int = 800,
    height: int = 500,
    label: str | None = None,
    plain: bool = False,
) -> None:
    """创建占位图片。"""
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # 浅灰背景 (RGB 245,245,245)
    img = Image.new("RGB", (width, height), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)

    if not plain:
        # 绘制虚线边框
        border_color = (200, 200, 200)
        for x in range(0, width, 20):
            draw.line([(x, 0), (min(x + 10, width), 0)], fill=border_color, width=1)
            draw.line([(x, height - 1), (min(x + 10, width), height - 1)], fill=border_color, width=1)
        for y in range(0, height, 20):
            draw.line([(0, y), (0, min(y + 10, height))], fill=border_color, width=1)
            draw.line([(width - 1, y), (width - 1, min(y + 10, height))], fill=border_color, width=1)

        # 显示文件名或自定义标签
        text = label if label else os.path.basename(output_path)
        text_color = (180, 180, 180)

        try:
            # 尝试使用系统字体
            font_size = min(width, height) // 25
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except OSError:
                try:
                    font = ImageFont.truetype("C:\\Windows\\Fonts\\msyh.ttc", font_size)
                except OSError:
                    font = ImageFont.load_default()
        except Exception:
            font = ImageFont.load_default()

        # 简单居中
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (width - tw) // 2
        y = (height - th) // 2
        draw.text((x, y), text, fill=text_color, font=font)

    img.save(output_path)
    print(f"已创建占位图: {output_path} ({width}x{height})")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="创建空白占位图片，用于论文写作时预留图片位置",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "output",
        help="输出图片路径，如 figures/related_work_xxx.png",
    )
    parser.add_argument("-w", "--width", type=int, default=800, help="图片宽度（默认 800）")
    parser.add_argument("-H", "--height", type=int, default=500, help="图片高度（默认 500）")
    parser.add_argument("-t", "--text", type=str, default=None, help="占位图上的文字（默认用文件名）")
    parser.add_argument(
        "--plain",
        action="store_true",
        help="纯灰色无边框无文字",
    )
    args = parser.parse_args()

    if args.width < 1 or args.height < 1:
        print("Error: 宽高必须为正整数")
        sys.exit(1)

    create_placeholder(
        output_path=args.output,
        width=args.width,
        height=args.height,
        label=args.text,
        plain=args.plain,
    )


if __name__ == "__main__":
    main()
