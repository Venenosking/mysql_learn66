html_content = """
<!DOCTYPE html>
<html>
<head>
	<title>播放MP3文件</title>
</head>
<body>
	<audio id="myAudio" controls>
		<source src="测试.mp3" type="audio/mpeg">
		Your browser does not support the audio element.
	</audio>

	<button onclick="playAudio()">播放</button>
	<button onclick="pauseAudio()">暂停</button>

	<script>
		var audio = document.getElementById("myAudio");

		function playAudio() {
			audio.play();
		}

		function pauseAudio() {
			audio.pause();
		}
	</script>
</body>
</html>
"""

# 将HTML内容写入文件
with open("index.html", "w") as f:
    f.write(html_content)

# 将MP3文件复制到HTML文件所在的目录
import shutil
# shutil.copyfile("测试.mp3", "index_files/测试.mp3")
