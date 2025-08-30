# Transam
Transam is an agentic AI for generating CDISC Biomedical Concept.

## Notification
This Agentic AI application was developed for the CDISC AI Innovation Challenge, but it lacks sufficient testing and should not be used for
production purposes.

## Platform
I developed Transam on Mac M4 platform.
- Python >= v3.12

## Instration and Run
- Install LM Studio and load the model.
- Install Python >= v3.12 and UV.
- Clone or download this repository.
- Configure Python venv for Transam.
- Create working directory.
- Create output and rag_docs sub-directories under the working directory
- deploy markdown docs into rag_docs sub-directory.
```
uv run python transam_agent.py --work_dir /path/to/working/dir
```

## License
MIT License
