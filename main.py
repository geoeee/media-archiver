
import click
import os


def scandir(path):
  os.chdir(path)
  for obj in os.listdir(os.curdir):
    if os.path.isfile(obj):    
      print(os.path.basename(obj))
    if os.path.isdir(obj):
      scandir(obj)
    

@click.command()
@click.option("--input", help="Input directory")
def media_archiver(input):
  print("media archiver start")
  scandir(input)
  

if __name__ == "__main__":
  media_archiver()