import pyautogui
import time

a,b,c,d,e,f,g,h,j,k = 0,0,0,0,0,0,0,0,0,0

y = pyautogui.confirm(text='Do you want to run python code to find all the location of button on screen', title='Run Python to find locations', buttons=['OK', 'Cancel'])
if(y=='OK'):
  for x in range(0,300):
    print(x)
    try:
      if(a):
        pyautogui.click(a,b)
      else:
        a,b = pyautogui.locateCenterOnScreen('runtime.png')
        pyautogui.click(a,b)
      time.sleep(2)
      if(c):
        pyautogui.click(c,d)
      else:
        c,d = pyautogui.locateCenterOnScreen('factoryresettime.png')
        pyautogui.click(c,d)
      time.sleep(2)
      pyautogui.press('enter')
      time.sleep(2)
      if(g):
        pyautogui.click(g,h)
      else:
        g,h = pyautogui.locateCenterOnScreen('reconnect.png')
        pyautogui.click(g,h)
      for i in range(0,30):
        try:
          pyautogui.locateCenterOnScreen('connected.png')
          break
        except:
          time.sleep(1)
          continue
      pyautogui.click(pyautogui.locateCenterOnScreen('uploadbutton.png'))  
      time.sleep(1)
      pyautogui.write('.env')
      pyautogui.press('enter')
      time.sleep(6)
      if(j):
        pyautogui.click(j,k)
      else:
        j,k = pyautogui.locateCenterOnScreen('run.png')
        pyautogui.click(j,k)
      time.sleep(350)
    except:
      pyautogui.alert('can\'t find Runtime button')
