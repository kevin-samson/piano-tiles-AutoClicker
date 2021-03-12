# Piano tiles AutoClicker

Using the [online](https://www.agame.com/game/magic-piano-tiles) verion of piano tiles.

## Usage

1. Install reqired librares using `pip install -r requierments.txt`  (Recomended to use virtual enviroment)
2. Get coordinants of Black tiles and change the values in `piano.py`
3. Run `piano.py`

## Getting coordiantes

1. Install pyautogui (`pip install pyautogui`)
2. Open terminal or powershell
3. Type 
```python
>>>python
import pyautogui as py
py.displayMousePosition()
```
4. Hover over tiles and note the coordinate

## Exampe output

```python
Press Ctrl-C to quit.
X:  0 Y: 1143 RGB: ( 38,  38,  38)
```
