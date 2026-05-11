@echo off
set "OLLAMA_HOST=http://127.0.0.1:11434"
set "OLLAMA_MODELS=C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent\ollama-models"
if not exist "%OLLAMA_MODELS%" mkdir "%OLLAMA_MODELS%"
ollama serve

