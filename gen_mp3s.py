import time
import sys

from gtts import gTTS


def show(s):
    print(f"{s}", end="")
    sys.stdout.flush()


if __name__ == "__main__":
    language = "en"
    for i in range(11):
        mins = (i + 1) * 5
        text = f"It has been {mins} minutes"
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save(f"{mins}mins.mp3")
        show(".")
        time.sleep(1)

    text = "It has been 1 hour"
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("60mins.mp3")
    time.sleep(1)
