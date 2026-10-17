import io
import csv
import runpy
from pathlib import Path
from unittest.mock import MagicMock, patch
import subprocess
import pytest

def execute(rows, fail=False):
    data = io.StringIO()
    csv.writer(data).writerows(rows)
    with patch.dict('sys.modules', {'pyautogui':MagicMock()}), patch('builtins.open', return_value=io.StringIO(data.getvalue())), patch('subprocess.run') as run:
        if fail:
            run.side_effect = subprocess.CalledProcessError(1, 'ffmpeg')
        runpy.run_path(str(Path(__file__).resolve().parents[1] / 'ffmpegDownload.py'))
        return run

def test_header_is_not_downloaded():
    assert execute([['a','b','c','d','e','url','name','manifest']]).call_count == 0

def test_download_uses_manifest_and_filename_for_each_row():
    run = execute([['header']*8, ['','','','','','https://example.test','lesson1','https://example.test/a.m3u8'], ['','','','','','https://example.test','lesson2','https://example.test/b.m3u8']])
    assert run.call_count == 2
    assert run.call_args_list[0].args[0][2] == 'https://example.test/a.m3u8'
    assert run.call_args_list[0].args[0][-1].endswith('lesson1.mp4')
    assert run.call_args_list[1].args[0][-1].endswith('lesson2.mp4')
    assert all(call.kwargs['check'] is True for call in run.call_args_list)

def test_ffmpeg_failure_is_not_silenced():
    with pytest.raises(subprocess.CalledProcessError):
        execute([['header']*8, ['','','','','','','lesson','https://example.test/a.m3u8']], fail=True)

def test_spaces_and_shell_characters_remain_literal_arguments():
    manifest = 'https://example.test/video.m3u8?token=a&quality=high'
    filename = 'Lesson 1 & introduction'
    run = execute([['header'] * 8, ['', '', '', '', '', '', filename, manifest]])
    args = run.call_args.args[0]
    assert isinstance(args, list)
    assert args[:5] == ['ffmpeg', '-i', manifest, '-c', 'copy']
    assert args[5].endswith(filename + '.mp4')
    assert run.call_args.kwargs.get('shell', False) is False
