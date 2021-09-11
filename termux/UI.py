'''Termux-API Dialog and Toast methods

    confirm - Show confirmation dialog
    checkbox - Select multiple values using checkboxes
    counter - Pick a number in specified range
    date - Pick a date
    time - Pick a time value
    radio - Pick a single value from radio buttons
    sheet - Pick a value from sliding bottom sheet
    spinner - Pick a single value from a dropdown spinner
    speech - Obtain speech using device microphone
    text - Input text
    toast - Show text as toast (transient popup) 
'''
from .android import execute

def __radiolike(func,opts,title):
  v = "-v "
  for f in opts:
    v += f'"{f}",'
  v = v[0:-1]
  if title is not None:
    v += f' -t "{title}"'
  return execute(f"termux-dialog {func} {v}")

def __hintlike(func,hint,title):
  opts = ""
  if hint is not None:
    opts += f'-i "{hint}" '
  if title is not None:
    opts += f'-t "{title}"'
  return execute(f"termux-dialog {func} {opts}")
   


def confirm(hint: str = None, title: str = None):
  '''Show confirmation dialog

    hint - text hint (optional)
    title - set title of dialog (optional)
  '''
  return __hintlike("confirm",hint,title)

def speech(hint :str = None, title :str = None):
  '''Obtain speech using device microphone

    hint - text hint (optional)
    title - set title of dialog (optional)
  '''
  return __hintlike("speech",hint,title)


def counter(rangeTuple :tuple = None, title :str = None):
  '''Pick a number in specified range

    rangeTuple - tuple of 3 numbers (min, max, start) (optional)
    title - set title of dialog (optional)
  '''
  r = "-r "
  for f in rangeTuple:
    r += f'{f},'
  r = r[0:-1]
  if title is not None:
    r += f' -t "{title}"'
  return execute(f"termux-dialog counter {r}")

def date(format :str = None, title :str = None):
  '''Pick a date

    format - SimpleDateFormat (optional) eg "dd-MM-yyyy"
    title - set title of dialog (optional)
  '''
  opts = ""
  if format is not None:
    opts += f'-d "{format}" '
  if title is not None:
    opts += f'-t "{title}"'
  return execute(f"termux-dialog date {opts}")

def time(title: str = None):
  '''Pick a time value
  
    title - set title of dialog (optional)
  '''
  return __hintlike("time",hint = None,title = title)


def checkbox(opts: tuple, title :str = None):
  '''Select multiple values using checkboxes

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('checkbox',opts,title)

def radio(opts: tuple, title :str = None):
  '''Pick a single value from radio buttons

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('radio',opts,title)

def sheet(opts: tuple, title :str = None):
  '''Pick a value from sliding bottom sheet

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('sheet',opts,title)

def spinner(opts: tuple, title :str = None):
  '''Pick a single value from a dropdown spinner

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('spinner',opts,title)

def text(hint :str = None, multiline: bool = None, number: bool = None, password: bool = None, title :str = None):
  '''Text input

    hint - text hint (optional)
    multiline - multiline input (optional)*
    number - number input (optional)*
    password - password input (optional)
    title - set title of dialog (optional)

    * cannot use together 
  '''
  if (multiline is not None) and (number is not None):
    return "Cannot use multiline and number together" 
  opts = ""
  if multiline is not None: 
    opts += "-m "
  if number is not None:
    opts += "-n "
  if password is not None:
    opts += "-p "
  if hint is not None:
    opts += f'-i "{hint}" '
  if title is not None:
    opts += f'-t "{title}"'
  return execute(f"termux-dialog text {opts}")

def toast(text: str, bgcolor :str = None, color: str = None, position: str = None, short: bool = False):
  '''Show a toast message

    text = Text to show toast
    bgcolor = background color (default: gray)
    color = text color (default: white)
    position = [top, middle, or bottom] (default: middle)
    short = only show the toast for a short while (default: false)
  '''
  opts = {
    "bgcolor": "-b",
    "color": "-c",
    "position": "-g"
  }

  options = ""
  for f in opts.keys():
      if eval(f) is not None:
          options += f"{opts[f]} {eval(f)} "

  if short is not None:
      options += "-s"

  r = execute(f'termux-toast {options} "{text}"')
  return r[1]
