# بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ

السلام عليكم ورحمة الله وبركاته!

As-salāmu ʿalaykum, May Allah bless you long age with good health!

Welcome to the Al-Mathurat Audio Data! This is an open source data provided by [IMulism](https://imuslim.me) to give chance to you to submit or add audio for IMuslim's Al-Mathurat Audio!

---

This Datas Provided by IMuslim is Under MIT License.

---

This Project contains list of JSON files which save the information about the audio.

Though this project is about Audio Data, we don't upload any Audio File instead we use cdn. Thereforce Collaborator MUST NOT upload any audio file to the PR, if it does, we won't accept it.

---

Collaborator MUST speak in English, this help among collaborators to understand each other.

Collaborator MUST upload JSON File with valid syntax which will we discuss now.

---

### Audio JSON File Rules

There's rule for the content of JSON file to save the audio data.
The Rules MUST include

- `name` key, which is the name of audio, this will be showed up in the UI
- `prefix` key, this is the first audio src
- `contents` key, this is the audio src contents

---

### Audio JSON File Generator

we created a script to generate automatically the audio data—JSON File. The name of the file is `audio_data_generator.py`, and yes, it requires python version 3.

#### Arguments Needed

| Argument            | Description                       | Options / Syntax                                      |
| ------------------- | --------------------------------- | ----------------------------------------------------- |
| `--dzikir_type`     | Dzikir Type                       | `sugro` or `kubro`                                    |
| `--audio_prefix`    | Audio src for Prefix              | `https://<url>`                                       |
| `--audio_name`      | The Audio Name                    | -                                                     |
| `--audio_file_name` | The name of audio json file       | -                                                     |
| `--audio_src`       | The Audio—Content of Al-Mathsurat | `https://<url>/\{n}.mp3`, {n} is the index of content |
| `--dzikir_time`     | The Dzikir Time                   | `morning` or `evening`                                |

example :

```
python3 audio_data_generator.py --dzikir_type sugro --audio_prefix https://imuslim.s3-website.ir-thr-at1.arvanstorage.com/mp3almatsurat/prefix.mp3 --audio_name "Pak Luzum Sugro" --audio_file_name luzum_sugro_pagi --audio_src https://imuslim.s3-website.ir-thr-at1.arvanstorage.com/mp3almatsurat/\{n}.mp3 --dzikir_time morning
```
