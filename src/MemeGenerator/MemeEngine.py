from PIL import Image, ImageDraw
import random
import os


class MemeEngine:
  def __init__(self, output_dir):
      self.output_dir = output_dir

  def make_meme(self, img_path, text, author, width=500) -> str: #generated image path
      im = Image.open(img_path)
      image_width, image_height = im.size
      new_width = min(width, 500)
      new_height = int((new_width / image_width) * image_height)

      out = im.resize((new_width, new_height))

      quote = self._formatQuote(text, author)

      draw = ImageDraw.Draw(out)

      text_anchor_pos = self._randomlyPositionText(out, draw, quote, image_width, image_height)

      draw.text(text_anchor_pos, quote, fill=(255,255,255,255))

      outfile = os.path.join(self.output_dir, f'{random.randint(1,10000000)}.png')
      out.save(outfile)

      return outfile

  def _formatQuote(self, body: str, author: str) -> str:
      return f'"{body}" - {author}'

  def _randomlyPositionText(self, image: Image, draw: ImageDraw, quote: str, width: int, height: int) -> tuple[int, int]:
      text_width, text_height = draw.textsize(quote)

      text_anchor_pos = (
        random.randint(0, image.width - text_width),
        random.randint(0, image.height - text_height)
      )

      return text_anchor_pos
