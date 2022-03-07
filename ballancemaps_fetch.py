from traceback import print_exception
from requests import get
from re import findall, search


username = "ballancemaps"
index_link = f"http://cc.ysepan.com/f_ht/ajcx/ml.aspx?cz=ml_dq&_dlmc={username}&_dlmm="
filelist_link = f"http://cc.ysepan.com/f_ht/ajcx/wj.aspx?cz=dq&jsq=0&mlbh=%s&wjpx=1&_dlmc={username}&_dlmm="
indexes = []
map_list = {}


def refresh():
  global indexes, map_list
  indexes = []
  map_list = {}


def get_group_indexes(pattern_str):
  global indexes
  if len(indexes) == 0:
    html_string = get_ys_html(index_link)
    indexes = list(map(
      lambda matches: {
        "id": matches[0],
        "name": matches[1],
        "notes": matches[2]
      },
      findall(
        r'<li[^<>]+id="ml_([0-9]+)"[^<>]*>.*?<a [^<>]*>([^<>]+)</a><label>([^<>]+)?</label>.*?</li>',
        html_string
      )
    ))

  matched_indexes = []
  for index in indexes:
    if search(pattern_str, index["name"]):
      matched_indexes.append(index)

  return matched_indexes


def get_map_list(index):
  def difficulty_to_number(difficulty: str):
    count = difficulty.count("★")
    if count == 0: count = -1
    return count

  global map_list
  if index not in map_list or len(index) == 0:
    html_string = get_ys_html(filelist_link % index)
    map_list[index] = list(map(
      lambda matches: {
        "name": matches[1],
        "url": matches[0],
        "size": matches[2],
        "author": matches[3],
        "difficulty": difficulty_to_number(matches[4]),
        "notes": matches[5],
        "upload_time": matches[6]
      },
      findall(
        r'<li(?:[^<>]+)>.*?<a[^<>]+?href="([^">]+)"(?:[^<>]+)?>([^<>]+)<\/a><i>([^<]+)<\/i><b>\s*([^\s|<>]+(?:\s+[^\s|<>]+)*)?\s*\|?\s*([^\s|<>]+(?:\s+[^\s|<>]+)*)?\s*\|?\s*([^\s|<>]+(?:\s+[^\s|<>]+)*)?\s*<\/b><span(?:[^<>]+)>([^<>]+)<\/span>.*?<\/a><\/li>',
        html_string
      )
    ))
  
  return map_list[index]


def get_ys_html(url):
  response_string = ""
  try:
    response_string = get(url, headers={"Referer": 'http://cg.ys168.com/f_ht/ajcx/000ht.html?bbh=1134'}).text
  except Exception as e:
    print_exception(e)
  return response_string


def main():
  def print_lines():
    print('-' * 24)

  print_lines()
  pattern = input("要获取的目录名称样式: ")
  print("\n".join([str(index) for index in get_group_indexes(pattern)]))
  print_lines()
  selected_index = input("要获取的目录 id: ")
  print("\n".join([str(map) for map in get_map_list(selected_index)]))
  print_lines()


if __name__ == '__main__':
  main()
