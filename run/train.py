from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

training_data = load_data("../data/examples/rasa/demo-rasa.json")
trainer = Trainer(RasaNLUConfig("config_spacy.json"))
trainer.train(training_data)
model_directory = trainer.persist('./models/')
