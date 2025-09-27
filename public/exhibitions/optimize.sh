#!/bin/bash
# Recursively optimize images and generate WebP only if smaller
# Resize images to max 2000px width or height
# Requires: imagemagick (convert), optipng, gifsicle, cwebp

MAX_DIM=2000

find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.gif' \) | while read -r f; do
  case "${f,,}" in
    *.jpg|*.jpeg)
      # Resize if larger than MAX_DIM
      convert "$f" -resize "${MAX_DIM}x${MAX_DIM}>" -sampling-factor 4:2:0 -strip -quality 90 -interlace JPEG -colorspace RGB "$f"
      # Generate WebP temporarily
      cwebp -q 90 -m 6 "$f" -o temp.webp
      [ $(stat -c%s temp.webp) -lt $(stat -c%s "$f") ] && mv temp.webp "${f%.*}.webp" || rm temp.webp
      ;;
    *.png)
      optipng -o7 "$f"
      convert "$f" -resize "${MAX_DIM}x${MAX_DIM}>" "$f"
      cwebp -q 90 -m 6 "$f" -o temp.webp
      [ $(stat -c%s temp.webp) -lt $(stat -c%s "$f") ] && mv temp.webp "${f%.*}.webp" || rm temp.webp
      ;;
    *.gif)
      gifsicle -O3 "$f" -o "$f"
      convert "$f" -resize "${MAX_DIM}x${MAX_DIM}>" "$f"
      cwebp -q 90 -m 6 "$f" -o temp.webp
      [ $(stat -c%s temp.webp) -lt $(stat -c%s "$f") ] && mv temp.webp "${f%.*}.webp" || rm temp.webp
      ;;
  esac
done
