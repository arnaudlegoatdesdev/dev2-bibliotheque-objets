from enum import StrEnum


class EtatObjet(StrEnum):
  BON_ETAT = "Bon_état"
  ENDOMMAGE = "Endommage"
  INCOMPLETE = "Incomplet"
  HORS_SERVICE = "Hors_service"