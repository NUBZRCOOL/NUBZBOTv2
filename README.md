# NUBZBOT

This is the second version. The first version is not on GitHub.
<!-- 
This code was made in Windows, so if you want to use it on a different OS, you'll have to edit the part of the code that changes the CWD to match your OS's file system. -->

<br>

### **Installing requirements**

1. I recommend installing a virtual environment into the directory. So set one up.
1. Install the libraries onto the virtual environment by using the command: ```pip install -r requirements.txt```. Note that if you are not on Windows, you should also install ```uvloop```.

<!-- <br>

### **Fixing file paths**

<table style="border: 1px solid black; margin: 10px;">
<tr>
<th style="border: 1px solid black; margin: 10px;">File & Line #</th>
<th style="border: 1px solid black; margin: 10px;">Windows</th>
<th style="border: 1px solid black; margin: 10px;">Linux/Mac</th>
</tr>
<tr>
<td>NUBZBOTv2/Bot.py: 8</td>
<td style="border: 1px solid black; margin: 10px;" rowspan="4"><code>os.chdir(os.path.dirname(__file__) + "\\")</code></td>
<td style="border: 1px solid black; margin: 10px;" rowspan="4"><code>os.chdir(os.path.dirname(__file__) + "/")</code></td>
</tr>
<tr>
<td style="border: 1px solid black; margin: 10px;">NUBZBOTv2/extensions/misc.py: 6</td>
</tr>
<tr>
<td style="border: 1px solid black; margin: 10px;">NUBZBOTv2/extensions/help.py: 7</td>
</tr>
<tr>
<td style="border: 1px solid black; margin: 10px;">NUBZBOTv2/extensions/moderation.py: 7</td>
</tr>
</table>

<br> -->

### **Running the bot**

<!-- 1. If you are not on Windows, the '```.env```' file probably did not show up. This is why you need to create it. Name the new file '```env```' (no file extension) and put in it: ```TOKEN = place bot token here``` -->
1. Run ```python ./NUBZBOTv2/__main__.py```