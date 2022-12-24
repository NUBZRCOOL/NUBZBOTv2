<style>

    table, th, td {

        border: 1px solid black;
        margin: 10px;
        border-collapse: collapse;
    }
    th, td {

        padding: 10px;
    }

</style>

# NUBZBOT

The second version. The first version is not on GitHub.

This code was made in Windows, so  if you want to use it, you'll have to edit the part of the code that changes the CWD to match your OS's file system.

<br>

### **Installing requirements**

1. I recommend installing a virtual environment into the directory. So set one up.
1. Install the libraries onto the virtual environment by using the command: ```pip install -r requirements.txt```. Note that if you are not on Windows, you should also install ```uvloop```.

<br>

### **Fixing file paths**

<table >
<tr>
<th>File & Line #</th>
<th>Windows</th>
<th>Linux/Mac</th>
</tr>
<tr>
<td>Bot.py: 8</td>
<td rowspan="4"><code>os.chdir(os.path.dirname(__file__) + "\\")</code></td>
<td rowspan="4"><code>os.chdir(os.path.dirname(__file__) + "/")</code></td>
</tr>
<tr>
<td>NUBZBOTv2/extensions/misc.py: 6</td>
</tr>
<tr>
<td>NUBZBOTv2/extensions/help.py: 7</td>
</tr>
<tr>
<td>NUBZBOTv2/extensions/moderation.py: 7</td>
</tr>
</table>