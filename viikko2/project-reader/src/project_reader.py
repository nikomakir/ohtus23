from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_content["tool"]["poetry"]["name"],
                       parsed_content["tool"]["poetry"]["license"],
                       parsed_content["tool"]["poetry"]["authors"],
                       parsed_content["tool"]["poetry"]["description"],
                       list(parsed_content["tool"]["poetry"]["dependencies"].keys()),
                       list(parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()))
