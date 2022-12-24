<head>

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

</head>

<body>
    
    <h1>NUBZBOT</h1>
    <p>The second version. The first version is not on GitHub.</p>

    <p>This code was made in Windows, so  if you want to use it, you'll have to edit the part of the code that changes the CWD to match your OS's file system.</p>

    <h3>Installing requirements</h3>
    <!-- <p>I reccomend installing the requirements on a virtualenv. So set one up. Then just run <code>pip install -r requirements.txt</code>. Note that if you are on Linux, you would also need to install <code>uvloop</code> to just speed up <code>asyncio</code> processes.</p> -->
    <ol>
        <li>I recommend installing a virtual environment into the directory. So set one up</li>
        <li>Install the libraries onto the virtual environment by using the command: <code>pip install -r requirements.txt</code>. Note that if you are not on Windows, you should also install <code>uvloop</code></li>
    </ol>

    <h3>Fixing file paths</h3>
    <h4>Since Windows has different file path systems, you'll have to change the code to make it work on other operating systems. Here is a table that guides you through what to change.</h4>
    <table>

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

</body>
