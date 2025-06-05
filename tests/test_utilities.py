import os
from modules.utilities import has_image_extension, is_image, is_video


def test_has_image_extension():
    assert has_image_extension("test.png")
    assert has_image_extension("photo.JPG")
    assert has_image_extension("picture.jpeg")
    assert not has_image_extension("movie.mp4")
    assert not has_image_extension("archive.tar.gz")


def test_is_image(tmp_path):
    img_file = tmp_path / "image.png"
    img_file.write_bytes(b"dummy")
    assert is_image(str(img_file))
    other = tmp_path / "clip.mp4"
    other.write_bytes(b"dummy")
    assert not is_image(str(other))
    assert not is_image(str(tmp_path / "missing.png"))


def test_is_video(tmp_path):
    vid_file = tmp_path / "video.mp4"
    vid_file.write_bytes(b"dummy")
    assert is_video(str(vid_file))
    other = tmp_path / "image.jpg"
    other.write_bytes(b"dummy")
    assert not is_video(str(other))
    assert not is_video(str(tmp_path / "missing.mp4"))
