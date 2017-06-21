from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter
from train import model_directory

metadata = Metadata.load(model_directory)
interpret = Interpreter.load(metadata, RasaNLUConfig("config_spacy.json"))
