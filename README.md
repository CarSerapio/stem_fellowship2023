# Implementing a Large Language Model (LLM) for Enhanced Tumour Phenotypic & Treatment Recommendations from Electronic Medical Records (EMRs)
Source code for the Indicium Conference 2023 research project: "Implementing Large Language Model (LLM) for Enhanced Tumour Phenotypic &amp; Treatment Recommendations from Electronic Medical Records (EMRs)​". We use `gpt-3.5-turbo` as our LLM and Flutter to build the front-end for the app. 

Uses `gpt-3.5-turbo` large language model to: 
* extract information from plaintext clinical records
* summarize information for cancers and tumours 
* output treatment plan for clinical decision support 

<img width="1064" alt="Screenshot 2023-05-08 at 3 48 18 PM" src="https://user-images.githubusercontent.com/105842563/236919496-6a3c7270-852d-4ea1-a027-f170768f04fb.png">

# Requirements

To have access to the front-end of this project, you should download [Flutter](https://docs.flutter.dev/get-started/install) and run: 

```
pip install -r requirements.txt
```

In addition, please set the `OPENAI_API_KEY` either in the environment variable or in `config.json`. If you do not have an OpenAI account with API key, please visit [OpenAI website](https://openai.com/blog/openai-api)

macOS(Bash):

```
export OPENAI_API_KEY=<your_api_key>
```

Windows(Command Prompt):
```
set OPENAI_API_KEY=<your_api_key>
```

# Usage

To start the app in Flutter and test different models, please run:

```
python model.py
```

or:

```
python model2.py
```


# Team

This project was developed by the following individuals:

- [Caroline Serapio](https://github.com/CarSerapio)
- Mithusan Sivarajah
- Qasim Tahir
- Simran Dhawan

Special thanks to [Yunfei Ma](https://github.com/Yunfei-Ma-McMaster) to be the mentor for STEM Fellowship research project.

## Contact

If you have any questions or feedback regarding this research, feel free to reach out to any of the authors or contributors mentioned above. We are actively looking for feedback from industry experts!

We appreciate your interest and support!
