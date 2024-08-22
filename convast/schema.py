# Auto generated from NCBI_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-22T12:09:58
# Schema: NCBI_antibiogram
#
# id: https://example.com/NCBI_antibiogram
# description: Schema for validation of NCBI antibiogram data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = "1.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ARO = CurieNamespace('ARO', 'http://purl.obolibrary.org/obo/ARO_')
BAO = CurieNamespace('BAO', 'hhtp://purl.obolibrary.org/obo/BAO_')
GENEPIO = CurieNamespace('GENEPIO', 'http://purl.obolibrary.org/obo/GENEPIO_')
NCIT = CurieNamespace('NCIT', 'hhtp://purl.obolibrary.org/obo/NCIT_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://example.com/NCBI_antibiogram/')


# Types

# Class references



@dataclass(repr=False)
class NCBIAntibiogram(YAMLRoot):
    """
    Class representing an antibiogram
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/NCBI_antibiogram/NCBIAntibiogram")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NCBI_antibiogram"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/NCBI_antibiogram/NCBIAntibiogram")

    biosample_accession: Optional[str] = None
    organism: Optional[str] = None
    antibiotic: Optional[Union[str, "AntibioticMenu"]] = None
    resistance_phenotype: Optional[Union[str, "ResistancePhenotypeMenu"]] = None
    measurement: Optional[float] = None
    measurement_units: Optional[Union[str, "MeasurementUnitsMenu"]] = None
    measurement_sign: Optional[Union[str, "MeasurementSignMenu"]] = None
    laboratory_typing_method: Optional[Union[str, "LaboratoryTypingMethodMenu"]] = None
    laboratory_typing_platform: Optional[Union[str, "LaboratoryTypingPlatformMenu"]] = None
    vendor: Optional[Union[str, "VendorMenu"]] = None
    laboratory_typing_method_version_or_reagent: Optional[Union[str, "LaboratoryTypingMethodVersionOrReagentMenu"]] = None
    testing_standard: Optional[Union[str, "TestingStandardMenu"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.biosample_accession is not None and not isinstance(self.biosample_accession, str):
            self.biosample_accession = str(self.biosample_accession)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.antibiotic is not None and not isinstance(self.antibiotic, AntibioticMenu):
            self.antibiotic = AntibioticMenu(self.antibiotic)

        if self.resistance_phenotype is not None and not isinstance(self.resistance_phenotype, ResistancePhenotypeMenu):
            self.resistance_phenotype = ResistancePhenotypeMenu(self.resistance_phenotype)

        if self.measurement is not None and not isinstance(self.measurement, float):
            self.measurement = float(self.measurement)

        if self.measurement_units is not None and not isinstance(self.measurement_units, MeasurementUnitsMenu):
            self.measurement_units = MeasurementUnitsMenu(self.measurement_units)

        if self.measurement_sign is not None and not isinstance(self.measurement_sign, MeasurementSignMenu):
            self.measurement_sign = MeasurementSignMenu(self.measurement_sign)

        if self.laboratory_typing_method is not None and not isinstance(self.laboratory_typing_method, LaboratoryTypingMethodMenu):
            self.laboratory_typing_method = LaboratoryTypingMethodMenu(self.laboratory_typing_method)

        if self.laboratory_typing_platform is not None and not isinstance(self.laboratory_typing_platform, LaboratoryTypingPlatformMenu):
            self.laboratory_typing_platform = LaboratoryTypingPlatformMenu(self.laboratory_typing_platform)

        if self.vendor is not None and not isinstance(self.vendor, VendorMenu):
            self.vendor = VendorMenu(self.vendor)

        if self.laboratory_typing_method_version_or_reagent is not None and not isinstance(self.laboratory_typing_method_version_or_reagent, LaboratoryTypingMethodVersionOrReagentMenu):
            self.laboratory_typing_method_version_or_reagent = LaboratoryTypingMethodVersionOrReagentMenu(self.laboratory_typing_method_version_or_reagent)

        if self.testing_standard is not None and not isinstance(self.testing_standard, TestingStandardMenu):
            self.testing_standard = TestingStandardMenu(self.testing_standard)

        super().__post_init__(**kwargs)


# Enumerations
class AntibioticMenu(EnumDefinitionImpl):

    acriflavin = PermissibleValue(text="acriflavin")
    actinomycin = PermissibleValue(text="actinomycin")
    amikacin = PermissibleValue(text="amikacin")
    amoxicillin = PermissibleValue(text="amoxicillin")
    ampicillin = PermissibleValue(text="ampicillin")
    anidulafungin = PermissibleValue(text="anidulafungin")
    apramycin = PermissibleValue(text="apramycin")
    arbekacin = PermissibleValue(text="arbekacin")
    arsphenamine = PermissibleValue(text="arsphenamine")
    arylomycin = PermissibleValue(text="arylomycin")
    astromicin = PermissibleValue(text="astromicin")
    aurodox = PermissibleValue(text="aurodox")
    avoparcin = PermissibleValue(text="avoparcin")
    azamulin = PermissibleValue(text="azamulin")
    azdimycin = PermissibleValue(text="azdimycin")
    azidamfenicol = PermissibleValue(text="azidamfenicol")
    azithromycin = PermissibleValue(text="azithromycin")
    azlocillin = PermissibleValue(text="azlocillin")
    aztreonam = PermissibleValue(text="aztreonam")
    bacitracin = PermissibleValue(text="bacitracin")
    balhimycin = PermissibleValue(text="balhimycin")
    benzylpenicillin = PermissibleValue(text="benzylpenicillin")
    bicyclomycin = PermissibleValue(text="bicyclomycin")
    bleomycin = PermissibleValue(text="bleomycin")
    brodimoprim = PermissibleValue(text="brodimoprim")
    butirosin = PermissibleValue(text="butirosin")
    capreomycin = PermissibleValue(text="capreomycin")
    carbenicillin = PermissibleValue(text="carbenicillin")
    carbomycin = PermissibleValue(text="carbomycin")
    caspofungin = PermissibleValue(text="caspofungin")
    cefaclor = PermissibleValue(text="cefaclor")
    cefadroxil = PermissibleValue(text="cefadroxil")
    cefalexin = PermissibleValue(text="cefalexin")
    cefalotin = PermissibleValue(text="cefalotin")
    cefamandole = PermissibleValue(text="cefamandole")
    cefazolin = PermissibleValue(text="cefazolin")
    cefdinir = PermissibleValue(text="cefdinir")
    cefditoren = PermissibleValue(text="cefditoren")
    cefepime = PermissibleValue(text="cefepime")
    cefetamet = PermissibleValue(text="cefetamet")
    cefideroco = PermissibleValue(text="cefideroco")
    cefixime = PermissibleValue(text="cefixime")
    cefmetazole = PermissibleValue(text="cefmetazole")
    cefonicid = PermissibleValue(text="cefonicid")
    cefoperazone = PermissibleValue(text="cefoperazone")
    cefotaxime = PermissibleValue(text="cefotaxime")
    cefotetan = PermissibleValue(text="cefotetan")
    cefotiam = PermissibleValue(text="cefotiam")
    cefoxitin = PermissibleValue(text="cefoxitin")
    cefpodoxime = PermissibleValue(text="cefpodoxime")
    cefprozil = PermissibleValue(text="cefprozil")
    ceftaroline = PermissibleValue(text="ceftaroline")
    ceftazidime = PermissibleValue(text="ceftazidime")
    ceftibuten = PermissibleValue(text="ceftibuten")
    ceftiofur = PermissibleValue(text="ceftiofur")
    ceftizoxime = PermissibleValue(text="ceftizoxime")
    ceftobiprole = PermissibleValue(text="ceftobiprole")
    ceftriaxone = PermissibleValue(text="ceftriaxone")
    cefuroxime = PermissibleValue(text="cefuroxime")
    celesticetin = PermissibleValue(text="celesticetin")
    cephalexin = PermissibleValue(text="cephalexin")
    cephalothin = PermissibleValue(text="cephalothin")
    cephamycin = PermissibleValue(text="cephamycin")
    cephapirin = PermissibleValue(text="cephapirin")
    cephem = PermissibleValue(text="cephem")
    cephradine = PermissibleValue(text="cephradine")
    chalcomycin = PermissibleValue(text="chalcomycin")
    chloramphenicol = PermissibleValue(text="chloramphenicol")
    chloroeremomycin = PermissibleValue(text="chloroeremomycin")
    chlortetracycline = PermissibleValue(text="chlortetracycline")
    cinoxacin = PermissibleValue(text="cinoxacin")
    ciprofloxacin = PermissibleValue(text="ciprofloxacin")
    clarithromycin = PermissibleValue(text="clarithromycin")
    clinafloxacin = PermissibleValue(text="clinafloxacin")
    clindamycin = PermissibleValue(text="clindamycin")
    clofazimine = PermissibleValue(text="clofazimine")
    clorobiocin = PermissibleValue(text="clorobiocin")
    cloxacillin = PermissibleValue(text="cloxacillin")
    colistin = PermissibleValue(text="colistin")
    cycloserine = PermissibleValue(text="cycloserine")
    dalbavancin = PermissibleValue(text="dalbavancin")
    dalfopristin = PermissibleValue(text="dalfopristin")
    danofloxacin = PermissibleValue(text="danofloxacin")
    daptomycin = PermissibleValue(text="daptomycin")
    defensin = PermissibleValue(text="defensin")
    delafloxacin = PermissibleValue(text="delafloxacin")
    demeclocycline = PermissibleValue(text="demeclocycline")
    diaminopyrimidine = PermissibleValue(text="diaminopyrimidine")
    dibekacin = PermissibleValue(text="dibekacin")
    dicloxacillin = PermissibleValue(text="dicloxacillin")
    dihydromocimycin = PermissibleValue(text="dihydromocimycin")
    dirithromycin = PermissibleValue(text="dirithromycin")
    doripenem = PermissibleValue(text="doripenem")
    doxycycline = PermissibleValue(text="doxycycline")
    edeine = PermissibleValue(text="edeine")
    efrotomycin = PermissibleValue(text="efrotomycin")
    elfamycin = PermissibleValue(text="elfamycin")
    enoxacin = PermissibleValue(text="enoxacin")
    enrofloxacin = PermissibleValue(text="enrofloxacin")
    eravacycline = PermissibleValue(text="eravacycline")
    ertapenem = PermissibleValue(text="ertapenem")
    erythromycin = PermissibleValue(text="erythromycin")
    ethambutol = PermissibleValue(text="ethambutol")
    ethionamide = PermissibleValue(text="ethionamide")
    factumycin = PermissibleValue(text="factumycin")
    fidaxomicin = PermissibleValue(text="fidaxomicin")
    fleroxacin = PermissibleValue(text="fleroxacin")
    flomoxef = PermissibleValue(text="flomoxef")
    florfenicol = PermissibleValue(text="florfenicol")
    flucloxacillin = PermissibleValue(text="flucloxacillin")
    fluconazole = PermissibleValue(text="fluconazole")
    flucytosine = PermissibleValue(text="flucytosine")
    fluoroquinolone = PermissibleValue(text="fluoroquinolone")
    fosfomycin = PermissibleValue(text="fosfomycin")
    fosmidomycin = PermissibleValue(text="fosmidomycin")
    furazolidone = PermissibleValue(text="furazolidone")
    G418 = PermissibleValue(text="G418")
    ganefromycin = PermissibleValue(text="ganefromycin")
    gatifloxacin = PermissibleValue(text="gatifloxacin")
    GE2270A = PermissibleValue(text="GE2270A")
    GE37468 = PermissibleValue(text="GE37468")
    gentamicin = PermissibleValue(text="gentamicin")
    glycylcycline = PermissibleValue(text="glycylcycline")
    gramicidin = PermissibleValue(text="gramicidin")
    grepafloxacin = PermissibleValue(text="grepafloxacin")
    griseoviridin = PermissibleValue(text="griseoviridin")
    heneicomycin = PermissibleValue(text="heneicomycin")
    iclaprim = PermissibleValue(text="iclaprim")
    imipenem = PermissibleValue(text="imipenem")
    isavuconazole = PermissibleValue(text="isavuconazole")
    isepamicin = PermissibleValue(text="isepamicin")
    isoniazid = PermissibleValue(text="isoniazid")
    itraconazole = PermissibleValue(text="itraconazole")
    josamycin = PermissibleValue(text="josamycin")
    kanamycin = PermissibleValue(text="kanamycin")
    kasugamicin = PermissibleValue(text="kasugamicin")
    kirromycin = PermissibleValue(text="kirromycin")
    kirrothricin = PermissibleValue(text="kirrothricin")
    kitasamycin = PermissibleValue(text="kitasamycin")
    levofloxacin = PermissibleValue(text="levofloxacin")
    lincomycin = PermissibleValue(text="lincomycin")
    lincosamide = PermissibleValue(text="lincosamide")
    linezolid = PermissibleValue(text="linezolid")
    lividomycin = PermissibleValue(text="lividomycin")
    lomefloxacin = PermissibleValue(text="lomefloxacin")
    loracarbef = PermissibleValue(text="loracarbef")
    mafenide = PermissibleValue(text="mafenide")
    magainin = PermissibleValue(text="magainin")
    mecillinam = PermissibleValue(text="mecillinam")
    megalomycin = PermissibleValue(text="megalomycin")
    meropenem = PermissibleValue(text="meropenem")
    methicillin = PermissibleValue(text="methicillin")
    methymycin = PermissibleValue(text="methymycin")
    metronidazole = PermissibleValue(text="metronidazole")
    mezlocillin = PermissibleValue(text="mezlocillin")
    micafungin = PermissibleValue(text="micafungin")
    midecamycin = PermissibleValue(text="midecamycin")
    minocycline = PermissibleValue(text="minocycline")
    moenomycin = PermissibleValue(text="moenomycin")
    moxalactam = PermissibleValue(text="moxalactam")
    moxifloxacin = PermissibleValue(text="moxifloxacin")
    mupirocin = PermissibleValue(text="mupirocin")
    mycinamicin = PermissibleValue(text="mycinamicin")
    nafcillin = PermissibleValue(text="nafcillin")
    narbomycin = PermissibleValue(text="narbomycin")
    neomycin = PermissibleValue(text="neomycin")
    netilmicin = PermissibleValue(text="netilmicin")
    nicotinamide = PermissibleValue(text="nicotinamide")
    niddamycin = PermissibleValue(text="niddamycin")
    nitrofurantoin = PermissibleValue(text="nitrofurantoin")
    norfloxacin = PermissibleValue(text="norfloxacin")
    novobiocin = PermissibleValue(text="novobiocin")
    ofloxacin = PermissibleValue(text="ofloxacin")
    oleandomycin = PermissibleValue(text="oleandomycin")
    omadacycline = PermissibleValue(text="omadacycline")
    oritavancin = PermissibleValue(text="oritavancin")
    oxacillin = PermissibleValue(text="oxacillin")
    oxytetracycline = PermissibleValue(text="oxytetracycline")
    paromomycin = PermissibleValue(text="paromomycin")
    pefloxacin = PermissibleValue(text="pefloxacin")
    penam = PermissibleValue(text="penam")
    penicillin = PermissibleValue(text="penicillin")
    phenicol = PermissibleValue(text="phenicol")
    phenoxymethylpenicillin = PermissibleValue(text="phenoxymethylpenicillin")
    pikromycin = PermissibleValue(text="pikromycin")
    piperacillin = PermissibleValue(text="piperacillin")
    plazomicin = PermissibleValue(text="plazomicin")
    pleuromutilin = PermissibleValue(text="pleuromutilin")
    polymyxin = PermissibleValue(text="polymyxin")
    posaconazole = PermissibleValue(text="posaconazole")
    propicillin = PermissibleValue(text="propicillin")
    prothionamide = PermissibleValue(text="prothionamide")
    pulvomycin = PermissibleValue(text="pulvomycin")
    puromycin = PermissibleValue(text="puromycin")
    pyrazinamide = PermissibleValue(text="pyrazinamide")
    quinupristin = PermissibleValue(text="quinupristin")
    retapamulin = PermissibleValue(text="retapamulin")
    ribostamycin = PermissibleValue(text="ribostamycin")
    rifabutin = PermissibleValue(text="rifabutin")
    rifampin = PermissibleValue(text="rifampin")
    rifamycin = PermissibleValue(text="rifamycin")
    rifapentine = PermissibleValue(text="rifapentine")
    rifaximin = PermissibleValue(text="rifaximin")
    ristocetin = PermissibleValue(text="ristocetin")
    rosaramicin = PermissibleValue(text="rosaramicin")
    roxithromycin = PermissibleValue(text="roxithromycin")
    SB22484 = PermissibleValue(text="SB22484")
    sisomicin = PermissibleValue(text="sisomicin")
    sparfloxacin = PermissibleValue(text="sparfloxacin")
    spectinomycin = PermissibleValue(text="spectinomycin")
    spiramycin = PermissibleValue(text="spiramycin")
    streptogramin = PermissibleValue(text="streptogramin")
    streptomycin = PermissibleValue(text="streptomycin")
    streptothricin = PermissibleValue(text="streptothricin")
    sulbactam = PermissibleValue(text="sulbactam")
    sulfacetamide = PermissibleValue(text="sulfacetamide")
    sulfadiazine = PermissibleValue(text="sulfadiazine")
    sulfadimethoxine = PermissibleValue(text="sulfadimethoxine")
    sulfadimidine = PermissibleValue(text="sulfadimidine")
    sulfadoxine = PermissibleValue(text="sulfadoxine")
    sulfamethizole = PermissibleValue(text="sulfamethizole")
    sulfamethoxazole = PermissibleValue(text="sulfamethoxazole")
    sulfasalazine = PermissibleValue(text="sulfasalazine")
    sulfisoxazole = PermissibleValue(text="sulfisoxazole")
    sulfonamide = PermissibleValue(text="sulfonamide")
    surotomycin = PermissibleValue(text="surotomycin")
    synercid = PermissibleValue(text="synercid")
    tazobactam = PermissibleValue(text="tazobactam")
    tedizolid = PermissibleValue(text="tedizolid")
    teicoplanin = PermissibleValue(text="teicoplanin")
    telavancin = PermissibleValue(text="telavancin")
    telithromycin = PermissibleValue(text="telithromycin")
    temocillin = PermissibleValue(text="temocillin")
    tetracycline = PermissibleValue(text="tetracycline")
    tetroxoprim = PermissibleValue(text="tetroxoprim")
    thiamphenicol = PermissibleValue(text="thiamphenicol")
    thiostrepton = PermissibleValue(text="thiostrepton")
    tiamulin = PermissibleValue(text="tiamulin")
    ticarcillin = PermissibleValue(text="ticarcillin")
    tigecycline = PermissibleValue(text="tigecycline")
    tilmicosin = PermissibleValue(text="tilmicosin")
    timentin = PermissibleValue(text="timentin")
    tinidazole = PermissibleValue(text="tinidazole")
    tobramycin = PermissibleValue(text="tobramycin")
    triclosan = PermissibleValue(text="triclosan")
    trimethoprim = PermissibleValue(text="trimethoprim")
    trovafloxacin = PermissibleValue(text="trovafloxacin")
    tuberactinomycin = PermissibleValue(text="tuberactinomycin")
    tulathromycin = PermissibleValue(text="tulathromycin")
    tunicamycin = PermissibleValue(text="tunicamycin")
    tylosin = PermissibleValue(text="tylosin")
    tyrothricin = PermissibleValue(text="tyrothricin")
    unphenelfamycin = PermissibleValue(text="unphenelfamycin")
    valnemulin = PermissibleValue(text="valnemulin")
    vancomycin = PermissibleValue(text="vancomycin")
    verdamicin = PermissibleValue(text="verdamicin")
    vertilimicin = PermissibleValue(text="vertilimicin")
    viomycin = PermissibleValue(text="viomycin")
    voriconazole = PermissibleValue(text="voriconazole")

    _defn = EnumDefinition(
        name="AntibioticMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "acridine dye",
            PermissibleValue(text="acridine dye"))
        setattr(cls, "actinomycin D",
            PermissibleValue(text="actinomycin D"))
        setattr(cls, "amoxicillin-clavulanic acid",
            PermissibleValue(text="amoxicillin-clavulanic acid"))
        setattr(cls, "amphotericin B",
            PermissibleValue(text="amphotericin B"))
        setattr(cls, "ampicillin-sulbactam",
            PermissibleValue(text="ampicillin-sulbactam"))
        setattr(cls, "amythiamicin A",
            PermissibleValue(text="amythiamicin A"))
        setattr(cls, "antibiotic A40926",
            PermissibleValue(text="antibiotic A40926"))
        setattr(cls, "antibiotic A47934",
            PermissibleValue(text="antibiotic A47934"))
        setattr(cls, "bacitracin A",
            PermissibleValue(text="bacitracin A"))
        setattr(cls, "bacitracin B",
            PermissibleValue(text="bacitracin B"))
        setattr(cls, "bacitracin F",
            PermissibleValue(text="bacitracin F"))
        setattr(cls, "bleomycin A2",
            PermissibleValue(text="bleomycin A2"))
        setattr(cls, "bleomycin B2",
            PermissibleValue(text="bleomycin B2"))
        setattr(cls, "bleomycinic acid",
            PermissibleValue(text="bleomycinic acid"))
        setattr(cls, "cefotaxime-clavulanic acid",
            PermissibleValue(text="cefotaxime-clavulanic acid"))
        setattr(cls, "cefpodoxime-proxetil",
            PermissibleValue(text="cefpodoxime-proxetil"))
        setattr(cls, "ceftazidime-avibactam",
            PermissibleValue(text="ceftazidime-avibactam"))
        setattr(cls, "ceftazidime-clavulanic acid",
            PermissibleValue(text="ceftazidime-clavulanic acid"))
        setattr(cls, "ceftolozane-tazobactam",
            PermissibleValue(text="ceftolozane-tazobactam"))
        setattr(cls, "clavulanic acid",
            PermissibleValue(text="clavulanic acid"))
        setattr(cls, "colistin A",
            PermissibleValue(text="colistin A"))
        setattr(cls, "colistin B",
            PermissibleValue(text="colistin B"))
        setattr(cls, "coumermycin A1",
            PermissibleValue(text="coumermycin A1"))
        setattr(cls, "cyclic thiazolyl peptide elfamycin",
            PermissibleValue(text="cyclic thiazolyl peptide elfamycin"))
        setattr(cls, "edeine A",
            PermissibleValue(text="edeine A"))
        setattr(cls, "edeine B",
            PermissibleValue(text="edeine B"))
        setattr(cls, "edeine D",
            PermissibleValue(text="edeine D"))
        setattr(cls, "edeine F",
            PermissibleValue(text="edeine F"))
        setattr(cls, "enacyloxin IIa",
            PermissibleValue(text="enacyloxin IIa"))
        setattr(cls, "fosfomycin-glucose-6-phosphate",
            PermissibleValue(text="fosfomycin-glucose-6-phosphate"))
        setattr(cls, "fusidic acid",
            PermissibleValue(text="fusidic acid"))
        setattr(cls, "gentamicin B",
            PermissibleValue(text="gentamicin B"))
        setattr(cls, "gentamicin C",
            PermissibleValue(text="gentamicin C"))
        setattr(cls, "gramicidin A",
            PermissibleValue(text="gramicidin A"))
        setattr(cls, "gramicidin B",
            PermissibleValue(text="gramicidin B"))
        setattr(cls, "gramicidin C",
            PermissibleValue(text="gramicidin C"))
        setattr(cls, "gramicidin D",
            PermissibleValue(text="gramicidin D"))
        setattr(cls, "gramicidin S",
            PermissibleValue(text="gramicidin S"))
        setattr(cls, "hygromycin B",
            PermissibleValue(text="hygromycin B"))
        setattr(cls, "Imipenem-EDTA-PA",
            PermissibleValue(text="Imipenem-EDTA-PA"))
        setattr(cls, "imipenem-relebactam",
            PermissibleValue(text="imipenem-relebactam"))
        setattr(cls, "isopenicillin N",
            PermissibleValue(text="isopenicillin N"))
        setattr(cls, "kanamycin A",
            PermissibleValue(text="kanamycin A"))
        setattr(cls, "L-681,217",
            PermissibleValue(text="L-681,217"))
        setattr(cls, "lipopeptide antibiotic",
            PermissibleValue(text="lipopeptide antibiotic"))
        setattr(cls, "lividomycin A",
            PermissibleValue(text="lividomycin A"))
        setattr(cls, "lividomycin B",
            PermissibleValue(text="lividomycin B"))
        setattr(cls, "madumycin II",
            PermissibleValue(text="madumycin II"))
        setattr(cls, "meropenem-vaborbactam",
            PermissibleValue(text="meropenem-vaborbactam"))
        setattr(cls, "moenomycin A1",
            PermissibleValue(text="moenomycin A1"))
        setattr(cls, "nalidixic acid",
            PermissibleValue(text="nalidixic acid"))
        setattr(cls, "ostreogrycin B3",
            PermissibleValue(text="ostreogrycin B3"))
        setattr(cls, "para-aminosalicylic acid",
            PermissibleValue(text="para-aminosalicylic acid"))
        setattr(cls, "patricin A",
            PermissibleValue(text="patricin A"))
        setattr(cls, "patricin B",
            PermissibleValue(text="patricin B"))
        setattr(cls, "penicillin N",
            PermissibleValue(text="penicillin N"))
        setattr(cls, "phenelfamycin A",
            PermissibleValue(text="phenelfamycin A"))
        setattr(cls, "phenelfamycin B",
            PermissibleValue(text="phenelfamycin B"))
        setattr(cls, "phenelfamycin C",
            PermissibleValue(text="phenelfamycin C"))
        setattr(cls, "phenelfamycin D",
            PermissibleValue(text="phenelfamycin D"))
        setattr(cls, "phenelfamycin E",
            PermissibleValue(text="phenelfamycin E"))
        setattr(cls, "phenelfamycin F",
            PermissibleValue(text="phenelfamycin F"))
        setattr(cls, "phenelfamycin G",
            PermissibleValue(text="phenelfamycin G"))
        setattr(cls, "phenelfamycin H",
            PermissibleValue(text="phenelfamycin H"))
        setattr(cls, "piperacillin-sulbactam",
            PermissibleValue(text="piperacillin-sulbactam"))
        setattr(cls, "piperacillin-tazobactam",
            PermissibleValue(text="piperacillin-tazobactam"))
        setattr(cls, "polymyxin B",
            PermissibleValue(text="polymyxin B"))
        setattr(cls, "polymyxin B1",
            PermissibleValue(text="polymyxin B1"))
        setattr(cls, "polymyxin B2",
            PermissibleValue(text="polymyxin B2"))
        setattr(cls, "polymyxin B3",
            PermissibleValue(text="polymyxin B3"))
        setattr(cls, "polymyxin B4",
            PermissibleValue(text="polymyxin B4"))
        setattr(cls, "pristinamycin IA",
            PermissibleValue(text="pristinamycin IA"))
        setattr(cls, "pristinamycin IB",
            PermissibleValue(text="pristinamycin IB"))
        setattr(cls, "pristinamycin IIA",
            PermissibleValue(text="pristinamycin IIA"))
        setattr(cls, "quinupristin-dalfopristin",
            PermissibleValue(text="quinupristin-dalfopristin"))
        setattr(cls, "streptogramin A antibiotic",
            PermissibleValue(text="streptogramin A antibiotic"))
        setattr(cls, "streptogramin B antibiotic",
            PermissibleValue(text="streptogramin B antibiotic"))
        setattr(cls, "ticarcillin-clavulanic acid",
            PermissibleValue(text="ticarcillin-clavulanic acid"))
        setattr(cls, "trimethoprim-sulfamethoxazole",
            PermissibleValue(text="trimethoprim-sulfamethoxazole"))
        setattr(cls, "UK-69,753",
            PermissibleValue(text="UK-69,753"))
        setattr(cls, "vernamycin B-gamma",
            PermissibleValue(text="vernamycin B-gamma"))
        setattr(cls, "vernamycin C",
            PermissibleValue(text="vernamycin C"))
        setattr(cls, "virginiamycin S2",
            PermissibleValue(text="virginiamycin S2"))

class ResistancePhenotypeMenu(EnumDefinitionImpl):

    resistant = PermissibleValue(
        text="resistant",
        meaning=ARO["3004301"])
    susceptible = PermissibleValue(
        text="susceptible",
        meaning=ARO["3004302"])
    intermediate = PermissibleValue(
        text="intermediate",
        meaning=ARO["3004300"])
    nonsusceptible = PermissibleValue(
        text="nonsusceptible",
        meaning=ARO["3004303"])
    not_defined = PermissibleValue(text="not_defined")

    _defn = EnumDefinition(
        name="ResistancePhenotypeMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "susceptible-dose dependent",
            PermissibleValue(
                text="susceptible-dose dependent",
                meaning=ARO["3004304"]))

class MeasurementUnitsMenu(EnumDefinitionImpl):

    mm = PermissibleValue(
        text="mm",
        meaning=UO["0000016"])

    _defn = EnumDefinition(
        name="MeasurementUnitsMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mg/L",
            PermissibleValue(
                text="mg/L",
                meaning=UO["0000273"]))

class MeasurementSignMenu(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MeasurementSignMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "<",
            PermissibleValue(text="<"))
        setattr(cls, "<=",
            PermissibleValue(text="<="))
        setattr(cls, "==",
            PermissibleValue(text="=="))
        setattr(cls, ">",
            PermissibleValue(text=">"))
        setattr(cls, ">=",
            PermissibleValue(text=">="))

class LaboratoryTypingMethodMenu(EnumDefinitionImpl):

    MIC = PermissibleValue(text="MIC")
    missing = PermissibleValue(text="missing")

    _defn = EnumDefinition(
        name="LaboratoryTypingMethodMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "agar dilution",
            PermissibleValue(text="agar dilution"))
        setattr(cls, "disk diffusion",
            PermissibleValue(text="disk diffusion"))

class LaboratoryTypingPlatformMenu(EnumDefinitionImpl):

    Microscan = PermissibleValue(
        text="Microscan",
        meaning=ARO["3004400"])
    Phoenix = PermissibleValue(
        text="Phoenix",
        meaning=ARO["3004401"])
    Sensititre = PermissibleValue(
        text="Sensititre",
        meaning=ARO["3004402"])
    Vitek = PermissibleValue(
        text="Vitek",
        meaning=ARO["3004403"])

    _defn = EnumDefinition(
        name="LaboratoryTypingPlatformMenu",
    )

class VendorMenu(EnumDefinitionImpl):

    Biomérieux = PermissibleValue(
        text="Biomérieux",
        meaning=ARO["3004406"])
    Siemens = PermissibleValue(
        text="Siemens",
        meaning=ARO["3004407"])
    Trek = PermissibleValue(
        text="Trek",
        meaning=ARO["3004409"])

    _defn = EnumDefinition(
        name="VendorMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Becton Dickinson",
            PermissibleValue(
                text="Becton Dickinson",
                meaning=ARO["3004405"]))

class LaboratoryTypingMethodVersionOrReagentMenu(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LaboratoryTypingMethodVersionOrReagentMenu",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "96-Well Plate",
            PermissibleValue(
                text="96-Well Plate",
                meaning=BAO["0000513"]))
        setattr(cls, "E-Test",
            PermissibleValue(
                text="E-Test",
                meaning=NCIT["85596"]))
        setattr(cls, "GM-NEG",
            PermissibleValue(text="GM-NEG"))

class TestingStandardMenu(EnumDefinitionImpl):

    BSAC = PermissibleValue(
        text="BSAC",
        meaning=ARO["3004365"])
    CLSI = PermissibleValue(
        text="CLSI",
        meaning=ARO["3004366"])
    DIN = PermissibleValue(
        text="DIN",
        meaning=ARO["3004367"])
    EUCAST = PermissibleValue(
        text="EUCAST",
        meaning=ARO["3004368"])
    NARMS = PermissibleValue(
        text="NARMS",
        meaning=ARO["3007195"])
    NCCLS = PermissibleValue(
        text="NCCLS",
        meaning=ARO["3007193"])
    SFM = PermissibleValue(
        text="SFM",
        meaning=ARO["3004369"])
    SIR = PermissibleValue(
        text="SIR",
        meaning=ARO["3007397"])
    WRG = PermissibleValue(
        text="WRG",
        meaning=ARO["3007398"])
    missing = PermissibleValue(text="missing")

    _defn = EnumDefinition(
        name="TestingStandardMenu",
    )

# Slots
class slots:
    pass

slots.biosample_accession = Slot(uri=DEFAULT_.biosample_accession, name="biosample_accession", curie=DEFAULT_.curie('biosample_accession'),
                   model_uri=DEFAULT_.biosample_accession, domain=None, range=Optional[str])

slots.organism = Slot(uri=DEFAULT_.organism, name="organism", curie=DEFAULT_.curie('organism'),
                   model_uri=DEFAULT_.organism, domain=None, range=Optional[str])

slots.antibiotic = Slot(uri=DEFAULT_.antibiotic, name="antibiotic", curie=DEFAULT_.curie('antibiotic'),
                   model_uri=DEFAULT_.antibiotic, domain=None, range=Optional[Union[str, "AntibioticMenu"]])

slots.resistance_phenotype = Slot(uri=DEFAULT_.resistance_phenotype, name="resistance_phenotype", curie=DEFAULT_.curie('resistance_phenotype'),
                   model_uri=DEFAULT_.resistance_phenotype, domain=None, range=Optional[Union[str, "ResistancePhenotypeMenu"]])

slots.measurement = Slot(uri=DEFAULT_.measurement, name="measurement", curie=DEFAULT_.curie('measurement'),
                   model_uri=DEFAULT_.measurement, domain=None, range=Optional[float])

slots.measurement_units = Slot(uri=DEFAULT_.measurement_units, name="measurement_units", curie=DEFAULT_.curie('measurement_units'),
                   model_uri=DEFAULT_.measurement_units, domain=None, range=Optional[Union[str, "MeasurementUnitsMenu"]])

slots.measurement_sign = Slot(uri=DEFAULT_.measurement_sign, name="measurement_sign", curie=DEFAULT_.curie('measurement_sign'),
                   model_uri=DEFAULT_.measurement_sign, domain=None, range=Optional[Union[str, "MeasurementSignMenu"]])

slots.laboratory_typing_method = Slot(uri=DEFAULT_.laboratory_typing_method, name="laboratory_typing_method", curie=DEFAULT_.curie('laboratory_typing_method'),
                   model_uri=DEFAULT_.laboratory_typing_method, domain=None, range=Optional[Union[str, "LaboratoryTypingMethodMenu"]])

slots.laboratory_typing_platform = Slot(uri=DEFAULT_.laboratory_typing_platform, name="laboratory_typing_platform", curie=DEFAULT_.curie('laboratory_typing_platform'),
                   model_uri=DEFAULT_.laboratory_typing_platform, domain=None, range=Optional[Union[str, "LaboratoryTypingPlatformMenu"]])

slots.vendor = Slot(uri=DEFAULT_.vendor, name="vendor", curie=DEFAULT_.curie('vendor'),
                   model_uri=DEFAULT_.vendor, domain=None, range=Optional[Union[str, "VendorMenu"]])

slots.laboratory_typing_method_version_or_reagent = Slot(uri=DEFAULT_.laboratory_typing_method_version_or_reagent, name="laboratory_typing_method_version_or_reagent", curie=DEFAULT_.curie('laboratory_typing_method_version_or_reagent'),
                   model_uri=DEFAULT_.laboratory_typing_method_version_or_reagent, domain=None, range=Optional[Union[str, "LaboratoryTypingMethodVersionOrReagentMenu"]])

slots.testing_standard = Slot(uri=DEFAULT_.testing_standard, name="testing_standard", curie=DEFAULT_.curie('testing_standard'),
                   model_uri=DEFAULT_.testing_standard, domain=None, range=Optional[Union[str, "TestingStandardMenu"]])
