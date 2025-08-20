import argparse
import json
import os
import zipfile
from typing import Dict

def _collect_assets(data: Dict) -> Dict[str, str]:
    """Return mapping of asset file names to human friendly names."""
    assets: Dict[str, str] = {}
    for target in data.get('targets', []):
        for key in ('costumes', 'sounds'):
            for item in target.get(key, []):
                md5ext = item.get('md5ext')
                name = item.get('name', '')
                if md5ext and name:
                    ext = os.path.splitext(md5ext)[1]
                    assets[md5ext] = f"{name}{ext}"
    return assets

def extract_sb3_assets(sb3_file: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(sb3_file) as zf:
        project_json = json.loads(zf.read('project.json'))
        assets = _collect_assets(project_json)
        # save project.json
        with open(os.path.join(output_dir, 'project.json'), 'wb') as f:
            f.write(zf.read('project.json'))
        for md5ext, filename in assets.items():
            data = zf.read(md5ext)
            target = os.path.join(output_dir, filename)
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(target):
                target = os.path.join(output_dir, f"{base}_{counter}{ext}")
                counter += 1
            with open(target, 'wb') as f:
                f.write(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract assets from a Scratch SB3 file')
    parser.add_argument('sb3_file', help='Path to the .sb3 file')
    parser.add_argument('output_dir', help='Directory to extract assets into')
    args = parser.parse_args()
    extract_sb3_assets(args.sb3_file, args.output_dir)
