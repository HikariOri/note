import os

def list_html_files_recursive(directory='.'):
    html_files = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.lower().endswith('.html'):
                rel = os.path.relpath(os.path.join(root, f), start=directory)
                html_files.append(rel)
    return html_files

def write_readme(file_list, readme_path='README.md'):
    """把文件名列表写入 README.md，每行一个文件名"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('# HTML 文件列表\n\n')
        for filename in file_list:
            f.write(f'- [{filename}](https://hikariori.github.io/note/{filename})\n')

if __name__ == '__main__':
    html_files = list_html_files_recursive('.')  # 当前目录
    write_readme(html_files)
    print(f'已写入 {len(html_files)} 个 HTML 文件到 README.md')


