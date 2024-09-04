import os
import json

def read_file(file_path: str) -> list[str]:
    """
    Reads a file and returns its content as a list of lines.
    
    Parameters:
    - file_path: str - Path to the file
    
    Returns:
    - list[str] - List of lines in the file
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(file_path: str, data: dict):
    """
    Writes data to a JSON file.
    
    Parameters:
    - file_path: str - Path to the output file
    - data: dict - Data to write to the file
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_sorted_directory_list(dir_path: str) -> list[str]:
    """
    Returns a sorted list of directory names in a specified path.
    
    Parameters:
    - dir_path: str - Path to the directory
    
    Returns:
    - list[str] - Sorted list of directory names
    """
    def convert_int(item: str) -> int:
        if item.isdigit():
            return int(item)
        elif '-' in item and item.split('-')[0].strip().isdigit():
            return int(item.split('-')[0])
        elif '.' in item and item.split('.')[0].isdigit():
            return int(item.split('.')[0])
        elif '_' in item and item.split('_')[0].isdigit():
            return int(item.split('_')[0])
        return 0
        
    return sorted(os.listdir(dir_path), key=lambda item: convert_int(item))

def process_directory(path_name: str, list_dir: list[str]) -> list[dict]:
    """
    Processes the directories and files, extracting information and structuring it.
    
    Parameters:
    - path_name: str - Base path to the directories
    - list_dir: list[str] - List of directories to process
    
    Returns:
    - list[dict] - Processed data in structured form
    """
    data = []
    cntl, cntdl = 0, 0

    for directory in list_dir:
        list_in_dir = get_sorted_directory_list(path_name + directory)
        info = {
            "title": directory,
            "param": f"chap-{cntl}-{cntdl}",
            "list": []
        }
        for file_in_dir in list_in_dir:
            file_path = f"{path_name}{directory}/{file_in_dir}"
            file_content = read_file(file_path)
            inner_info = {
                "author": "Dev Alex",
                "title": file_content[0].strip().replace("# ", "") if file_content else "No title",
                "param": f"chap-{cntl}-{cntdl}",
                "level": "beginner",
                "code": '\n'.join(file_content),
            }
            info["list"].append(inner_info)
            cntdl += 1
        
        cntl += 1
        cntdl = 0
        data.append(info)
    
    return data


def gen_chapter_lesson(path_name: str, list_dir: list[str]) -> list[dict]:
    """
    Processes the directories and files, extracting information and structuring it.
    
    Parameters:
    - path_name: str - Base path to the directories
    - list_dir: list[str] - List of directories to process
    
    Returns:
    - list[dict] - Processed data in structured form
    """
    data_chapter = []
    data_lesson = []
    cntl, cntdl = 1, 1

    for directory in list_dir:
        list_in_dir = get_sorted_directory_list(path_name + directory)
        info = {
            "model": "app_v1.chapter",
            "pk": cntl,
            "fields": {
                "name": directory,
                "content": "",
                "lessons": []
            },
        }
        for file_in_dir in list_in_dir:
            file_path = f"{path_name}{directory}/{file_in_dir}"
            file_content = read_file(file_path)
            inner_info = {
                "model": "app_v1.lesson",
                "pk": cntdl,
                "fields": {
                    "name": file_content[0].strip().replace("# ", "") if file_content else "No title",
                    "content": ''.join(file_content),
                    "reviews": [],
                    "exercises": []
                },
            }
            info["fields"]["lessons"].append(cntdl)
            cntdl += 1
            data_lesson.append(inner_info)
        
        cntl += 1
        # cntdl = 0
        data_chapter.append(info)
    
    return data_chapter, data_lesson



def main(path_name: str):
    """
    Main function to execute the processing and writing of data.
    
    Parameters:
    - path_name: str - Base path to the directories
    """
    list_dir = get_sorted_directory_list(path_name)
    print(list_dir)
    
    data = gen_chapter_lesson(path_name, list_dir)

    write_file('./export/chapter.json', data[0])
    write_file('./export/lesson.json', data[1])

if __name__ == "__main__":
    main('./data/python/')
