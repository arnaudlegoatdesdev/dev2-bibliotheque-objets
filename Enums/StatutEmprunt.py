from enum import StrEnum


class StatutEmprunt(StrEnum):
  EN_COURS = "En_cours"
  RETOURNE = "Retourné"
  EN_RETARD = "En_retard"