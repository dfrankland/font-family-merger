<h1>Font Family Merger</h1>
<i>Merge font variations together to make a big, happy, font family!</i>
<p>Have you ever gotten a brand new, shiny, awesome font, but were taken agahst once it was loaded into your editing program? <i>Your precious new font was seperated by variations in a list of endless other fonts! This really sucks</i>, and there seems to be next to nothing out there for solutions to this (I am looking at you FontForge, GlyphsApp, etc.) &mdash; until now!</p>

<h2>Prerequisites</h2>
<ol>
    <li><strong>TTF is the only supported font!</strong></li>
    <li>
        <p>Font Family Merger assumes that each of your fonts has a font name like <i>"Font FontVariation"</i> which it will take and make the font family and rename your files. <i>If your fonts do not follow this pattern, changes to the code will be neccesary in order for it to work properly.</i></p>
    </li>
    <li>
        <p>Font Family Merger requires you to have <code>python</code> and also <code>BeautifulSoup</code> plus <code>fontTools</code> python modules installed as a prereqisite. For more information on that see below:</p>
        <ul>
            <li><a href="https://www.python.org/">Python</a></li>
            <li><a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a></li>
            <li><a href="https://github.com/behdad/fonttools">FontTools</a></li>
        </ul>
    </li>
</ol>
<h2>How to use this bad boy</h2>
<ol>
    <li><p>Backup the fonts that you want to merge. <i>If something goes wrong you might lose everything ;(</i></p></li>
    <li><p>Drop <code>font_family_merger.py</code> in the directory that contains <strong>only</strong> the font you want to merge</p></li>
    <li><p>In terminal <code>cd</code> to your directory containing your font files and <code>font_family_merger.py</code></p></li>
    <li><p>Run the command <code>python font_family_merger.py</code></p></li>
    <li><p><i>Watch the magic happen!</i></p></li>
</ol>
