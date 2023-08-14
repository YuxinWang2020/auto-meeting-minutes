# auto-meeting-minutes

This project demonstrates automatically generating meeting minutes from audio recordings. It uses OpenAI's Whisper for speech recognition and GPT-3.5 for natural language processing.

## Overview

- Transcribe an audio recording of a meeting using Whisper
- Analyze the transcript to identify abstract summary, key points, action items and sentiment using GPT-3.5
- Generate formatted meeting minutes summarizing the key details

## Getting Started

### Prerequisites

- OpenAI API key
- Python 3.7+
- pip

### Installation
```
pip install -r requirements.txt
```

This will install the required packages including OpenAI, etc. 

### Usage  

1. Add your OpenAI API key to openai_api_key.txt
2. Transcribe an audio file and generate minutes:
    ```
    python meeting_minutes.py <input-audio.mp3>
    ```
This will output the generated meeting minutes to meeting_minutes.docx.

### Audio File Size Limitation

This project currently only supports audio files under 25MB due to a limitation of the Whisper API. Whisper can only transcribe files less than 25MB.

For longer audio files, consider splitting the recording into multiple parts under 25MB each before transcribing. 

See the [Whisper docs on longer inputs](https://platform.openai.com/docs/guides/speech-to-text/longer-inputs) for more details on workaround options for large files.

The summarization step does not have a size limitation, so you can concatenate the transcripts from multiple Whisper API calls before summarizing.


## Customization

The summarization model can be tuned by modifying the prompt in meeting_minutes.py. Feel free to experiment!

## License

This project is licensed under the MIT license - see LICENSE for more details.

## Credits  

Tutorial referenced:
https://platform.openai.com/docs/tutorials/meeting-minutes
