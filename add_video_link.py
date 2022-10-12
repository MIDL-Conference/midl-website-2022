#!/usr/bin/env python3.10

import json
from typing import Union
from pathlib import Path

if __name__ == "__main__":
        papers: dict[str, dict[str, Union[str, int]]]

        with open("long_papers.json", 'r') as f:
                papers = json.load(f)

        # with open("short_papers.json", 'r') as f:
        #         papers |= json.load(f)

        # Let's be dirty here..
        live_talks: list[int] = [113, 137, 16, 198, 230, 256, 45, 58, 64, 85, 95,
                                 122, 163, 173, 209, 23, 286, 52, 61, 67, 91, 9,
                                 130, 166, 18, 213, 24, 35, 57, 62, 84, 94]

        # print(papers.keys())
        k: str
        v: dict
        num: int
        for k, v in papers.items():
                paper_page: Path = (Path("pages/papers") / k).with_suffix(".md")
                with open(paper_page, 'r') as tap:
                        content: str = tap.read()

                # sub_folder: str = 'short' if '_S_' in k else 'long'
                # video_str: str = f'''{{{{ macros.video("https://video.midl.io/2022/{sub_folder}/{v['id']}.mp4") }}}}'''
                video_str: str = ""
                if v['id'] in live_talks:
                        video_str += f'''\n{{{{ macros.video("https://video.midl.io/2022/live/{v['id']}.mp4") }}}}'''

                print(video_str)
                # content = content.replace("<!-- {{ macros.presentation('', '', 720, 450) }} -->", video_str)
                # content = content.replace("<!-- { macros.presentation('', '', 720, 450) } -->", video_str)
                content += video_str
                # print(content)

                with open(paper_page, 'w') as sink:
                        sink.write(content)
